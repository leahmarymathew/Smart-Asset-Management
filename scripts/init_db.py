import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')")
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('manager', 'manager123', 'manager')")
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('viewer', 'viewer123', 'viewer')")

conn.commit()
conn.close()
