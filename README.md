## 🧠 School Quiz App (Flask-based)

This is a fully functional **web-based quiz application** built using **Python (Flask)** and HTML/CSS/JavaScript. It supports candidate login, CSV-based questions, a countdown timer, scoring, review with ✅❌, and an admin panel with charts and Excel export.
---
## 🌟 Features

- 👤 **Candidate Login** with duplicate attempt protection
- 📄 **Questions from CSV** (easy to update)
- ⏱️ **Countdown Timer** — quiz auto-submits when time is up
- 📊 **Score Calculation** with “Selected / Not Selected” status
- ✅ ❌ **Review Answers** after submission
- 🛑 **Prevents re-attempts** or refresh abuse
- 🔐 **Admin Panel**
  - View all scores and statuses
  - Filter/search by candidate name
  - Delete individual or all records
  - 📈 View charts (Score Distribution & Selection Status)
  - 📤 Export results to Excel
---
## 📁 Folder Structure

quizapp/
├── mainfile.py
├── questions.csv
├── quiz.db 
├── templates/
│ ├── quiz.html
│ ├── result.html
│ ├── admin.html
│ ├── review.html
│ ├── candidatelogin.html
│ ├── admin_login.html
│ └── home.html
│ └── alreadyattempted.html
├── static/
│ ├── quiz.css
│ ├── result.css
│ ├── admin.css
│ ├── review.css
│ ├── candidatelogin.css
│ ├── admin_login.css
│ ├── alreadyattempted.css
│ └── home.css
---

## 🚀 How to Run Locally
Make sure you have Python installed (preferably 3.9+).

### 1️⃣ Install Flask
```bash
pip install flask
2️⃣ Run the App
bash
Copy
Edit
python mainfile.py
Then open your browser and go to:
http://127.0.0.1:5000

## 🔐Admin Access
## 🔐 Admin Login

To access the admin dashboard, go to:
http://127.0.0.1:5000/admin_login

> You'll need valid admin credentials to log in.
Admin credentials are stored securely (not hard-coded). You can update them manually in the database or extend the login system as needed.

📦 Technologies Used

Python 3
Flask Web Framework
SQLite3 Database
HTML5 + CSS3
JavaScript (for timer & search)
Chart.js (for charts)
pandas (for Excel export)

## 🧠 Why This Project?

- This project was created to demonstrate:
- Web development using Flask and templates
- Managing quiz logic, scoring, and session state
- Using CSV and SQLite for data storage
- Real-time UI interactions with JS
- Full CRUD control and dashboard design
**It’s ideal for:**

- Beginner Python/Flask learners
- Academic evaluations
- Mini-project submissions

📜 License
This project is licensed under the MIT License — free to use, share, and modify.

🙋‍♀️ Author
Mariyam Shareef

