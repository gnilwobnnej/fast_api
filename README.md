# FastAPI Videogames API

A simple RESTful API for managing a videogames collection, built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- Add new videogames (title, genre, platform)
- Retrieve all videogames
- Data validation with Pydantic
- PostgreSQL database integration via SQLAlchemy ORM

## Project Structure

```
.
├── database.py      # Database connection and session setup
├── init_db.py       # Script to initialize database tables
├── main.py          # FastAPI app with API endpoints
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas for request/response
└── README.md        # Project documentation
```

## Requirements

- Python 3.8+
- PostgreSQL
- fastapi 
- sqlalchemy 
- psycopg2-binary 
- uvicorn 
- pydantic

## Setup Instructions

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd fast_api
   ```

2. **Install dependencies**

   ```sh
   pip install fastapi sqlalchemy psycopg2-binary uvicorn pydantic
   ```

3. **Configure the database**

   - Ensure PostgreSQL is running.
   - Update the `DATABASE_URL` in `database.py` if needed:
     ```
     postgresql://<username>:<password>@localhost:<port>/<database>
     ```
   - Example in this project:
     ```
     postgresql://postgres:Jetgrind0!@localhost:5433/videogames
     ```

4. **Create the database and tables**

   - Create the `videogames` database in PostgreSQL if it doesn't exist.
   - Run the table creation script:
     ```sh
     python init_db.py
     ```

5. **Run the API server**

   ```sh
   uvicorn main:app --reload
   ```


   The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000) (local only)

## Screenshots

### 1. Querying the API with curl

Shows a successful `curl` request to the `/videogames/` endpoint, returning all videogames in JSON format.

![curl output showing videogames JSON response](./screenshots/1.png)

### 2. Viewing the database with SQL

Demonstrates a `SELECT * FROM videogames;` query in a PostgreSQL client, displaying the current videogames table contents.

![PostgreSQL SELECT * from videogames result](./screenshots/2.png)

### 3. Using the Swagger UI to add a videogame

Shows the FastAPI interactive docs (`/docs`) with a POST request to add a new videogame using the Swagger UI interface.

![Swagger UI POST /videogames/ example](./screenshots/3.png)

### 4. Updated database after adding games

Displays the updated videogames table in the database after adding new entries via the API.

![PostgreSQL table after adding games](./screenshots/4.png)

### 5. Pretty-printed JSON response

Shows the pretty-printed JSON output of the `/videogames/` GET endpoint, listing all videogames.

![Pretty-printed JSON response](./screenshots/5.png)

### 6. Swagger UI GET /videogames/ response

Displays the Swagger UI showing a successful GET request to `/videogames/`, with the response body and headers.

![Swagger UI GET /videogames/ response](./screenshots/6.png)


## Interactive API Docs

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (local only)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) (local only)

## Notes

- The `title` field is unique for each videogame.
- All database models and schemas are defined in `models.py` and `schemas.py`.
- Database connection and session management are handled in `database.py`.
