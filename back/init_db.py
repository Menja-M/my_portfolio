from app.db.connection import engine, Base
from app.db.models import Section, Project, Contact, Skill, SocialLink

def init_database():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_database()