__author__ = 'user'

import sqlite3

# Establish SQLite database connection
# Replace 'library.db' with your desired database file name
con = sqlite3.connect('library.db')

# Create a cursor object to interact with the database
cur = con.cursor()

print("SQLite connection established successfully.")
