#  Import the SQLAlchemy Base and engine 
from database import Base, engine  # Base: model base class, engine: DB connection
# Import the VideoGame model so its table is created
from models import VideoGame

#  Create all tables in the database 
# This will create the tables defined by all models that inherit from Base
Base.metadata.create_all(bind=engine)