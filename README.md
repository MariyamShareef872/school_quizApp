# 🧠 School Quiz App (Flask-based)

A fully functional **web-based quiz application** built using **Python (Flask)** and **HTML/CSS/JavaScript**. It supports candidate login, CSV-based questions, a countdown timer, score evaluation, review with ✅❌, and a feature-rich admin panel with charts and Excel export.

---

## 🌟 Features

- 👤 Candidate login system with duplicate attempt prevention
- 📄 Load questions dynamically from a CSV file
- ⏱️ Auto-submit quiz when timer runs out
- 📊 Score calculation with “Selected / Not Selected” result logic
- ✅❌ Review answers after submission
- 🔁 Prevent refresh and reattempts after quiz is submitted
- 🔐 Admin dashboard:
  - View all candidates, scores, and statuses
  - Search/filter by name
  - Delete single or all records
  - 📈 Chart.js visualizations (Score Distribution, Selection Status)
  - 📤 Export results to Excel

---

## 📁 Folder Structure

quizapp/
├── mainfile.py
├── questions.csv
├── quiz.db # (Optional sample DB)
├── templates/
│ ├── quiz.html
│ ├── result.html
│ ├── admin.html
│ ├── review.html
│ ├── candidatelogin.html
│ ├── admin_login.html
│ ├── home.html
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

Make sure Python is installed (preferably version 3.9+)

### 1️⃣ Install Flask

```bash
pip install flask
2️⃣ Run the Application
bash
python mainfile.py
Open your browser and visit:
http://127.0.0.1:5000

🔐 Admin Login
To access the admin dashboard, visit:

http://127.0.0.1:5000/admin_login
You'll need valid admin credentials. These are stored securely (not hard-coded). You can update them manually in the database or enhance the system to support multiple admins.

📦 Technologies Used

Python 3
Flask Web Framework
SQLite3 Database
HTML5 + CSS3
JavaScript (for timer, search, alert handling)
Chart.js (for bar and pie charts)
pandas (for Excel export)

🧠 Why This Project?

This project was built to demonstrate:
Flask-based web application structure
Quiz logic and session management
Real-time user experience with auto-submit timer
CSV/Database integration in Python
Admin interface with CRUD, visualization, and export features

**Perfect for:**

🧪 Python/Flask learners
🎓 Academic assignments or mini projects
📂 AI/EdTech-related portfolios

📜 License
This project is licensed under the MIT License — free to use, modify, and distribute.

🙋‍♀️ Author
Mariyam Shareef
