#!/usr/bin/env python3
import sqlite3

# Connect to the database
conn = sqlite3.connect('test.db')

# Create a cursor object
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS user;")
cursor.execute("DROP TABLE IF EXISTS posts;")

# Commit the transaction
conn.commit()

# Create tables if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(200) NOT NULL,
        email VARCHAR(200) NOT NULL,
        password VARCHAR(25)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        created_by TEXT NOT NULL, 
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        post_user_id INTEGER,
        FOREIGN KEY(post_user_id) REFERENCES user(user_id)
    );
""")

# Commit the transaction again
conn.commit()

# Close the connection
conn.close()
