# Stage 2 — Relational SQL, SQLAlchemy 2.0 ORM & FastAPI Architecture

> **Status:** ✅ COMPLETED (Flagship Capstone Built & Verified)  
> **Goal:** Bridge Python core patterns to enterprise-grade relational database design, modern ORM modeling, and modular RESTful web APIs.

---

## 📌 Executive Overview

Stage 2 represents the transition from procedural and object-oriented Python scripts to production-grade backend engineering. Every module in this stage was written from a blank file, tested against edge cases, and reviewed under strict production standards.

### Core Milestones Achieved:
1. **Relational SQL Foundations**: DDL schema modeling, parameterized DML query execution (SQL injection prevention), foreign key referential integrity, relational set joins, ACID transactions, and B-Tree index optimization verified via `EXPLAIN QUERY PLAN`.
2. **FastAPI Web API Design**: Asynchronous route handling, Pydantic v2 schema validation, centralized HTTP exception mapping, dependency injection (`Depends`), and automatic OpenAPI documentation.
3. **SQLAlchemy 2.0 ORM Depth**: Modern 2.0 syntax (`DeclarativeBase`, `Mapped[T]`, `mapped_column`), Session Unit of Work, dirty tracking, bidirectional relationships (`relationship(back_populates=...)`), and clean repository/service patterns.
4. **Flagship Capstone — Job Application Tracker API**: A fully decoupled, multi-file modular application running across dedicated routers, schemas, services, and database layers.

---

## 📂 Actual Directory Structure

```text
Stage-2/
├── README.md                          # Stage 2 complete documentation (This file)
│
├── SQL/                               # Pure Relational SQL & Database Internals
│   ├── sql_drill_00.py                # DDL: In-memory DB, CREATE TABLE, sqlite_master verification
│   ├── sql_drill_01.py                # Parameterized INSERT & SELECT — SQL injection defense
│   ├── sql_drill_02.py                # Foreign Keys, PRAGMA foreign_keys = ON, ON DELETE CASCADE
│   ├── sql_drill_03.py                # INNER JOIN vs LEFT JOIN, orphan detection via NULL filtering
│   ├── sql_drill_04.py                # ACID Transactions: Atomic money transfer, balance guards, ROLLBACK
│   ├── sql_drill_05.py                # B-Tree Indexes & EXPLAIN QUERY PLAN (SCAN vs SEARCH USING INDEX)
│   └── sql_final_assesment.py         # 🏆 SQL Final Assessment — 5/5 tests passed from blank file
│
├── FastAPI/                           # FastAPI Core & Dependency Injection
│   ├── main.py                        # App skeleton, path/query params, Pydantic v2 validation, Swagger UI
│   ├── users_api.py                   # In-memory SQLite + FastAPI integration (CRUD, 404s, 201 Created)
│   └── di_users_api.py                # Dependency Injection (Depends(get_db)), session generators, response_model
│
└── SQLAlchemy/                        # SQLAlchemy 2.0 ORM & Modular Backend Services
    ├── drill_01_engine_and_model.py   # DeclarativeBase, Mapped[T], mapped_column, engine setup
    ├── drill_02_session_crud.py       # Session Unit of Work, session.add_all(), select() queries
    ├── drill_03_update_delete.py      # Dirty tracking UPDATE & atomic mutations, session.delete()
    ├── drill_04_relationships.py      # Bidirectional 1-to-many relationship, back_populates, cascade insert
    ├── practice.py                    # Kirana Store full CRUD blank-file challenge
    ├── drill_05_fastapi_orm.py        # FastAPI + SQLAlchemy DI integration (Depends(get_db) generator)
    ├── stage_2_grand_capstone.py      # Production Store REST API with custom exceptions, decorators, ORM
    ├── capstone_2.py                  # Authors + Posts Blog REST API with @timer decorator & service layer
    │
    └── job_tracker/                   # 🚀 Flagship Project: Multi-File Modular Job Application Tracker
        ├── __init__.py                # Package initialization & dynamic sys.path resolver
        ├── database.py                # Engine, Base(DeclarativeBase), and get_db session generator
        ├── models.py                  # User and Application relational SQLAlchemy models
        ├── schemas.py                 # Pydantic v2 schemas (Create, Response, StatusUpdate)
        ├── services.py                # Business logic, @timer latency profiling, HTTP error handling
        ├── routers/
        │   ├── __init__.py            # Routers package initialization
        │   ├── users.py               # User endpoints (POST /users, GET /users/{id})
        │   └── applications.py        # Application endpoints (POST, GET, PATCH status, DELETE)
        ├── main.py                    # Application entrypoint mounting routers
        └── README.md                  # Comprehensive job tracker documentation & roadmap
```

