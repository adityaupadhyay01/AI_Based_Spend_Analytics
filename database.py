import sqlite3


def create_database():

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()

    print("Database and table created successfully!")


if __name__ == "__main__":
    create_database()