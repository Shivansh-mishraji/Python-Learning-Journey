<div align="center">

# ⚡ Python Backend & AI Engineering Journey

<p align="center">
  <img src="assets/banner.jpg" alt="Python Backend Architecture Banner" width="100%" style="border-radius: 12px;" />
</p>

[![Python Version](https://img.shields.io/badge/Python-3.13%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20Async%20APIs-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQL Database](https://img.shields.io/badge/Database-SQLite%20%7C%20PostgreSQL-336791.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Code Standard](https://img.shields.io/badge/Standard-Production%20Grade%20%26%20Typed-success.svg)](#-engineering-standards-enforced)
[![Git Commits](https://img.shields.io/badge/Commits-Conventional-orange.svg)](#)
[![Status](https://img.shields.io/badge/Status-Active%20Sprint%202-brightgreen.svg)](#-curriculum--progress-tracker)

<p align="center">
  <b>A rigorous, from-scratch journey toward building production-ready Python backend systems, relational databases, and AI-integrated architectures.</b><br>
  <i>No copy-pasting. No vibe-coding. Every module built and verified from blank-file specifications.</i>
</p>

---

</div>

## 📌 Executive Summary

This repository chronicles an intensive, industry-calibrated journey toward mastering production-grade backend engineering, relational database internals, and scalable AI systems.

**The Mission**: Build senior-level engineering depth as an undergraduate to dominate technical screens, excel during internships, and secure a **Pre-Placement Offer (PPO) before 4th Year** at a top-tier product company or high-paying startup (₹8–25 LPA / $20k–$50k USD remote).

Rather than relying on passive tutorials, toy scripts, or surface-level copy-pasting:
- **Zero Toy Topics**: Strict adherence to enterprise production tools (SQLAlchemy 2.0 ORM, Alembic migrations, PostgreSQL, FastAPI, Pydantic v2, Docker, pytest, Vector RAG) instead of throwaway abstractions.
- **Spiral Synthesis**: Continuous forward progression paired with cumulative active recall. Every major milestone culminates in an **Integrated Capstone** built from a blank slate without starter code.
- **Senior-Depth Rigor**: Understanding every layer from first principles — failure modes, concurrency, data integrity, N+1 query bottlenecks, and deterministic resource lifecycles.

---

## 🗺️ Curriculum & Roadmap

<p align="center">
  <img src="assets/roadmap.jpg" alt="Backend AI Engineering Roadmap" width="100%" style="border-radius: 12px;" />
</p>

| Stage | Focus Area | Key Concepts & Industry Deliverables | Status |
|:---|:---|:---|:---:|
| **Stage 1** | **Python Core & Advanced Systems** | Encapsulation, `@property` validation, Custom Exceptions, Decorators (`@wraps`), Generators (`yield` pipelines), Typing | **✅ Mastered** |
| **Stage 2** | **Relational SQL, SQLAlchemy 2.0 ORM & FastAPI** | Relational Modeling, Parameterized SQL, B-Tree Indexes, SQLAlchemy 2.0 DeclarativeBase, Session Unit of Work, Relationships, FastAPI DI | **🔥 Active** |
| **Grand Capstone** | **Stage 2 Blank-Slate Production API** | **Full Store REST API**: FastAPI + SQLAlchemy 2.0 + Pydantic v2 + Custom Exceptions + Decorators + Multi-Table Relations | **⏳ Next** |
| **Stage 3** | **PostgreSQL, Alembic Migrations & Testing** | PostgreSQL engine, version-controlled migrations (Alembic), automated testing with `pytest`, fixtures, and DB rollback isolation | **⏳ Upcoming** |
| **Stage 4** | **Docker, Cloud DevOps & Production AI** | Multi-stage Docker, `docker-compose`, Gemini API, vector embeddings, pgvector/ChromaDB RAG pipeline, Cloud deployment | **⏳ Upcoming** |

---

## 🚀 Step-by-Step Journey & Concrete Achievements

```
Step 1: OOP & Encapsulation ──► Step 2: Decorators & Streams ──► Step 3: Security Capstone ──► Step 4: SQL & FastAPI
```

---

### Step 1: Python Core & Advanced Encapsulation
> **Milestone:** Eliminating recursion bugs, mastering private state encapsulation, and building custom domain exception hierarchies.

<p align="center">
  <img src="assets/step1_oop.jpg" alt="Python OOP Mastery and Property Validation" width="100%" style="border-radius: 12px;" />
</p>

#### 💡 Core Breakthroughs:
- **Private State Protection (`_balance`):** Internalized why getters must return `self._balance` rather than `self.balance` to avoid infinite recursive call stack overflows.
- **Validation Setters:** Enforced business constraints directly at attribute assignment (`@balance.setter` raising `ValueError` on invalid states).
- **Domain Exceptions (`class InsufficientFundsError(Exception)`):** Replaced silent `print()` failures with structured exception raising for enterprise reliability.

#### 📁 Implemented Modules:
- [`Stage-1/projects/bank.py`](Stage-1/projects/bank.py): `BankAccount` with transaction guards and property validation.
- [`Stage-1/projects/catalog.py`](Stage-1/projects/catalog.py): Smart product catalog with automated dynamic discount calculations.
- [`Stage-1/projects/inventory.py`](Stage-1/projects/inventory.py): CLI Inventory Manager leveraging `@dataclass` and Python magic methods (`__repr__`, `__len__`).

---

### Step 2: Higher-Order Decorators & Lazy Generator Streaming
> **Milestone:** Intercepting execution flows with decorators and building memory-efficient data pipelines processing streams in $O(1)$ memory.

<p align="center">
  <img src="assets/step2_pipeline.jpg" alt="Python Decorators and Generator Streaming Pipeline" width="100%" style="border-radius: 12px;" />
</p>

#### 💡 Core Breakthroughs:
- **Function Introspection (`@functools.wraps`):** Preserved function metadata (`__name__`, docstrings, type annotations) across wrapper layers.
- **Universal Parameter Forwarding (`*args, **kwargs`):** Engineered decorators capable of intercepting any callable signature without breaking interfaces.
- **Lazy Stream Processing (`yield`):** Replaced eager memory-hungry list allocations (`return [x for x in data]`) with chained generator pipelines processing multi-gigabyte log streams with constant memory footprint.

#### 📁 Implemented Modules:
- [`Stage-1/projects/decorators.py`](Stage-1/projects/decorators.py): Custom execution timing (`@timer`) and argument validation (`@validate_positive`).
- [`Stage-1/projects/generator.py`](Stage-1/projects/generator.py): 3-stage chained generator log pipeline (`read_logs` → `filter_errors` → `parse_ip`).
- [`Stage-1/interview/`](Stage-1/interview/): High-throughput `RateLimiter` and `@require_auth` interceptors.

---

### Step 3: Robust File I/O & The 7-in-1 Secure Audit Vault Capstone
> **Milestone:** Cross-platform file manipulation with `pathlib`, leak-free resource cleanup via Context Managers, and integrating all 7 core backend patterns from a blank file.

<p align="center">
  <img src="assets/step3_vault.jpg" alt="Cybersecurity Backend Audit Vault Architecture" width="100%" style="border-radius: 12px;" />
</p>

#### 💡 Core Breakthroughs:
- **Leak-Free Context Managers (`with open(...)`):** Guaranteed deterministic file descriptor closure even during runtime exception handling.
- **Cross-Platform Path Manipulation (`pathlib.Path`):** Unified POSIX and Windows filesystem operations with automatic directory provisioning (`parents=True, exist_ok=True`).
- **The 7-in-1 Integration Capstone:** Built [`Stage-2/sprint-1-capstone.py`](Stage-2/sprint-1-capstone.py) completely from scratch, synthesizing:
  1. *Custom Exception:* `SecurityViolationError`
  2. *OOP Encapsulation:* `User` with `@property` role validation
  3. *Decorator Security:* `@require_admin` role-based access control
  4. *Type Hints:* Full typing across arguments and returns
  5. *File I/O:* JSON audit event logging
  6. *Generators:* Lazy log streaming from disk
  7. *Test Suite:* Automated positive & negative security assertions

#### 📁 Implemented Modules:
- [`Stage-2/file_io.py`](Stage-2/file_io.py): Core `pathlib` and JSON persistence utility engine.
- [`Stage-2/file_io_challenge.py`](Stage-2/file_io_challenge.py): Blank-file user storage and data serialization challenge.
- [`Stage-2/sprint-1-capstone.py`](Stage-2/sprint-1-capstone.py): **Sprint 1 & 2 Capstone — Secure System Audit Vault**.

---

### Step 4: Relational SQL Database Engineering & FastAPI Architecture
> **Milestone:** Designing relational schemas, defending against SQL injections, mastering relational JOINs, and transitioning into asynchronous web APIs.

<p align="center">
  <img src="assets/step4_sql_ai.jpg" alt="Relational Database and FastAPI AI Architecture" width="100%" style="border-radius: 12px;" />
</p>

#### 💡 Core Breakthroughs:
- **SQL Injection Prevention:** Enforced parameterized query execution using `(?, ?, ?)` placeholder substitution instead of vulnerable raw string interpolation.
- **Relational Integrity:** Implemented Foreign Key constraints linking `resumes` child records to parent `users` entities.
- **Relational Set Operations:** Engineered `INNER JOIN` (intersection) vs. `LEFT JOIN` (complete left-side retention with NULL fallbacks).
- **Asynchronous Architecture Pathway:** Laying database foundations to power the upcoming **AI Resume & Job Description Analyzer** backend.

#### 📁 Implemented Modules:
- [`Stage-2/SQL/sql_drill_00.py`](Stage-2/SQL/sql_drill_00.py): In-memory DB connection, DDL `CREATE TABLE`, `sqlite_master` verification — written from blank file.
- [`Stage-2/SQL/sql_drill_01.py`](Stage-2/SQL/sql_drill_01.py): Parameterized `INSERT (?, ?, ?)` and `SELECT fetchall()` — **passed on first try, zero guidance.**
- [`Stage-2/SQL/sql_drill_02.py`](Stage-2/SQL/sql_drill_02.py): Relational schema with `FOREIGN KEY` constraints, `PRAGMA foreign_keys = ON`, and `ON DELETE` behavior — `IntegrityError` verified against orphan records.
- [`Stage-2/SQL/sql_drill_03.py`](Stage-2/SQL/sql_drill_03.py): `INNER JOIN` (intersection only) vs `LEFT JOIN` (full left-side retention with `NULL` fallback) — orphan detection pattern using `WHERE right_table.id IS NULL`.
- [`Stage-2/SQL/sql_drill_04.py`](Stage-2/SQL/sql_drill_04.py): ACID Transactions & `ROLLBACK` in code — atomic money transfer with `WHERE balance >= amount` guards, `cursor.rowcount` zero-check, and exception rollback defense.
- [`Stage-2/SQL/sql_drill_05.py`](Stage-2/SQL/sql_drill_05.py): B-Tree Indexes & `EXPLAIN QUERY PLAN` — inspecting query execution plans, verifying `SCAN` (unindexed $O(N)$ full table scan) vs `SEARCH USING INDEX` ($O(\log N)$ B-Tree lookup).
- [`Stage-2/SQL/sql_final_assesment.py`](Stage-2/SQL/sql_final_assesment.py): **SQL Final Assessment** — 5/5 tests passed from blank file. All concepts integrated: FK constraints, INNER/LEFT JOINs, ACID transactions, B-Tree index verification via `EXPLAIN QUERY PLAN`.
- [`Stage-2/FastAPI/main.py`](Stage-2/FastAPI/main.py): FastAPI app skeleton — 3 GET routes, path parameters, Pydantic v2 `BaseModel` request body validation (`POST /users`), automatic HTTP 422 on invalid input, Swagger UI at `/docs`.
- [`Stage-2/FastAPI/users_api.py`](Stage-2/FastAPI/users_api.py): **SQL + FastAPI Integration** — in-memory SQLite database wired to live REST endpoints (`GET /users`, `GET /users/{id}` with 404 handler, `POST /users` returning HTTP 201 + `lastrowid`), thread-safe connection pooling.
- [`Stage-2/FastAPI/di_users_api.py`](Stage-2/FastAPI/di_users_api.py): **Dependency Injection & Lifecycle Management** — production pattern using `Depends(get_db)`, generator dependencies (`yield conn` + `finally: conn.close()`), `response_model=UserResponse` schema enforcement, `sqlite3.Row` dictionary mapping.
- [`Stage-2/SQLAlchemy/drill_01_engine_and_model.py`](Stage-2/SQLAlchemy/drill_01_engine_and_model.py): **Engine & Modern Declarative Mapping** — SQLAlchemy 2.0 `DeclarativeBase`, `Mapped[T]`, `mapped_column`, and deterministic path configuration.
- [`Stage-2/SQLAlchemy/drill_02_session_crud.py`](Stage-2/SQLAlchemy/drill_02_session_crud.py): **Session Lifecycle & Object Queries** — Unit of Work, `session.add_all()`, typed SELECT queries with `select(Model).scalars().all()`.
- [`Stage-2/SQLAlchemy/drill_03_update_delete.py`](Stage-2/SQLAlchemy/drill_03_update_delete.py): **ORM UPDATE & DELETE** — In-memory dirty tracking, atomic attribute mutations, `session.delete()`, and transactional persistence.
- [`Stage-2/SQLAlchemy/drill_04_relationships.py`](Stage-2/SQLAlchemy/drill_04_relationships.py): **One-to-Many Relationships & Unit of Work** — Bidirectional mapping (`ForeignKey`, `relationship()`, `back_populates`), cascade insert via Unit of Work, and verified bidirectional back-links.
- [`Stage-2/SQLAlchemy/practice.py`](Stage-2/SQLAlchemy/practice.py): **Consolidated Blank-File Challenge: Kirana Store System** — Full 5-phase lifecycle synthesis from scratch (Declarative models, Unit of Work cascade insert, relational queries, dirty tracking update, and object deletion).
- `Stage-2/SQLAlchemy/drill_05_fastapi_orm.py`: **FastAPI + SQLAlchemy DI Integration** — Generator dependency injection `get_db()`, Pydantic v2 serialization (`from_attributes=True`), and full REST CRUD. *(Next)*
- `Stage-2/stage_2_grand_capstone.py`: **Stage 2 Grand Capstone: Production Store REST API** — Blank-slate synthesis of Custom Exceptions, Decorators, Pydantic v2, SQLAlchemy 2.0 ORM, and FastAPI endpoints. *(Milestone Gateway)*

---

## 🛠️ Technical Stack & Production Tooling

```
Core Language     : Python 3.13+ (Strict Type Hints, Generator Pipelines, Functional Decorators)
Web Framework     : FastAPI (Async Route Handlers, Dependency Injection, Centralized Exception Middleware)
ORM & Persistence : SQLAlchemy 2.0 (Unit of Work, Dirty Tracking, Eager Loading vs Lazy Loading)
Database Engines  : PostgreSQL (Production Target), SQLite (Local Isolation), ACID Relational Integrity
Schema Migrations : Alembic (Zero-Downtime Versioned Migrations — Upcoming)
Data Validation   : Pydantic v2 (Request Sanitization, Response Schema Serialization)
Testing & Quality : pytest, fixtures, DB rollback isolation, mock interfaces (Upcoming)
DevOps & Deploy   : Docker (Multi-stage builds), docker-compose, GitHub Actions CI (Upcoming)
AI Engineering    : Google Gemini API, Vector Embeddings, pgvector/ChromaDB RAG Pipelines (Upcoming)
```

---

## 📂 Repository Structure

```
Python-Learning-Journey/
├── .agents/                    # Workspace mentor rules, progress logs & strategy
├── assets/                     # Milestone architecture diagrams & roadmap visuals
│   ├── banner.jpg              # Hero banner image
│   ├── roadmap.jpg             # 4-Stage engineering roadmap
│   ├── step1_oop.jpg           # Step 1: OOP & Property Validation visual
│   ├── step2_pipeline.jpg      # Step 2: Decorators & Stream Pipeline visual
│   ├── step3_vault.jpg         # Step 3: Secure Audit Vault Capstone visual
│   └── step4_sql_ai.jpg        # Step 4: Relational SQL & AI Architecture visual
├── Stage-1/                    # Stage 1: Python Core Mastery (COMPLETED)
│   ├── projects/               # Capstone implementations (vault, bank, catalog, generator)
│   ├── practice/               # Blank-file re-implementation proofs
│   ├── interview/              # RateLimiter, require_auth, APIResponse drills
│   ├── Assessment/             # Self-assessment verification tests
│   └── DSA/                    # Data Structures & Algorithms track (HashMap Two Sum O(n))
├── Stage-2/                    # Stage 2: Relational SQL, SQLAlchemy 2.0 ORM & FastAPI (ACTIVE)
│   ├── SQL/                    # Relational SQL drills (DDL, parameterized DML, FK constraints, JOINs, ACID, Indexes)
│   │   ├── sql_drill_00.py     # ✅ DDL from blank file — CREATE TABLE, sqlite_master
│   │   ├── sql_drill_01.py     # ✅ Parameterized INSERT & SELECT — first-try pass
│   │   ├── sql_drill_02.py     # ✅ Foreign Keys, PRAGMA, ON DELETE behavior, Soft Deletes
│   │   ├── sql_drill_03.py     # ✅ INNER JOIN vs LEFT JOIN, NULL handling, orphan detection
│   │   ├── sql_drill_04.py     # ✅ ACID Transactions, Atomic Balance Guards, ROLLBACK handling
│   │   ├── sql_drill_05.py         # ✅ B-Tree Indexes & EXPLAIN QUERY PLAN (SCAN vs SEARCH)
│   │   ├── sql_final_assesment.py  # ✅ SQL FINAL ASSESSMENT — 5/5 tests, all concepts integrated
│   │   └── joins.py            # Relational set-matching engine
│   ├── FastAPI/                # FastAPI REST API drills
│   │   ├── main.py             # ✅ Drill 01 & 02 — App skeleton, Pydantic v2 validation, Swagger UI
│   │   ├── users_api.py        # ✅ Drill 03 — SQL + FastAPI Integration (CRUD, 404s, 201 Created)
│   │   └── di_users_api.py     # ✅ Drill 04 — Dependency Injection (Depends, generator lifecycle, response_model)
│   └── SQLAlchemy/             # SQLAlchemy 2.0 ORM drills (High-ROI Production ORM)
│       ├── drill_01_engine_and_model.py  # ✅ DeclarativeBase & Mapped Models
│       ├── drill_02_session_crud.py      # ✅ Session Lifecycle, add_all, SELECT
│       ├── drill_03_update_delete.py     # ✅ Dirty tracking UPDATE & DELETE
│       ├── drill_04_relationships.py     # ✅ 1-to-Many Relationships & Unit of Work Cascade
│       ├── practice.py                   # ✅ Consolidated Blank-File Challenge (Kirana Store Full CRUD)
│       └── drill_05_fastapi_orm.py       # ⏳ FastAPI + SQLAlchemy DI Integration (NEXT)
└── README.md                   # Complete journey documentation
```

---

## 🚀 How to Run & Verify

Clone the repository and execute any module directly:

```bash
# Clone the repository
git clone https://github.com/Shivansh-mishraji/Python-Learning-Journey.git
cd Python-Learning-Journey

# Run Stage 2 Capstone (Secure Audit Vault - 7 Concepts Integrated)
python Stage-2/sprint-1-capstone.py

# Run SQLAlchemy ORM Dirty Tracking & Persistence Drill
python Stage-2/SQLAlchemy/drill_03_update_delete.py

# Run SQL Relational JOINs Engine
python Stage-2/SQL/joins.py

# Run Lazy Log Stream Generator
python Stage-1/projects/generator.py
```

---

## 💡 Engineering Standards Enforced

1. **Explicit Type Annotations:** Strict typing on all signatures using `Optional`, `Union`, `Callable`, `Generator`.
2. **Never Mask Exceptions:** Domain-specific exceptions raised explicitly instead of generic `print()` statements.
3. **Deterministic Resource Safety:** Context managers (`with`) mandatory for all I/O, database sessions, and connections to guarantee leak-free cleanup.
4. **Verified Mastery:** Every concept proven by writing working implementations from a completely blank file without starter code.
5. **Senior Depth Standard:** Every concept mastered at production-engineer depth — internals, failure modes, tradeoffs, and real-world implications — not just surface-level API usage.
6. **Zero Toy Distractions:** Strict focus on enterprise-standard tools (SQLAlchemy 2.0, PostgreSQL, Alembic, Docker, pytest) that deliver direct leverage in technical rounds and high-paying jobs.
7. **Spiral Synthesis & Active Recall:** Continuous forward progression reinforced by periodic blank-slate integrated capstones and unannounced spaced retrieval challenges.

---

<div align="center">

*Maintained with pride by **Shivansh Mishra** • Aspiring Backend & AI Engineer*<br>
[LinkedIn Profile](https://www.linkedin.com/in/shivansh-mishra-132b97358/) • [GitHub Profile](https://github.com/Shivansh-mishraji)

</div>
