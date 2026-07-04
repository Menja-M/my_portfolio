# app/database.py
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Configuration PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Pour Neon, on ajoute des paramètres spécifiques
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    echo=False,
    connect_args={
        "sslmode": "require",
        "connect_timeout": 10
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dépendance pour obtenir une session de base de données"""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Erreur de base de données: {e}")
        db.rollback()
        raise
    finally:
        db.close()

# Fonction de test de connexion
def test_connection():
    """Teste la connexion à la base de données Neon"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.scalar()
            logger.info(f"✅ Connexion réussie à PostgreSQL!")
            logger.info(f"📦 Version: {version}")
            
            # Test supplémentaire
            result = conn.execute(text("SELECT current_database(), current_user, inet_server_addr()"))
            db_info = result.fetchone()
            logger.info(f"📊 Base: {db_info[0]}, Utilisateur: {db_info[1]}")
            return True
    except Exception as e:
        logger.error(f"❌ Erreur de connexion: {e}")
        return False

def init_db():
    """Initialise la base de données avec les tables"""
    try:
        # Création des tables
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Tables créées avec succès!")
        return True
    except Exception as e:
        logger.error(f"❌ Erreur lors de la création des tables: {e}")
        return False