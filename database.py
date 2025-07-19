#  Import SQLAlchemy engine and ORM utilities 
from sqlalchemy import create_engine                    # For connecting to the database
from sqlalchemy.orm import sessionmaker, declarative_base  # For session and model base class
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

#  Database connection URL 
# Format: dialect+driver://username:password@host:port/database
DATABASE_URL = os.getenv("DATABASE_URL")

#  Create the SQLAlchemy engine 
engine = create_engine(DATABASE_URL)  # Engine manages connections to the database

#  Create a configured "Session" class 
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)  # Factory for DB sessions

#  Base class for all ORM models 
Base = declarative_base()  # All models should inherit from this