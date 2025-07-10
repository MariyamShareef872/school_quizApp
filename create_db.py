import sqlite3

# Connect or create the database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create candidates table
cursor.execute('''
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    score INTEGER,
    status TEXT
)
''')

conn.commit()
conn.close()
print("✅ Database and candidates table created successfully.")
