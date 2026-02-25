# agents.md

## Purpose

This file defines the constraints, rules, and guidance used when leveraging AI tools during development of this Task Manager system.

The goal is to ensure AI assistance improves productivity while maintaining correctness, safety, and system integrity.

---

## System Overview

Architecture follows a layered structure:

Frontend (React)
↓
API Layer (Flask routes)
↓
Validation Layer (Marshmallow schemas)
↓
Persistence Layer (SQLAlchemy ORM)
↓
SQLite Database

AI tools were used primarily for:

• scaffolding boilerplate  
• suggesting structure  
• improving validation  
• improving UI layout  
• reviewing architecture decisions

All generated code was manually reviewed and tested.

---

## AI Usage Constraints

AI was NOT allowed to:

• introduce raw SQL queries  
• bypass schema validation  
• modify database directly outside ORM  
• introduce hidden background processes  
• generate unreviewed production logic

AI suggestions were always:

• reviewed manually  
• tested locally  
• verified using automated tests

---

## Data Integrity Rules

The system enforces:

• Task title is required  
• Task status must be:

-   pending
-   completed

• Task priority must be:

-   low
-   medium
-   high

• Default values are applied at model level to prevent invalid states.

Validation occurs using Marshmallow schemas before persistence.

---

## API Safety Rules

All endpoints follow REST conventions:

GET /tasks  
POST /tasks  
PUT /tasks/{id}  
DELETE /tasks/{id}

Invalid inputs return HTTP 400.

Missing resources return HTTP 404.

---

## Testing Rules

Automated tests validate:

• Task creation  
• Task retrieval  
• Task update  
• Task deletion

Tests run using isolated SQLite database.

This ensures behavior remains correct during future changes.

---

## Observability

System includes logging for:

• task creation  
• updates  
• deletion  
• validation errors

This ensures failures are visible and diagnosable.

---

## Change Safety

The system is designed to allow safe extension, including:

• adding authentication  
• adding due dates  
• adding pagination  
• adding multi-user support

without breaking existing functionality.

---

## Human Review Requirement

All AI-generated code must be reviewed, understood, and verified before being committed.

AI is used as an assistant, not as an autonomous developer.
