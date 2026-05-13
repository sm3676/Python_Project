## Module 15: Final Project

This is my final project developed using Python with Docker support.


## 🚀 Features

- CRUD operations
- Database integration
- Docker containerization
- GitHub integration

### 🔐 Authentication
- User Registration
- User Login (JWT आधारित authentication)
- Secure password hashing

### 🧮 Calculations (BREAD)
- ➕ Add Calculation
- 📥 Browse All Calculations
- 🔍 Read Single Calculation
- ✏️ Edit Calculation
- ❌ Delete Calculation

---

## 🛠️ Tech Stack
- Python (FastAPI)
- SQLite / PostgreSQL
- Pydantic
- JWT Authentication
- Playwright (E2E Testing)
- Pytest
- Docker
- GitHub Actions (CI/CD)

---

## 📂 Project Structure

backend-assignment/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── Auth.py
│ └── routes/
│ ├── user.py
│ └── calculation.py
│
├── module13-fastapi-jwt/
│ └── Frontend/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ └── script.js
│
├── tests/
│ ├── test_users.py
│ ├── test_calculations.py
│ └── test_e2e.py
│
├── requirements.txt
├── Dockerfile
└── README.md


---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Run FastAPI server

uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000/docs

🧪 Run Tests

pytest

🌐 Frontend Usage

Open:

register.html → Register user
login.html → Login & get token
index.html → Perform calculations
script.js


🐳 Docker

Build image

docker run -p 5000:5000 sm3676/backend-assignment

Run container

docker hub https://hub.docker.com/r/sm3676/backend-assignment -- for project

⚙️ GitHub Actions (CI/CD)

Automatically runs tests on push
Builds project
Ensures everything works before submission




