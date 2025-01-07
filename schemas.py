from pydantic import BaseModel
from datetime import date
from typing import Optional

class FestivalBase(BaseModel):
    name: str
    location: str
    date: date
    organizer: Optional[str] = None
    format: Optional[str] = None

class FestivalCreate(FestivalBase):
    pass

class Festival(FestivalBase):
    id: int

    class Config:
        from_attributes = True

class RockBandBase(BaseModel):
    name: str
    year_founded: Optional[int] = None
    genre: Optional[str] = None
    producer: Optional[str] = None
    members: Optional[str] = None

class RockBandCreate(RockBandBase):
    pass

class RockBand(RockBandBase):
    id: int

    class Config:
        from_attributes = True

class PerformanceBase(BaseModel):
    festival_id: int
    band_id: int
    performance_type: Optional[str] = None
    number: Optional[int] = None
    duration: Optional[float] = None

class PerformanceCreate(PerformanceBase):
    pass

class Performance(PerformanceBase):
    id: int

    class Config:
        from_attributes = True