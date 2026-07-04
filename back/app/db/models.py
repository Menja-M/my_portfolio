from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.db.connection import Base

class Section(Base):
    __tablename__ = "sections"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    title = Column(String(200))
    subtitle = Column(String(200))
    content = Column(Text)
    background_image = Column(String(500))
    icon = Column(String(100))
    order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    description = Column(Text)
    long_description = Column(Text)
    category = Column(String(100))
    image_url = Column(String(500))
    demo_url = Column(String(500))
    github_url = Column(String(500))
    technologies = Column(Text)  # Stocké comme JSON string
    featured = Column(Boolean, default=False)
    order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    email = Column(String(200), index=True)
    subject = Column(String(200))
    message = Column(Text)
    status = Column(String(50), default="new")  # new, read, replied
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    category = Column(String(100))
    level = Column(Integer)  # 1-100
    icon = Column(String(100))
    order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class SocialLink(Base):
    __tablename__ = "social_links"
    
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(100))
    url = Column(String(500))
    icon = Column(String(100))
    order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())