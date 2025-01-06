from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from database import Base

class Festival(Base):
    __tablename__ = "festivals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    date = Column(Date)
    organizer = Column(String)
    format = Column(String)

class RockBand(Base):
    __tablename__ = "rockbands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    year_founded = Column(Integer)
    genre = Column(String)
    producer = Column(String)
    members = Column(String)

class Performance(Base):
    __tablename__ = "performances"

    id = Column(Integer, primary_key=True, index=True)
    festival_id = Column(Integer, ForeignKey("festivals.id"))
    band_id = Column(Integer, ForeignKey("rockbands.id"))
    performance_type = Column(String)
    number = Column(Integer)
    duration = Column(Float)