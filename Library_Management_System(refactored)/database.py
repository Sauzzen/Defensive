import sqlite3
import hashlib

# Database connection
con = sqlite3.connect('library.db')
cur = con.cursor()
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def make_all_tables():
    try:
        sql = """CREATE TABLE IF NOT EXISTS customers (
                     customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     first_name TEXT NOT NULL,
                     last_name TEXT NOT NULL,
                     address TEXT NOT NULL,
                     password TEXT NOT NULL
                 )"""
        cur.execute(sql)
        con.commit()
        print("Customers table created successfully.")
    except sqlite3.DatabaseError as e:
        print(f"Error creating customers table: {e}")
# In your database.py file

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

def make_all_tables1():
    try:
        sql = """CREATE TABLE IF NOT EXISTS book (
                     title TEXT NOT NULL,
                     author TEXT NOT NULL,
                     publisher TEXT NOT NULL,
                     pub_year INTEGER NOT NULL,
                     book_id TEXT PRIMARY KEY,
                     status TEXT CHECK (status IN ('Issued', 'Due', 'Available'))
                 )"""
        cur.execute(sql)
        con.commit()
        print("Books table created successfully.")
    except sqlite3.DatabaseError as e:
        print(f"Error creating books table: {e}")

def make_all_tables2():
    try:
        sql = """CREATE TABLE IF NOT EXISTS admin (
                     admin_id INTEGER PRIMARY KEY,
                     password TEXT NOT NULL
                 )"""
        cur.execute(sql)
        con.commit()

        # Insert default admin
        hashed_password = hash_password('helloadmin')
        sql = "INSERT OR IGNORE INTO admin (admin_id, password) VALUES (?, ?)"
        cur.execute(sql, (227, hashed_password))
        con.commit()
        print("Admin table created and default admin added.")
    except sqlite3.DatabaseError as e:
        print(f"Error creating admin table: {e}")

def make_all_tables3():
    try:
        sql = """CREATE TABLE IF NOT EXISTS issue_history (
                     book_id TEXT NOT NULL,
                     customer_id INTEGER NOT NULL,
                     status TEXT CHECK (status IN ('Issued', 'Returned')),
                     FOREIGN KEY (book_id) REFERENCES book (book_id),
                     FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
                 )"""
        cur.execute(sql)
        con.commit()
        print("Issue history table created successfully.")
    except sqlite3.DatabaseError as e:
        print(f"Error creating issue history table: {e}")

# Call the table creation functions
make_all_tables()
make_all_tables1()
make_all_tables2()
make_all_tables3()

# Sign-up function for customers
def sign_up_customer(customer):
    try:
        fname = customer.get_first_name()
        lname = customer.get_last_name()
        address = customer.get_address()
        password = customer.get_password()
        
        # Hash the password
        

        # Insert the customer data into the table
        sql = """INSERT INTO customers (first_name, last_name, address, password)
                 VALUES (?, ?, ?, ?)"""
        cur.execute(sql, (fname, lname, address, password))
        con.commit()
        
        # Get the generated customer ID
        c_id = cur.lastrowid
        
        print("Congratulations! Your account was created successfully.")
        print(f"Your Customer ID: {c_id}")
    except sqlite3.DatabaseError as e:
        print(f"Error during customer sign up: {e}")

# Example Usage
class Customer:
    def __init__(self, first_name, last_name, address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.password = password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

    def get_password(self):
        return self.password
    

import sqlite3
from hashlib import sha256

def get_db_connection():
    """
    Connect to the SQLite database and return the connection object.
    """
    return sqlite3.connect('library.db')

def hash_password(password):
    """
    Hash a password using SHA256.
    """
    return sha256(password.encode('utf-8')).hexdigest()

# 1. All Books
def all_books():
    """
    Fetch and display all books from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    
    for book in books:
        print(f"Title: {book[0]}, Author: {book[1]}, Publisher: {book[2]}, Year: {book[3]}, Book ID: {book[4]}, Status: {book[5]}")
    
    conn.close()

# 2. Available Books
def avail_book():
    """
    Fetch and display all available books.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM book WHERE status = 'Available'")
    books = cursor.fetchall()
    
    for book in books:
        print(f"Title: {book[0]}, Author: {book[1]}, Publisher: {book[2]}, Year: {book[3]}, Book ID: {book[4]}")
    
    conn.close()

# 3. Add Book
def add_book(title, author, publisher, pub_year, book_id, status='Available'):
    """
    Add a new book to the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO book (title, author, publisher, pub_year, book_id, status) VALUES (?, ?, ?, ?, ?, ?)", 
                   (title, author, publisher, pub_year, book_id, status))
    conn.commit()
    print("Book added successfully.")
    
    conn.close()

# 4. Remove Book
def remove_book(book_id):
    """
    Remove a book from the database by its book_id.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM book WHERE book_id = ?", (book_id,))
    conn.commit()
    print(f"Book with ID {book_id} removed successfully.")
    
    conn.close()

# 5. All Customers
def all_customers():
    """
    Fetch and display all customers from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    
    for customer in customers:
        print(f"ID: {customer[0]}, Name: {customer[1]} {customer[2]}, Address: {customer[3]}, Email: {customer[4]}")
    
    conn.close()

# 6. Remove Customer
def remove_customer(customer_id):
    """
    Remove a customer from the database by their customer_id.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
    conn.commit()
    print(f"Customer with ID {customer_id} removed successfully.")
    
    conn.close()

# 7. Check Issue History
def check_issue_history():
    """
    Fetch and display all issue histories.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT book_id, customer_id, status FROM issue_history
    """)
    history = cursor.fetchall()
    
    for record in history:
        print(f"Book ID: {record[0]}, Customer ID: {record[1]}, Status: {record[2]}")
    
    conn.close()


def login_customer(customer_id, input_hashed_password):
    """Logs in a customer by comparing the hashed input password with the stored password."""
    
    try:
        # Connect to the database
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        
        # Retrieve the stored password for the given customer ID
        sql = "SELECT password FROM customers WHERE customer_id = ?"
        cur.execute(sql, (customer_id,))
        result = cur.fetchone()
        
        if result:
            stored_hashed_password = result[0]
            # Debug print to compare the stored and input hashes
            print(f"Stored hashed password for customer {customer_id}: {stored_hashed_password}")
            print(f"Input hashed password: {input_hashed_password}")
            
            # Compare the input hashed password with the stored password
            if stored_hashed_password == input_hashed_password:
                return True
            else:
                print("Password mismatch")  # Debug: Indicate that the password does not match
                return False
        else:
            print("Customer not found!")  # Debug: Indicate if the customer is not found
            return False
    
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    
    finally:
        con.close()


