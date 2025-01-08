from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Festival(Base):
    __tablename__ = "Festivals"
    
    FestivalID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    Location = Column(String(100), nullable=False)
    Date = Column(Date, nullable=False)
    Organizer = Column(String(100), nullable=True)
    Format = Column(String(50), nullable=True)

    Performances = relationship("Performance", back_populates="Festival")

class RockBand(Base):
    __tablename__ = "RockBands"
    
    BandID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    YearFounded = Column(Integer, nullable=True)
    Genre = Column(String(50), nullable=True)
    Producer = Column(String(100), nullable=True)
    Members = Column(String(250), nullable=True)

    Performances = relationship("Performance", back_populates="RockBand")

class Performance(Base):
    __tablename__ = "Performances"
    
    PerformanceID = Column(Integer, primary_key=True, index=True)
    FestivalID = Column(Integer, ForeignKey("Festivals.FestivalID"), nullable=False)
    BandID = Column(Integer, ForeignKey("RockBands.BandID"), nullable=False)
    PerformanceType = Column(String(100), nullable=True)
    Number = Column(Integer, nullable=True)
    Duration = Column(Float, nullable=True)

    Festival = relationship("Festival", back_populates="Performances")
    RockBand = relationship("RockBand", back_populates="Performances")