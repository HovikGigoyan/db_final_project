from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Festival(Base):
    __tablename__ = "festivals"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    organizer = Column(String(100), nullable=True)
    format = Column(String(50), nullable=True)

    performances = relationship("Performance", back_populates="festival")

class RockBand(Base):
    __tablename__ = "rockbands"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    year_founded = Column(Integer, nullable=True)
    genre = Column(String(50), nullable=True)
    producer = Column(String(100), nullable=True)
    members = Column(String(250), nullable=True)

    performances = relationship("Performance", back_populates="rockband")

class Performance(Base):
    __tablename__ = "performances"
    
    id = Column(Integer, primary_key=True, index=True)
    festival_id = Column(Integer, ForeignKey("festivals.id"), nullable=False)
    band_id = Column(Integer, ForeignKey("rockbands.id"), nullable=False)
    performance_type = Column(String(100), nullable=True)
    number = Column(Integer, nullable=True)
    duration = Column(Float, nullable=True)

    festival = relationship("Festival", back_populates="performances")
    rockband = relationship("RockBand", back_populates="performances")