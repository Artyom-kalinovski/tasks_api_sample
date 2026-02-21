# Task Manager API

Pseudo-production FastAPI project with PostgreSQL, Docker and Alembic migrations.

---

# 🖥️ Required Software on Windows (From Scratch)

If you're developing on Windows and have nothing installed yet, you will need:

| Software | Purpose |
|----------|---------|
| **Git** | Clone repo, branches, commits. Download: [git-scm.com](https://git-scm.com/download/win). |
| **Docker Desktop** | Run the app and PostgreSQL in containers. Download: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/). |
| **PostgreSQL client** | Connect to the DB in the container for debugging and viewing data (DBeaver, pgAdmin, or psql in WSL). The DB and app run inside Docker; the client runs on your machine. |

After installation, verify in terminal:

    git --version
    docker --version

---

# 🧰 Full Setup Guide (From Zero)

## 1️⃣ Install Docker

Download and install Docker Desktop.
After installation:

    docker --version

---

## 2️⃣ Install Git

Install Git and verify:

    git --version

---

# 🚀 Run Project with Docker

1. Unzip project
2. Open terminal in project folder
3. Copy environment file (Windows: `copy .env.example .env`, Linux/Mac: `cp .env.example .env`):

    copy .env.example .env

4. Start containers:

    docker compose up --build

---

# 🗄 Run Database Migration (IMPORTANT)

Open new terminal window and run:

    docker compose exec backend alembic upgrade head

This will create the tasks table.

---

**Endpoints:**

- `GET /tasks` — list of tasks (excluding deleted)
- `GET /tasks/{id}` — task by ID (404 if not found or deleted)

Swagger: http://localhost:8000/docs

Health: http://localhost:8000/health

All API requests require this header:

    X-API-Key: supersecret

---

# 📚 What This Project Teaches

• FastAPI architecture
• PostgreSQL
• Docker
• Alembic migrations
• Clean layered structure
• Git workflow

---
