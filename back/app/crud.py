from sqlalchemy.orm import Session
from typing import Optional

from app.db import models
from app.schemas import all_schemas as schemas

# Sections CRUD
def get_section(db: Session, section_id: int):
    return db.query(models.Section).filter(models.Section.id == section_id).first()

def get_sections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Section).order_by(models.Section.order).offset(skip).limit(limit).all()

def create_section(db: Session, section: schemas.SectionCreate):
    db_section = models.Section(**section.model_dump())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section

def update_section(db: Session, section_id: int, section: schemas.SectionUpdate):
    db_section = get_section(db, section_id)
    if db_section:
        update_data = section.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_section, key, value)
        db.commit()
        db.refresh(db_section)
    return db_section

def delete_section(db: Session, section_id: int):
    db_section = get_section(db, section_id)
    if db_section:
        db.delete(db_section)
        db.commit()
    return db_section

# Projects CRUD
def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 100, featured: Optional[bool] = None):
    query = db.query(models.Project)
    if featured is not None:
        query = query.filter(models.Project.featured == featured)
    return query.order_by(models.Project.order).offset(skip).limit(limit).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate):
    db_project = get_project(db, project_id)
    if db_project:
        update_data = project.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = get_project(db, project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project

# Contacts CRUD
def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def get_contacts(db: Session, skip: int = 0, limit: int = 100, status: Optional[str] = None):
    query = db.query(models.Contact)
    if status:
        query = query.filter(models.Contact.status == status)
    return query.order_by(models.Contact.created_at.desc()).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, contact_id: int, contact: schemas.ContactUpdate):
    db_contact = get_contact(db, contact_id)
    if db_contact:
        update_data = contact.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_contact, key, value)
        db.commit()
        db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db_contact = get_contact(db, contact_id)
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact

# Skills CRUD
def get_skill(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()

def get_skills(db: Session, skip: int = 0, limit: int = 100, category: Optional[str] = None):
    query = db.query(models.Skill)
    if category:
        query = query.filter(models.Skill.category == category)
    return query.order_by(models.Skill.order).offset(skip).limit(limit).all()

def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(**skill.model_dump())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def update_skill(db: Session, skill_id: int, skill: schemas.SkillUpdate):
    db_skill = get_skill(db, skill_id)
    if db_skill:
        update_data = skill.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_skill, key, value)
        db.commit()
        db.refresh(db_skill)
    return db_skill

def delete_skill(db: Session, skill_id: int):
    db_skill = get_skill(db, skill_id)
    if db_skill:
        db.delete(db_skill)
        db.commit()
    return db_skill

# Social Links CRUD
def get_social_link(db: Session, link_id: int):
    return db.query(models.SocialLink).filter(models.SocialLink.id == link_id).first()

def get_social_links(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SocialLink).order_by(models.SocialLink.order).offset(skip).limit(limit).all()

def create_social_link(db: Session, link: schemas.SocialLinkCreate):
    db_link = models.SocialLink(**link.model_dump())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def update_social_link(db: Session, link_id: int, link: schemas.SocialLinkUpdate):
    db_link = get_social_link(db, link_id)
    if db_link:
        update_data = link.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_link, key, value)
        db.commit()
        db.refresh(db_link)
    return db_link

def delete_social_link(db: Session, link_id: int):
    db_link = get_social_link(db, link_id)
    if db_link:
        db.delete(db_link)
        db.commit()
    return db_link