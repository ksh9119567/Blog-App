# 🛠️ Project Setup Guide (Windows, Linux, macOS)

This guide explains how to set up and run the **FastAPI Blog Platform** on any operating system.

---

## ✅ Prerequisites

Ensure the following are installed:

| Requirement | Version | Docs |
|--------------|----------|----------------|
| Python | 3.11+ | https://www.python.org/downloads/ |
| Docker | latest | https://docs.docker.com/get-docker/ |
| Docker Compose | latest | Included with Docker Desktop |
| Git | latest | https://git-scm.com/downloads |

---

## 📂 Clone the Repository

```bash
git clone <REPO_URL>
cd blog-app
```

> Replace `<REPO_URL>` with your repository link

---

## 🧰 Environment Setup

Create a `.env` file in the project root with required variables:

```
DATABASE_URL=postgresql+asyncpg://blog_user:blog1234@db:5432/blog_db
POSTGRES_USER=blog_user
POSTGRES_PASSWORD=blog1234
POSTGRES_DB=blog_db

REDIS_URL=redis://redis:6379/0

SECRET_KEY=BLOG_APP_SECRET_KEY
REFRESH_SECRET_KEY=BLOG_APP_REFRESH_SECRET_KEY
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## 🐳 Run with Docker (Recommended for all OS)

### Build and start containers

```bash
docker compose build --no-cache
docker compose up -d
```

### Check container status

```bash
docker ps
```

### Stop containers

```bash
docker compose down
```

> To remove volumes too: `docker compose down -v`

---

## 💻 Local Setup (without Docker)

> Only recommended for development or debugging

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate        # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL & Redis manually

- Install PostgreSQL & Redis based on your OS
- Update `.env` with local host credentials

### 4. Run migrations

```bash
alembic upgrade head
```

### 5. Start the backend

```bash
uvicorn app.main:app --reload
```

---

## 🔍 Useful Docker Commands

| Task | Command |
|--------|------------|
| View logs | `docker logs -f blog_app` |
| Enter container shell | `docker exec -it blog_app bash` |
| Access PostgreSQL | `docker exec -it blog_postgres psql -U blog_user -d blog_db` |
| Access Redis | `docker exec -it blog_redis redis-cli` |

---

## 🎯 Next Steps

- Read `docs/roadmap.txt`
- Set up development branches
- Start implementing Version 1.0 features

---

Happy coding! 🚀