---

## 🏆 Detailed Breakdown of Accomplishments

### 1. Pure SQL & Database Internals (`Stage-2/SQL/`)
- **SQL Injection Defense**: Replaced vulnerable string concatenation with parameterized `(?, ?)` queries.
- **Relational Integrity**: Enforced SQLite foreign keys via `PRAGMA foreign_keys = ON`, validating `IntegrityError` when attempting orphan inserts or invalid cascade deletions.
- **Set Operations**: Mastered intersection queries (`INNER JOIN`) vs left-side retention (`LEFT JOIN`), employing `WHERE right.id IS NULL` to uncover orphaned records.
- **ACID Transactions**: Implemented transactional atomicity in money transfers with rowcount verification and automated rollback on failure.
- **Query Optimization**: Inspected query execution plans using `EXPLAIN QUERY PLAN`, proving performance shift from $O(N)$ table scans (`SCAN TABLE`) to $O(\log N)$ logarithmic index lookups (`SEARCH TABLE ... USING INDEX`).

### 2. FastAPI Core & Dependency Injection (`Stage-2/FastAPI/`)
- **Schema Validation**: Automated input parsing and type coercion using Pydantic v2 `BaseModel`, producing structured `422 Unprocessable Entity` responses on invalid payloads.
- **Session Lifecycle via Dependency Injection**: Designed generator dependencies (`get_db`) using `yield` and `finally` blocks to guarantee database connection closure and prevent connection pooling leaks.
- **Data Serialization**: Leveraged `response_model` with `ConfigDict(from_attributes=True)` to decouple internal database structures from public API responses.

### 3. Modern SQLAlchemy 2.0 ORM (`Stage-2/SQLAlchemy/`)
- **Type-Safe Declarative Mapping**: Replaced legacy SQLAlchemy 1.x syntax with modern 2.0 type-annotated constructs (`Mapped[int] = mapped_column(primary_key=True)`).
- **Unit of Work Pattern**: Leveraged `Session` state management, utilizing automatic dirty tracking for in-memory object mutations and batched commits.
- **Relational Mapping**: Configured bidirectional 1-to-many relationships (`User.applications` ↔ `Application.user`) ensuring bidirectional navigation and cascading operations.
- **Layered Service Architecture**: Decoupled business rules and database queries from route handlers, wrapping critical functions in a custom `@timer` decorator for sub-millisecond latency observability.

### 4. Flagship Project: Job Application Tracker API (`job_tracker/`)
A production-ready microservice tracking users and job applications across hiring pipelines:
- **Modular Directory Architecture**: Clean separation into `database`, `models`, `schemas`, `services`, `routers`, and `main`.
- **Full RESTful Endpoints**:
  - `POST /users` (201 Created) — Register user
  - `GET /users/{user_id}` (200 OK) — Retrieve user with linked applications
  - `POST /applications` (201 Created) — Create application with user foreign key validation
  - `GET /applications/{user_id}` (200 OK) — Retrieve all applications for a candidate
  - `PATCH /applications/{app_id}/status` (200 OK) — Update status (`applied`, `interview`, `offer`, `rejected`) with strict 400 validation
  - `DELETE /applications/{app_id}` (204 No Content) — Remove application record
- **Execution Portability**: Dynamic path injection allowing execution from both root repository and local project directories.

---

## 🏃 Quick Start: Running the Flagship Job Tracker

From the `Stage-2/SQLAlchemy` directory:
```powershell
uvicorn job_tracker.main:app --reload
```

Or from inside `Stage-2/SQLAlchemy/job_tracker`:
```powershell
uvicorn main:app --reload
```

Interactive API documentation available at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
