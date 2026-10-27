"""
Run this once to create attendance.db from schema.sql
Usage: python init_db.py
"""
import sqlite3

connection = sqlite3.connect('attendance.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()

print("Database initialized successfully as attendance.db")
