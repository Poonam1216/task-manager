# Task Manager — Full Stack Assessment

A simple full-stack Task Manager built using Flask, React, and SQLite.

The goal of this project is to demonstrate clean architecture, correctness, testability, and safe evolution of the system.

---

## Tech Stack

Backend

-   Python
-   Flask
-   SQLAlchemy
-   Marshmallow
-   SQLite
-   pytest

Frontend

-   React (Vite)
-   Axios

---

## Architecture Overview

Frontend (React)
↓ HTTP API
Backend (Flask REST API)
↓ ORM
SQLite Database

The backend follows the Flask application factory pattern for modularity and testability.

Key layers:

app/

-   models.py → database models
-   schemas.py → validation and serialization
-   routes.py → API endpoints
-   extensions.py → shared extensions
-   config.py → configuration

tests/

-   automated API tests

---

## Key Technical Decisions

### 1. Flask Application Factory

Allows isolated testing and flexible configuration.

### 2. SQLAlchemy ORM

Prevents direct SQL usage and ensures relational integrity.

### 3. Marshmallow Validation

Prevents invalid states at the API boundary.

Example enforced rules:

-   title required
-   priority must be low/medium/high
-   status must be pending/completed

### 4. SQLite Database

Chosen for simplicity and portability.
Can be swapped with Postgres without architecture changes.

### 5. Automated Tests

pytest tests verify:

-   create task
-   fetch tasks
-   update task
-   delete task

Uses in-memory DB for isolation.

### 6. Clear Separation of Concerns

Frontend → UI only  
Backend → business logic  
Database → persistence

---

## Running Backend

cd backend

source venv/bin/activate

pip install -r requirements.txt

python run.py

Server runs on:
http://127.0.0.1:5000

---

## Running Frontend

cd frontend

npm install

npm run dev

Frontend runs on:
http://localhost:5173

---

## API Endpoints

GET /tasks

POST /tasks

PUT /tasks/:id

DELETE /tasks/:id

---

## Testing

cd backend

pytest

---

## AI Usage

AI tools were used to:

-   accelerate boilerplate generation
-   assist in architecture planning
-   generate validation and test scaffolding

All generated code was reviewed, tested, and verified manually.

---

## Risks and Improvements

Possible improvements:

Authentication

Task ownership (multi-user)

Pagination

Docker deployment

Production database (Postgres)

CI/CD pipeline

---

## Extension Approach

The system is designed to allow:

adding new models without breaking existing routes

adding authentication middleware

replacing database without API changes

adding background workers
