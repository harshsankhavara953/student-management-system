<h1 align="center">🎓 Student Management System</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&center=true&width=360&lines=Welcome+to+Student+Management+System;Built+With+Django+%26+SQLite" alt="Typing SVG" />
</p>


<p align="center">
  <b>A Django-powered web app to manage student data efficiently — register, login, search, update, and more!</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.11-yellow?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite&logoColor=black" />
  <img src="https://img.shields.io/badge/VS%20Code-IDE-blue?style=for-the-badge&logo=visualstudiocode&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML-Templates-orange?style=for-the-badge&logo=html5&logoColor=white" />
</p>

---

## 🛠️ Tech Stack

| 🧩 Category        | 🚀 Technologies Used                     |
|-------------------|-------------------------------------------|
| 🌐 Framework      | Django (Python)                           |
| 💡 Language       | Python 3.11                               |
| 🧱 Database       | SQLite3                                   |
| 🎨 Frontend       | HTML5, CSS3 (basic styling)               |
| 🧰 Tools & IDE    | Git, GitHub, Visual Studio Code           |

---

## ✨ Features

- 🔐 User registration and login
- 📝 Student insertion, update, and deletion
- 🔍 Search student records by ID or name
- 🏆 Display top 3 students by marks
- 📦 Clean MVC structure with Django
- 💾 Lightweight SQLite3 database backend

---

## 📁 Project Structure

```plaintext
student_demo/
│
├── student_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── delete.html
│   │   ├── index.html
│   │   ├── insert.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── search.html
│   │   ├── top3.html
│   │   └── update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── student_demo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md

```
##⚙️ Installation & Setup
```
Follow these steps to run this project on your local machine:

✅ Prerequisites
Python 3.10 or higher

Git

pip

Virtualenv (optional but recommended)
```

🔧 Steps to Run Locally
```
# 1. Clone the repository
git clone https://github.com/harshsankhavara953/student-management-system.git
cd student-management-system

# 2. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install Django
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Start the server
python manage.py runserver

# 6. Visit in your browser
http://127.0.0.1:8000/
```

👨‍💻 Author
Made with ❤️
by Harsh Sankhavara
