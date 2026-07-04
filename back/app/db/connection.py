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
    pool_size=5,            # Limite le nombre de connexions simultanées
    max_overflow=10,        # Connexions temporaires additionnelles autorisées
    pool_recycle=1800,      # Recycle les connexions toutes les 30 minutes
    pool_pre_ping=True      # Vérifie si la connexion est valide 
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