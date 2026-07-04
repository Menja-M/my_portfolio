#!/usr/bin/env python3
"""Script pour tester la connexion à Neon PostgreSQL"""

import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_neon_connection():
    """Test complet de la connexion Neon"""
    
    # Charger les variables d'environnement
    load_dotenv()
    
    # Récupérer l'URL
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        logger.error("❌ DATABASE_URL non définie dans .env")
        logger.info("💡 Ajoutez: DATABASE_URL=postgresql://user:pass@host/dbname?sslmode=require")
        return False
    
    logger.info("🔌 Tentative de connexion à Neon PostgreSQL...")
    logger.info(f"📝 URL: {database_url.replace('://', '://***:***@')[:50]}...")
    
    try:
        # Créer l'engine
        engine = create_engine(
            database_url,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            connect_args={
                "sslmode": "require",
                "connect_timeout": 10
            }
        )
        
        # Tester la connexion
        with engine.connect() as conn:
            logger.info("✅ Connexion établie!")
            
            # 1. Version PostgreSQL
            result = conn.execute(text("SELECT version()"))
            version = result.scalar()
            logger.info(f"📦 Version PostgreSQL: {version}")
            
            # 2. Informations de la base
            result = conn.execute(text("""
                SELECT 
                    current_database() as database,
                    current_user as user,
                    inet_server_addr() as server_ip,
                    current_setting('server_version_num') as version_num
            """))
            row = result.fetchone()
            logger.info(f"📊 Base: {row[0]}")
            logger.info(f"👤 Utilisateur: {row[1]}")
            logger.info(f"🌐 Serveur: {row[2]}")
            
            # 3. Tester la création d'une table temporaire
            logger.info("🧪 Test des opérations CRUD...")
            
            # Créer une table temporaire
            conn.execute(text("""
                CREATE TEMPORARY TABLE test_connection (
                    id SERIAL PRIMARY KEY,
                    test_data TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            
            # Insérer des données
            conn.execute(
                text("INSERT INTO test_connection (test_data) VALUES (:data)"),
                {"data": "Test Neon PostgreSQL"}
            )
            
            # Lire les données
            result = conn.execute(text("SELECT * FROM test_connection"))
            test_row = result.fetchone()
            logger.info(f"✅ Test CRUD réussi! ID: {test_row[0]}, Donnée: {test_row[1]}")
            
            # 4. Information sur la connexion
            result = conn.execute(text("""
                SELECT 
                    pid,
                    usename,
                    application_name,
                    client_addr,
                    state
                FROM pg_stat_activity 
                WHERE pid = pg_backend_pid()
            """))
            session_info = result.fetchone()
            logger.info(f"🆔 PID: {session_info[0]}")
            logger.info(f"📱 App: {session_info[2] or 'N/A'}")
            logger.info(f"🌍 Client: {session_info[3] or 'local'}")
            logger.info(f"📊 État: {session_info[4]}")
            
            logger.info("🎉 Tous les tests sont passés avec succès!")
            return True
            
    except SQLAlchemyError as e:
        logger.error(f"❌ Erreur SQLAlchemy: {e}")
        logger.info("💡 Vérifiez:")
        logger.info("   - L'URL de connexion")
        logger.info("   - Le mot de passe")
        logger.info("   - Que la base existe")
        logger.info("   - Que l'IP est autorisée dans Neon")
        return False
    except Exception as e:
        logger.error(f"❌ Erreur inattendue: {e}")
        return False

def check_neon_config():
    """Vérifie la configuration recommandée pour Neon"""
    logger.info("\n📋 Configuration recommandée pour Neon:")
    logger.info("  1. Utilisez 'sslmode=require' dans l'URL")
    logger.info("  2. Activez 'Pooled connections' dans Neon")
    logger.info("  3. Vérifiez que votre IP est dans la liste d'accès")
    logger.info("  4. Utilisez des variables d'environnement pour la sécurité")
    logger.info("  5. Pensez à définir un pool_size adapté")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🧪 TEST DE CONNEXION NEON POSTGRESQL")
    print("="*60)
    
    success = test_neon_connection()
    
    if success:
        print("\n✅ Connexion réussie! L'API est prête à être utilisée.")
    else:
        print("\n❌ La connexion a échoué.")
        print("\n🔧 Solutions possibles:")
        print("  1. Vérifiez votre fichier .env")
        print("  2. Générez une nouvelle URL dans le dashboard Neon")
        print("  3. Ajoutez votre IP dans Neon → Settings → IP Allow")
        print("  4. Vérifiez que le mot de passe est correct")
        print("  5. Réinitialisez votre mot de passe si nécessaire")
        sys.exit(1)