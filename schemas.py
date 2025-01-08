from pydantic import BaseModel
from datetime import date
from typing import Optional

class FestivalBase(BaseModel):
    Name: str
    Location: str
    Date: date
    Organizer: Optional[str] = None
    Format: Optional[str] = None

class FestivalCreate(FestivalBase):
    pass

class Festival(FestivalBase):
    FestivalID: int

    class Config:
        from_attributes = True

class RockBandBase(BaseModel):
    Name: str
    YearFounded: Optional[int] = None
    Genre: Optional[str] = None
    Producer: Optional[str] = None
    Members: Optional[str] = None

class RockBandCreate(RockBandBase):
    pass

class RockBand(RockBandBase):
    BandID: int

    class Config:
        from_attributes = True

class PerformanceBase(BaseModel):
    FestivalID: int
    BandID: int
    PerformanceType: Optional[str] = None
    Number: Optional[int] = None
    Duration: Optional[float] = None

class PerformanceCreate(PerformanceBase):
    pass

class Performance(PerformanceBase):
    PerformanceID: int

    class Config:
        from_attributes = True