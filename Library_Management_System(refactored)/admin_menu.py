__author__ = 'user'

from connection import con, cur
import database_admin as db_admin
from classes import Customer, Book
import sqlite3
def add_book():
    book = Book()
    title = input("ENTER TITLE OF BOOK: ")
    author = input("ENTER AUTHOR OF BOOK: ")
    publish = input("ENTER PUBLISHER OF BOOK: ")
    pub_year = input("ENTER PUBLISH YEAR OF BOOK: ")
    book_id = input("ENTER ID OF BOOK: ")
    status = "Available"

    # Set book attributes
    book.set_title(title)
    book.set_author(author)
    book.set_publish(publish)
    book.set_pub_year(pub_year)
    book.set_b_id(book_id)
    book.set_status(status)

    # Add the book to the database
    db_admin.add_book(book)

def remove_book():
    book = Book()
    book_id = input("ENTER BOOK ID TO BE REMOVED: ")
    book.set_b_id(book_id)

    # Remove the book from the database
    db_admin.remove_book(book)

def remove_customer():
    customer_id = input("ENTER CUSTOMER ID TO BE REMOVED: ")

    # Remove the customer from the database
    db_admin.remove_Customer(customer_id)

def all_customers():
    sql = "SELECT * FROM customers"
    cur.execute(sql)
    data = cur.fetchall()

    for line in data:
        print(f"ID: {line[0]}, FNAME: {line[1]}, LNAME: {line[2]}, ADDRESS: {line[3]}, PASSWORD: {line[4]}")

    # No need to commit for a SELECT query in SQLite

def check_history():
    sql = "SELECT * FROM issue_history"
    cur.execute(sql)
    data = cur.fetchall()

    for line in data:
        print(f"Book ID: {line[0]}, Customer ID: {line[1]}, STATUS: {line[2]}")

    # No need to commit for a SELECT query in SQLite
def login_admin(admin_id, password):
    try:
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        sql = "SELECT password FROM admin WHERE admin_id = ?"
        cur.execute(sql, (admin_id,))
        result = cur.fetchone()
        
        if result:
            stored_password = result[0]
            if stored_password == password:
                return True
            else:
                print("Incorrect password")
                return False
        else:
            print("Admin not found")
            return False
    except Exception as e:
        print(f"Error during admin login: {e}")
        return False