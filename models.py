#  Import SQLAlchemy base and column types 
from sqlalchemy import Column, Integer, String  # Column types for table fields
from database import Base                      # Base class for SQLAlchemy models

#  VideoGame model: represents a videogame record in the database 
class VideoGame(Base):
    __tablename__ = "videogames"  # Name of the table in the database

    # Unique ID for each videogame (Primary Key)
    id = Column(Integer, primary_key=True, index=True)
    # Title of the videogame (must be unique)
    title = Column(String, unique=True, index=True)
    # Genre of the videogame (e.g., Action, RPG)
    genre = Column(String)
    # Platform for the videogame
    platform = Column(String)