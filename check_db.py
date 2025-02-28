import sqlite3

# Connect to the database
conn = sqlite3.connect("reviews.db")
cursor = conn.cursor()

# Check if any reviews exist
cursor.execute("SELECT * FROM reviews;")
rows = cursor.fetchall()

if rows:
    print("✅ Found reviews in the database:")
    for row in rows:
        print(row)
else:
    print("⚠️ No reviews found in the database!")

# Close the connection
conn.close()
