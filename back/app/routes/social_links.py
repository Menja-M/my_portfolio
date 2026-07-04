from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud
from app.db.connection import get_db
from app.schemas import all_schemas as schemas

router = APIRouter(prefix="/api/social-links", tags=["social-links"])

@router.get("/", response_model=List[schemas.SocialLink])
def get_social_links(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    links = crud.get_social_links(db, skip=skip, limit=limit)
    return links

@router.get("/{link_id}", response_model=schemas.SocialLink)
def get_social_link(link_id: int, db: Session = Depends(get_db)):
    link = crud.get_social_link(db, link_id=link_id)
    if not link:
        raise HTTPException(status_code=404, detail="Social link not found")
    return link

@router.post("/", response_model=schemas.SocialLink)
def create_social_link(link: schemas.SocialLinkCreate, db: Session = Depends(get_db)):
    return crud.create_social_link(db=db, link=link)

@router.put("/{link_id}", response_model=schemas.SocialLink)
def update_social_link(link_id: int, link: schemas.SocialLinkUpdate, db: Session = Depends(get_db)):
    db_link = crud.update_social_link(db, link_id=link_id, link=link)
    if not db_link:
        raise HTTPException(status_code=404, detail="Social link not found")
    return db_link

@router.delete("/{link_id}")
def delete_social_link(link_id: int, db: Session = Depends(get_db)):
    db_link = crud.delete_social_link(db, link_id=link_id)
    if not db_link:
        raise HTTPException(status_code=404, detail="Social link not found")
    return {"message": "Social link deleted successfully"}