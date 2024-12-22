__author__ = 'user'
from connection import con, cur
from classes import Customer, Book
import sqlite3

def check_customer_exists(id):
    try:
        sql = "SELECT COUNT(*) FROM customers WHERE customer_id = ?"
        cur.execute(sql, (id,))
        res = cur.fetchone()
        count = res[0]
        return count == 1
    except sqlite3.DatabaseError as e:
        print(f"Error checking customer existence: {e}")
        return False

def add_book(book):
    try:
        title = book.get_title()
        author = book.get_author()
        publish = book.get_publish()
        pub_year = book.get_pub_year()
        b_id = book.get_b_id()
        status = book.get_status()

        sql = """INSERT INTO book (title, author, publisher, pub_year, book_id, status)
                 VALUES (?, ?, ?, ?, ?, ?)"""
        cur.execute(sql, (title, author, publish, pub_year, b_id, status))
        con.commit()
        print("Book Added")
    except sqlite3.DatabaseError as e:
        print(f"Error adding book: {e}")

def remove_book(book):
    try:
        b_id = book.get_b_id()
        sql = "DELETE FROM book WHERE book_id = ?"
        cur.execute(sql, (b_id,))
        con.commit()
        print("Book Removed")
    except sqlite3.DatabaseError as e:
        print(f"Error removing book: {e}")

def remove_customer(c_id):
    try:
        sql = "DELETE FROM customers WHERE customer_id = ?"
        cur.execute(sql, (c_id,))
        con.commit()
        print("Customer Removed")
    except sqlite3.DatabaseError as e:
        print(f"Error removing customer: {e}")
import sqlite3
from hashlib import sha256
from connection import con, cur

# Function to hash the password
def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest()

# Function to authenticate admin login
def login_admin(admin_id, password):
    try:
        hashed_password = hash_password(password)  # Hash the input password
        sql = "SELECT password FROM admin WHERE admin_id = ?"
        cur.execute(sql, (admin_id,))
        result = cur.fetchone()

        if result:
            stored_hash = result[0]
            if stored_hash == hashed_password:
                return True  # Authentication successful
            else:
                return False  # Incorrect password
        else:
            return False  # Admin not found
    except sqlite3.DatabaseError as e:
        print(f"Error during authentication: {e}")
        return False
