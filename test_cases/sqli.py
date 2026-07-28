import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
user_id = input("Enter ID: ")
query = "SELECT * FROM users WHERE id = " + user_id
cursor.execute(query)