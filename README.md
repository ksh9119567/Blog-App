# 🚀 FastAPI Blog Platform (Hashnode‑Style)

A modern, full‑stack blogging platform inspired by Hashnode & Medium.  
This project is built with **FastAPI**, **PostgreSQL**, **Redis**, **Docker**, and **React (frontend planned)**.

> This repository contains the backend implementation. Frontend repo will be linked once developed.

---

## 📌 Features (Current & Upcoming)

### ✅ Current Features
- FastAPI backend with modular architecture
- PostgreSQL database with SQLAlchemy + Alembic migrations
- JWT authentication with refresh tokens stored in Redis
- Role‑based access (User & Admin)
- CRUD for Users & Blogs
- Dockerized for Windows/Mac/Linux

### 🧠 Upcoming (Roadmap)
- Follow system, likes, comments, bookmarks
- Blog drafts, publish scheduling
- Notifications, analytics, user profiles
- Markdown editor, SEO, custom domains
- Monetization tools for creators

👉 Full roadmap: `docs/roadmap.txt`

---

## 🏗️ Tech Stack

| Layer | Technology |
|--------|----------------|
| Language | Python 3.11 |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy (async) |
| Migrations | Alembic |
| Cache & Auth Store | Redis |
| Containerization | Docker & Docker Compose |
| Auth | JWT + OAuth2 |
| Task Queue *(Later)* | Celery / RQ |
| Frontend *(Planned)* | React + Tailwind / Next.js |

---

## 📦 Project Structure (Backend)

```
app/
├── core/           # security, config, redis manager
├── db/             # database setup & alembic
├── models/         # SQLAlchemy models
├── routers/        # API routes
├── schemas/        # Pydantic schemas
├── services/       # business logic (future)
├── tests/          # test cases (future)
└── main.py         # app entrypoint
```

---

## 🐳 Docker Setup

To run the entire stack (FastAPI + PostgreSQL + Redis):

```bash
docker compose build
docker compose up -d
```

App will be available at:  
👉 http://localhost:8000/docs

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes using conventional commits
4. Push and create PR

Branch Rules:
- `main` → stable releases only
- `develop` → active development

---

## 📜 License

This project will be licensed under **MIT** (to be added).

---

## 👨‍💻 Author

Developed by **Kunal Sharma & Team**  
Contributions welcome!

---

## ⭐ Support

If you like this project, star the repo to support development.
