import sqlite3
from pathlib import Path
path = Path("99-work/16-inventory.sqlite")
path.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(path) as connection:
    connection.execute("CREATE TABLE IF NOT EXISTS services (name TEXT PRIMARY KEY, owner TEXT NOT NULL)")
    connection.execute("INSERT OR IGNORE INTO services VALUES (?, ?)", ("checkout", "commerce"))
    rows = connection.execute("SELECT name, owner FROM services ORDER BY name").fetchall()
    print(rows)
try:
    with sqlite3.connect(path) as connection:
        connection.execute("INSERT INTO services VALUES (?, ?)", ("checkout", "search"))
except sqlite3.IntegrityError:
    print("duplicate identity rejected")
