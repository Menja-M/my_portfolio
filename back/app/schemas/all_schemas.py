from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Section Schemas
class SectionBase(BaseModel):
    name: str
    title: Optional[str] = None
    subtitle: Optional[str] = None
    content: Optional[str] = None
    background_image: Optional[str] = None
    icon: Optional[str] = None
    order: Optional[int] = 0
    is_active: Optional[bool] = True

class SectionCreate(SectionBase):
    pass

class SectionUpdate(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    content: Optional[str] = None
    background_image: Optional[str] = None
    icon: Optional[str] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class Section(SectionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Project Schemas
class ProjectBase(BaseModel):
    title: str
    description: str
    long_description: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    demo_url: Optional[str] = None
    github_url: Optional[str] = None
    technologies: Optional[str] = None
    featured: Optional[bool] = False
    order: Optional[int] = 0
    is_active: Optional[bool] = True

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    demo_url: Optional[str] = None
    github_url: Optional[str] = None
    technologies: Optional[str] = None
    featured: Optional[bool] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class Project(ProjectBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Contact Schemas
class ContactBase(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    status: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    subject: Optional[str] = None
    message: Optional[str] = None

class Contact(ContactBase):
    id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Skill Schemas
class SkillBase(BaseModel):
    name: str
    category: str
    level: int
    icon: Optional[str] = None
    order: Optional[int] = 0
    is_active: Optional[bool] = True

class SkillCreate(SkillBase):
    pass

class SkillUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    level: Optional[int] = None
    icon: Optional[str] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class Skill(SkillBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Social Link Schemas
class SocialLinkBase(BaseModel):
    platform: str
    url: str
    icon: Optional[str] = None
    order: Optional[int] = 0
    is_active: Optional[bool] = True

class SocialLinkCreate(SocialLinkBase):
    pass

class SocialLinkUpdate(BaseModel):
    platform: Optional[str] = None
    url: Optional[str] = None
    icon: Optional[str] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class SocialLink(SocialLinkBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True