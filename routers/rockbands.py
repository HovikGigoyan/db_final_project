from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(
    prefix="/rockbands",
    tags=["RockBands"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.RockBand)
def create_rockband(rockband: schemas.RockBandCreate, db: Session = Depends(get_db)):
    new_rockband = models.RockBand(**rockband.dict())
    db.add(new_rockband)
    db.commit()
    db.refresh(new_rockband)
    return new_rockband

@router.get("/", response_model=list[schemas.RockBand])
def read_rockbands(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rockbands = db.query(models.RockBand).offset(skip).limit(limit).all()
    return rockbands

@router.get("/{band_id}", response_model=schemas.RockBand)
def read_rockband(band_id: int, db: Session = Depends(get_db)):
    band = db.query(models.RockBand).filter(models.RockBand.id == band_id).first()
    if not band:
        raise HTTPException(status_code=404, detail="RockBand not found")
    return band

@router.put("/{band_id}", response_model=schemas.RockBand)
def update_rockband(band_id: int, rockband_update: schemas.RockBandCreate, db: Session = Depends(get_db)):
    band = db.query(models.RockBand).filter(models.RockBand.id == band_id).first()
    if not band:
        raise HTTPException(status_code=404, detail="RockBand not found")
    for key, value in rockband_update.dict().items():
        setattr(band, key, value)
    db.commit()
    db.refresh(band)
    return band

@router.delete("/{band_id}")
def delete_rockband(band_id: int, db: Session = Depends(get_db)):
    band = db.query(models.RockBand).filter(models.RockBand.id == band_id).first()
    if not band:
        raise HTTPException(status_code=404, detail="RockBand not found")
    db.delete(band)
    db.commit()
    return {"message": "RockBand deleted successfully"}