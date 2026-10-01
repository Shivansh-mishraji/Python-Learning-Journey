# 🎯 Job Application Tracker API

A production-style, modular RESTful API built with **FastAPI**, **SQLAlchemy 2.0**, and **Pydantic v2** to track job applications, application stages, and user profiles.

This project serves as an evolving flagship backend system designed from scratch following enterprise multi-file software architecture patterns.

---

## 🏗️ Architecture & Project Structure

The project enforces a strict **separation of concerns** across modular layers:

```text
job_tracker/
├── __init__.py              # Package initialization and dynamic sys.path resolver
├── database.py              # Engine setup, DeclarativeBase, and get_db session generator
├── models.py                # SQLAlchemy 2.0 ORM relational models (User, Application)
├── schemas.py               # Pydantic v2 validation and serialization schemas
├── services.py              # Business logic layer, CRUD operations, @timer latency profiling
├── routers/
│   ├── __init__.py          # Routers package initialization
│   ├── users.py             # User endpoints (POST, GET)
│   └── applications.py      # Application endpoints (POST, GET, PATCH, DELETE)
├── main.py                  # FastAPI application entry point and router registration
└── README.md                # Project documentation and roadmap
```

### Layer Responsibilities
- **`database.py`**: Configures SQLite engine (`job_tracker.db`) and exports the `get_db()` dependency generator managing clean session lifecycles (`yield session`).
- **`models.py`**: Defines database tables using modern SQLAlchemy 2.0 `Mapped[...]` and `mapped_column(...)` with foreign keys and bidirectional `relationship(back_populates=...)`.
- **`schemas.py`**: Pure Pydantic v2 data transfer objects (DTOs) with `ConfigDict(from_attributes=True)` for ORM model serialization.
- **`services.py`**: Decoupled service layer containing all business rules, input constraints, and database queries. Monitored with an active `@timer` decorator for latency tracking.
- **`routers/`**: Lean controllers using FastAPI's `APIRouter` to handle HTTP status codes, dependency injection, and request dispatching.
- **`main.py`**: Application factory that mounts all sub-routers onto the root FastAPI instance.

---

## 📡 API Endpoints

| Method | Endpoint | Status Code | Description | Request Body | Response Body |
|:---|:---|:---:|:---|:---|:---|
| `POST` | `/users` | `201 Created` | Register a new user | `UserCreate` (`name`, `email`) | `UserResponse` |
| `GET` | `/users/{user_id}` | `200 OK` | Fetch user details and applications | — | `UserResponse` |
| `POST` | `/applications` | `201 Created` | Add a new job application | `ApplicationCreate` | `ApplicationResponse` |
| `GET` | `/applications/{user_id}` | `200 OK` | List all applications for a user | — | `list[ApplicationResponse]` |
| `PATCH` | `/applications/{app_id}/status` | `200 OK` | Update application status | `StatusUpdate` (`status`) | `ApplicationResponse` |
| `DELETE` | `/applications/{app_id}` | `204 No Content` | Delete an application | — | — |

> **Allowed Application Statuses**: `"applied"`, `"interview"`, `"offer"`, `"rejected"`. Invalid transitions trigger HTTP `400 Bad Request`.

---

## ✅ What Has Been Done (Current Milestone)

- [x] **Modular Multi-File Refactor**: Successfully decoupled monolithic script architecture into dedicated `database`, `models`, `schemas`, `services`, and `routers` packages.
- [x] **Relational Schema**: Implemented 1-to-many relationship between `User` and `Application` with relational integrity.
- [x] **FastAPI Dependency Injection**: Implemented deterministic DB session lifecycles using `Depends(get_db)`.
- [x] **Defensive Error Handling**: Service layer raises appropriate HTTP exceptions (`404 Not Found`, `400 Bad Request`) for missing records and invalid status strings.
- [x] **Performance Profiling**: Wrapped service methods with a `@timer` decorator logging sub-millisecond execution times.
- [x] **Flexible Entrypoint Execution**: Configured path resolution enabling clean startup both from repository subfolders and root package contexts.
- [x] **End-to-End Test Suite**: Verified complete CRUD workflow using automated FastAPI test client.

---

## 🔮 What Next Will Be Done (Roadmap)

### Phase 2: Stage 3 Enhancements
- [ ] **Alembic Database Migrations**: Replace `Base.metadata.create_all()` with version-controlled, reversible migration scripts.
- [ ] **PostgreSQL Migration**: Swap SQLite for production PostgreSQL with environment-based configuration (`.env`).
- [ ] **Automated Pytest Suite**: Build dedicated unit and integration tests with transactional rollback fixtures to guarantee 100% test isolation.

### Phase 3: Authentication & Security
- [ ] **User Authentication**: Implement JWT-based access tokens with password hashing via `bcrypt` / `passlib`.
- [ ] **Ownership Protection**: Restrict application operations so users can only view, update, or delete their own applications.

### Phase 4: AI & Cloud Deployment
- [ ] **AI Job Fit Analyzer**: Integrate Gemini API / LLM to compare user resume text against the `job_description` field and generate a match score with interview tips.
- [ ] **Containerization**: Create multi-stage `Dockerfile` and `docker-compose.yml` orchestrating API and database services.
- [ ] **Cloud Deployment**: Deploy the containerized API with automated health checks and CI/CD pipeline.

---

## 🚀 Getting Started

### 1. Run the Server
From the `Stage-2/SQLAlchemy` directory:
```powershell
uvicorn job_tracker.main:app --reload
```

Or from inside the `job_tracker` directory:
```powershell
cd job_tracker
uvicorn main:app --reload
```

### 2. Interactive API Documentation
Once running, open your browser to:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
