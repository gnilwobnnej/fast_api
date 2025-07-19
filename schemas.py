#  Import Pydantic's BaseModel for data validation and serialization 
from pydantic import BaseModel

#  Base schema for VideoGame (shared fields) 
class VideoGameBase(BaseModel):
    title: str      # Title of the videogame
    genre: str      # Genre of the videogame
    platform: str   # Platform of the videogame

#  Schema for creating a new VideoGame (inherits all fields from base) 
class VideoGameCreate(VideoGameBase):
    pass  # No extra fields needed for creation

#  Schema for reading a VideoGame from the database (includes ID) 
class VideoGameRead(VideoGameBase):
    id: int  # Unique ID of the videogame

    class Config:
        orm_mode = True  # Enable compatibility with ORM objects (eg SQLAlchemy)