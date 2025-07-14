import sqlite3

conn = sqlite3.connect("SynapseMind/data/synapsemind.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()

def save_message(role, content):
    cursor.execute("INSERT INTO chat_history (role, content) VALUES (?, ?)", (role, content))
    conn.commit()

def get_chat_history():
    cursor.execute("SELECT role, content FROM chat_history ORDER BY id")
    return cursor.fetchall()
