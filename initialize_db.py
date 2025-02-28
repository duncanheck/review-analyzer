import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("reviews.db")
cursor = conn.cursor()

# Create table for storing reviews
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        author TEXT,
        rating INTEGER,
        text TEXT,
        business_name TEXT,
        location TEXT
    )
''')

# Commit and close
conn.commit()
conn.close()

print("✅ Database initialized successfully! Table 'reviews' is ready.")
