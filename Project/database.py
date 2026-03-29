import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "finance.db") # 將資料庫同程式在同一個資料夾

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            amount REAL NOT NULL,
            type TEXT NOT NULL, 
            date TIMESTAMP DEFAULT (datetime('now', 'localtime'))
        )
    ''')
    conn.commit()
    conn.close()

def add_record(item, amount, record_type):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    val = float(amount) if record_type == "Income" else -float(amount)
    cursor.execute("INSERT INTO record (item, amount, type) VALUES (?, ?, ?)", 
                   (item, val, record_type))
    conn.commit()
    conn.close()

def delete_record(record_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM record WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    print(f"ID {record_id} Delete form the Database")

def get_all_records():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, item, amount, type, date FROM record ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_total_amount():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM record")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0