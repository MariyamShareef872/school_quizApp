from flask import Flask, render_template, request, redirect, session, Response
import sqlite3
import csv

app = Flask(__name__)
app.secret_key = 'secret123'


# Home Page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# Candidate Login
@app.route('/candidate_login', methods=['GET', 'POST'])
def candidate_login():
    error = None
    if request.method == 'POST':
        name = request.form['name'].strip().upper()  # Make name uppercase for uniqueness

        if name == "":
            error = "❌ Name is required."
            return render_template("candidatelogin.html", error=error)

        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        # Make sure table exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS candidates (
                name TEXT UNIQUE,
                score INTEGER,
                status TEXT
            )
        """)

        # Check for duplicates
        cursor.execute("SELECT * FROM candidates WHERE name = ?", (name,))
        if cursor.fetchone():
            conn.close()
            return render_template("already_attempted.html", name=name)  # ✅ Show Already Attempted page
        else:
            session['username'] = name
            conn.close()
            return redirect('/quiz')

    return render_template('candidatelogin.html', error=error)

# Quiz Page
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'username' not in session:
        return redirect('/candidate_login')

    questions = []
    with open('questions.csv', newline='', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            questions.append(row)

    if request.method == 'POST':
        # Only set this when the quiz is submitted!
        if session.get('attempted'):
            return render_template("already_attempted.html")

        score = 0
        user_answers = []

        for i, q in enumerate(questions):
            answer = request.form.get(f'q_{i}')
            user_answers.append(answer)
            if answer == q['answer']:
                score += 2

        status = 'Selected' if score >= 40 else 'Not Selected'

        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO candidates (name, score, status) VALUES (?, ?, ?)",
                           (session['username'], score, status))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("already_attempted.html")
        conn.close()

        # ✅ Only set this AFTER quiz submitted successfully
        session['attempted'] = True
        session['score'] = score
        session['user_answers'] = user_answers
        session['questions'] = questions
        session['status'] = status

        return redirect('/result')

    # ❌ DO NOT set session['attempted'] here!
    return render_template('quiz.html', questions=questions)

# Result Page
@app.route('/result')
def result():
    if 'score' not in session:
        return redirect('/candidate_login')
    return render_template('result.html',
                           name=session['username'],
                           score=session['score'],
                           status=session['status'])


# Review Page
@app.route('/review')
def review():
    if 'user_answers' not in session:
        return redirect('/candidate_login')
    return render_template('review.html',
                           name=session['username'],
                           questions=session['questions'],
                           user_answers=session['user_answers'])


# Admin Login
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['admin_logged_in'] = True
            return redirect('/admin')
        else:
            error = "Invalid credentials"
    return render_template('admin_login.html', error=error)


# Admin Panel
@app.route('/admin')
def admin():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, status FROM candidates")
    data = cursor.fetchall()

    # Score chart data
    cursor.execute("SELECT score FROM candidates")
    scores = [row[0] for row in cursor.fetchall()]

    # Status chart data
    cursor.execute("SELECT status FROM candidates")
    statuses = [row[0] for row in cursor.fetchall()]

    conn.close()
    return render_template('admin.html', data=data, scores=scores, statuses=statuses)


# Delete Individual Record
@app.route('/delete', methods=['POST'])
def delete_record():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    name = request.form['name']
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM candidates WHERE name=?", (name,))
    conn.commit()
    conn.close()
    return redirect('/admin')


# Delete All Records
@app.route('/delete_all', methods=['POST'])
def delete_all():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM candidates")
    conn.commit()
    conn.close()
    return redirect('/admin')


# Export to CSV
@app.route('/export')
def export():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, status FROM candidates")
    data = cursor.fetchall()
    conn.close()

    csv_data = "Name,Score,Status\n"
    for row in data:
        csv_data += f"{row[0]},{row[1]},{row[2]}\n"

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=candidates_results.csv"}
    )


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/home')


if __name__ == '__main__':
    app.run(debug=True)
