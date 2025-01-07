from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import List
import sqlalchemy as sa
import models, schemas

router = APIRouter(
    prefix="/festivals",
    tags=["Festivals"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Festival)
def create_festival(festival: schemas.FestivalCreate, db: Session = Depends(get_db)):
    new_festival = models.Festival(**festival.dict())
    db.add(new_festival)
    db.commit()
    db.refresh(new_festival)
    return new_festival


@router.get("/", response_model=List[schemas.Festival])
def read_festivals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    festivals = db.query(models.Festival).offset(skip).limit(limit).all()
    return festivals


@router.get("/{festival_id}", response_model=schemas.Festival)
def read_festival(festival_id: int, db: Session = Depends(get_db)):
    festival = db.query(models.Festival).filter(models.Festival.id == festival_id).first()
    if not festival:
        raise HTTPException(status_code=404, detail="Festival not found")
    return festival


@router.put("/{festival_id}", response_model=schemas.Festival)
def update_festival(festival_id: int, festival: schemas.FestivalCreate, db: Session = Depends(get_db)):
    db_festival = db.query(models.Festival).filter(models.Festival.id == festival_id).first()
    if not db_festival:
        raise HTTPException(status_code=404, detail="Festival not found")
    for key, value in festival.dict().items():
        setattr(db_festival, key, value)
    db.commit()
    db.refresh(db_festival)
    return db_festival


@router.delete("/{festival_id}")
def delete_festival(festival_id: int, db: Session = Depends(get_db)):
    db_festival = db.query(models.Festival).filter(models.Festival.id == festival_id).first()
    if not db_festival:
        raise HTTPException(status_code=404, detail="Festival not found")
    db.delete(db_festival)
    db.commit()
    return {"message": "Festival deleted successfully"}


@router.get("/filter", response_model=List[schemas.Festival])
def filter_festivals(name: str, location: str, db: Session = Depends(get_db)):
    festivals = db.query(models.Festival).filter(
        models.Festival.name == name,
        models.Festival.location == location
    ).all()
    return festivals


@router.put("/update-format")
def update_festival_format(location: str, new_format: str, db: Session = Depends(get_db)):
    updated = db.query(models.Festival).filter(
        models.Festival.location == location
    ).update({models.Festival.format: new_format})
    db.commit()
    if updated:
        return {"message": f"Updated {updated} festivals to format '{new_format}'."}
    return {"message": "No festivals updated."}


@router.get("/group-by-format")
def group_by_format(db: Session = Depends(get_db)):
    results = db.query(
        models.Festival.format,
        sa.func.count(models.Festival.id).label("count")
    ).group_by(models.Festival.format).all()
    return results

@router.get("/", response_model=List[schemas.Festival])
def read_festivals(skip: int = 0, limit: int = 10, sort_by: str = "name", db: Session = Depends(get_db)):
    valid_sort_columns = ["name", "location", "date", "organizer", "format"]
    if sort_by not in valid_sort_columns:
        raise HTTPException(status_code=400, detail="Invalid sort field.")
    festivals = db.query(models.Festival).order_by(getattr(models.Festival, sort_by)).offset(skip).limit(limit).all()
    return festivals