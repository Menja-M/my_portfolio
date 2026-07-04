from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud
from app.db.connection import get_db
from app.schemas import all_schemas as schemas


router = APIRouter(prefix="/api/sections", tags=["sections"])

@router.get("/", response_model=List[schemas.Section])
def get_sections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sections = crud.get_sections(db, skip=skip, limit=limit)
    return sections

@router.get("/{section_id}", response_model=schemas.Section)
def get_section(section_id: int, db: Session = Depends(get_db)):
    section = crud.get_section(db, section_id=section_id)
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")
    return section

@router.post("/", response_model=schemas.Section)
def create_section(section: schemas.SectionCreate, db: Session = Depends(get_db)):
    return crud.create_section(db=db, section=section)

@router.put("/{section_id}", response_model=schemas.Section)
def update_section(section_id: int, section: schemas.SectionUpdate, db: Session = Depends(get_db)):
    db_section = crud.update_section(db, section_id=section_id, section=section)
    if not db_section:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section

@router.delete("/{section_id}")
def delete_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.delete_section(db, section_id=section_id)
    if not db_section:
        raise HTTPException(status_code=404, detail="Section not found")
    return {"message": "Section deleted successfully"}