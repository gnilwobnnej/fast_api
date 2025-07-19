#  Import necessary libraries and modules 
from fastapi import FastAPI, Depends  # FastAPI for API creation, Depends for dependency injection
from sqlalchemy.orm import Session    # SQLAlchemy session for DB operations
from typing import List               # For type hinting list responses

# Import local modules for DB, models, and schemas
from database import SessionLocal     # SessionLocal: SQLAlchemy session factory
from models import VideoGame          # VideoGame: SQLAlchemy model for videogames
from schemas import VideoGameCreate, VideoGameRead  # Pydantic schemas for request/response

#  Initialize FastAPI app 
app = FastAPI()

#  Dependency: Get a database session for each request 
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db         # Provide the session to the request
    finally:
        db.close()      # Ensure the session is closed after the request

#  Endpoint: Add a new videogame (POST) 
@app.post("/videogames/", response_model=VideoGameRead)
def create_game(game: VideoGameCreate, db: Session = Depends(get_db)):
    """
    Create a new videogame entry in the database.
    - game: VideoGameCreate schema with game details from the request body
    - db: Database session (injected)
    Returns the created videogame as a response.
    """
    db_game = VideoGame(**game.dict())  # Create a VideoGame model instance from input data
    db.add(db_game)                     # Add to the session
    db.commit()                         # Commit to save in DB
    db.refresh(db_game)                 # Refresh to get updated data (e.g., ID)
    return db_game

#  Endpoint: Retrieve all videogames (GET) 
@app.get("/videogames/", response_model=List[VideoGameRead])
def read_games(db: Session = Depends(get_db)):
    """
    Retrieve all videogame entries from the database.
    - db: Database session (injected)
    Returns a list of videogames.
    """
    return db.query(VideoGame).all()