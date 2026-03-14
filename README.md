```markdown
# Smart Quiz Game (Python GUI + FastAPI + Database)

## Project Overview
Smart Quiz Game is an advanced Python-based quiz application built using a **GUI interface**, **FastAPI backend**, and **database integration**. The project demonstrates full-stack development using Python with modular architecture suitable for workshops and academic demonstrations.

The application allows users to take quizzes, submit answers, calculate scores, and view leaderboard rankings. Questions are served from a backend API and stored in a database.

---

## Features

- Python GUI Quiz Interface
- FastAPI Backend Server
- SQLite Database
- Random Question Generation
- Score Calculation
- Leaderboard System
- Modular Project Structure
- REST API Integration
- Scalable Architecture

---

## Technology Stack

### Frontend (GUI)
- Python
- Tkinter / PyQt5

### Backend
- FastAPI
- Uvicorn

### Database
- SQLite
- SQLAlchemy ORM

### Other Tools
- GitHub
- Requests Library

---

## Project Architecture

```

GUI Application (Python Tkinter / PyQt)
|
|
Requests API
|
FastAPI Server
|
SQLAlchemy
|
SQLite

```

---

## Project Structure

```

quiz_master/

backend/
main.py
routes.py
models.py
database.py

gui/
app.py
quiz.py
result.py

database/
quiz.db

README.md

```

---

## Installation

### 1. Clone the Repository

```

git clone [https://github.com/your-username/quiz_master.git](https://github.com/your-username/quiz_master.git)
cd quiz_master

```

### 2. Install Dependencies

```

pip install fastapi uvicorn sqlalchemy requests

```

---

## Running the Backend Server

Navigate to the backend folder:

```

cd backend

```

Run the server:

```

uvicorn main:app --reload

```

Open API documentation:

```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

```

---

## Running the GUI Application

Navigate to the GUI folder:

```

cd gui

```

Run the application:

```

python app.py

```

---

## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | /questions | Retrieve quiz questions |
| POST | /submit | Submit quiz score |
| GET | /leaderboard | Get top scores |

---

## Team Member Responsibilities

| Member | Role | Responsibility |
|------|------|------|
| Member 1 | GUI Developer | Design quiz interface |
| Member 2 | Backend Developer | Create FastAPI endpoints |
| Member 3 | Database Engineer | Design database models |
| Member 4 | Quiz Logic Developer | Implement scoring & quiz flow |
| Member 5 | Integration & Testing | Connect GUI with backend |

---

## Future Improvements

- Timer for each question
- Difficulty levels (Easy / Medium / Hard)
- Admin panel for adding questions
- Improved GUI using PyQt5
- Data analytics dashboard
- Online deployment

---

## Demonstration Flow

1. Start FastAPI backend server
2. Launch GUI application
3. Start quiz
4. Answer questions
5. Submit score
6. View leaderboard

---

## Learning Outcomes

This project demonstrates:

- GUI application development using Python
- REST API development using FastAPI
- Database integration using SQLAlchemy
- Software architecture design
- Team collaboration using GitHub

---

## License

This project is for educational purposes.
```
