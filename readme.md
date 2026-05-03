# 🚀 Smart Task Manager API

A modern backend task management system built with **FastAPI**, **SQLite**, and **SQLAlchemy**.
This project provides a clean REST API for creating, updating, deleting, searching, and managing tasks efficiently.

---

## 🌐 Live Demo

🔗 **Live App:**
https://smart-task-manager-api-3fj2.onrender.com

📄 **Swagger API Docs:**
https://smart-task-manager-api-3fj2.onrender.com/docs

---

## ✨ Features

✅ Create new tasks
✅ View all tasks
✅ Update existing tasks
✅ Delete tasks
✅ Search tasks by title
✅ Filter completed tasks
✅ Filter pending tasks
✅ Set priority levels (`low`, `medium`, `high`)
✅ Add due dates
✅ Clean modular project structure
✅ Live deployment on Render

---

## 🛠️ Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Uvicorn
* Git & GitHub
* Render

---

## 📁 Project Structure

```text
smart-task-manager-api/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── requirements.txt
│── README.md
│── render.yaml
│── routers/
│   └── tasks.py
```

---

## ⚡ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Harish-aiml/smart-task-manager-api.git
cd smart-task-manager-api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

## 📄 API Documentation

After running locally:

```text
http://127.0.0.1:8000/docs
```

---

## 📌 Example Task JSON

```json
{
  "title": "Build portfolio project",
  "description": "Complete FastAPI backend app",
  "completed": false,
  "priority": "high",
  "due_date": "2026-05-15"
}
```

---

## 🎯 Future Improvements

* JWT Authentication
* User Accounts
* PostgreSQL Integration
* Docker Support
* Task Analytics Dashboard
* AI Smart Task Suggestions

---

## 👨‍💻 Author

**Harish**
AI & ML Student | Backend Developer | Future AI Engineer

GitHub: https://github.com/Harish-aiml

---

## ⭐ Support

If you like this project, consider giving it a **star** on GitHub ⭐
