# TEST ASSIGNMENT

**Project:** Task Manager API

You are given a starter project (task-manager-api.zip). Your task is to run the project, understand its structure, and complete the required steps below.

This project is built using:

- FastAPI
- PostgreSQL
- Docker
- Alembic (database migrations)
- Layered architecture (API → Service → Repository → DB)

---

## 1. Environment Setup

1. Install PyCharm from JETBRAINS. 
2. Install Docker Desktop.
3. Install Git.
4. Unzip the provided project.
5. Copy `.env.example` to `.env`.
6. Run:

   ```bash
   docker compose up --build
   ```

7. In a new terminal window, execute:

   ```bash
   docker compose exec backend alembic upgrade head
   ```

   After this, the database table `tasks` must be created.

---

## 2. Required Functional Tasks

You must implement the following improvements:

### A) Add GET /tasks/{id}

- Return task by ID
- Return 404 if not found

### B) Add PATCH /tasks/{id}

- Allow partial update
- Validate priority (1–5)

### C) Add soft delete support to DELETE /tasks/{id}

- Set `is_deleted = True` instead of removing record

### D) Add filtering to GET /tasks

- Filter by status
- Filter by priority

### E) Add basic pagination to GET /tasks

- `limit`
- `offset`

All business logic must remain inside **Service** and **Repository** layers.  
No database logic inside route handlers.

## Projects and relation to Tasks

Add a second entity and link it to tasks:

- **Add a `Project` entity** with fields such as: `name`, `description`, `created_at` (and any others you choose). Create the `projects` table via an Alembic migration.
- **Implement full CRUD for projects:**  
  - `GET /projects`, 
  - `POST /projects`, 
  - `GET /projects/{id}`, 
  - `PATCH /projects/{id}`, 
  - `DELETE /projects/{id}`. 
- **Link tasks to a project:** add a `project_id` column (foreign key to `projects`) to the `tasks` table. Create an Alembic migration for this change. A task may optionally belong to one project.
- **Filter tasks by project:** in `GET /tasks`, support an optional query parameter (e.g. `project_id`) so that the list can be filtered by project.


---

## 3. Technical Requirements

- Follow the existing layered architecture.
- Use SQLAlchemy properly.
- Use Pydantic schemas.
- Use Alembic if DB schema changes.
- Return proper HTTP status codes.
- Do not break Docker setup.

All new features must be committed using Git with meaningful commit messages.

---

## 4. Git Workflow

- Create feature branches for each major task.
- Use descriptive commit messages.
- Merge changes into main branch.
- **Do not commit `.env` file.**

Example branch names:

- `feature/add-get-by-id`
- `feature/add-pagination`
- `feature/add-soft-delete`

---

## 5. Expected Result

After completion:

- Project runs via Docker.
- Database migrations work.
- All endpoints function correctly.
- Swagger documentation is usable.
- Code follows clean architecture principles.
- Git history shows structured development.



