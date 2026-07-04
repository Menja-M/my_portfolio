from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app import crud
from app.db.connection import get_db
from app.schemas import all_schemas as schemas

router = APIRouter(prefix="/api/skills", tags=["skills"])

@router.get("/", response_model=List[schemas.Skill])
def get_skills(
    skip: int = 0, 
    limit: int = 100,
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    skills = crud.get_skills(db, skip=skip, limit=limit, category=category)
    return skills

@router.get("/{skill_id}", response_model=schemas.Skill)
def get_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = crud.get_skill(db, skill_id=skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.post("/", response_model=schemas.Skill)
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    return crud.create_skill(db=db, skill=skill)

@router.put("/{skill_id}", response_model=schemas.Skill)
def update_skill(skill_id: int, skill: schemas.SkillUpdate, db: Session = Depends(get_db)):
    db_skill = crud.update_skill(db, skill_id=skill_id, skill=skill)
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill

@router.delete("/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = crud.delete_skill(db, skill_id=skill_id)
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"message": "Skill deleted successfully"}