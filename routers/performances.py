from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import List
import models, schemas

router = APIRouter(
    prefix="/performances",
    tags=["Performances"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Performance)
def create_performance(performance: schemas.PerformanceCreate, db: Session = Depends(get_db)):
    new_performance = models.Performance(**performance.dict())
    db.add(new_performance)
    db.commit()
    db.refresh(new_performance)
    return new_performance

@router.get("/", response_model=list[schemas.Performance])
def read_performances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    performances = db.query(models.Performance).offset(skip).limit(limit).all()
    return performances

@router.get("/{performance_id}", response_model=schemas.Performance)
def read_performance(performance_id: int, db: Session = Depends(get_db)):
    perf = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if not perf:
        raise HTTPException(status_code=404, detail="Performance not found")
    return perf

@router.put("/{performance_id}", response_model=schemas.Performance)
def update_performance(performance_id: int, performance_update: schemas.PerformanceCreate, db: Session = Depends(get_db)):
    perf = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if not perf:
        raise HTTPException(status_code=404, detail="Performance not found")
    for key, value in performance_update.dict().items():
        setattr(perf, key, value)
    db.commit()
    db.refresh(perf)
    return perf

@router.delete("/{performance_id}")
def delete_performance(performance_id: int, db: Session = Depends(get_db)):
    perf = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if not perf:
        raise HTTPException(status_code=404, detail="Performance not found")
    db.delete(perf)
    db.commit()
    return {"message": "Performance deleted successfully"}


@router.get("/performances", response_model=List[schemas.Performance])
def get_performances_with_details(db: Session = Depends(get_db)):
    performances = db.query(
        models.Performance.id,
        models.Festival.name.label("festival_name"),
        models.RockBand.name.label("band_name"),
        models.Performance.performance_type,
        models.Performance.duration
    ).join(models.Festival, models.Performance.festival_id == models.Festival.id)\
     .join(models.RockBand, models.Performance.band_id == models.RockBand.id).all()
    return performances
