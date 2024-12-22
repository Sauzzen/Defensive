__author__ = 'user'
import sqlite3
import re
import database
from classes import Customer, Book
import login_menu
import admin_menu
import hashlib
import database_admin as db_admin
import logging

# Basic setup for a logger
logging.basicConfig(
    filename='app.log',  # Logs will be written to this file
    level=logging.ERROR,  # Set the minimum level of messages to log
    format='%(asctime)s - %(levelname)s - %(message)s'  # How the log message should be formatted
)
logger = logging.getLogger(__name__)
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_password(password):
    return 8 <= len(password) <= 20 


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def sign_up():
    customer = Customer()
    
    # Get customer details
    first_name = input("Enter First Name\n")
    last_name = input("Enter Last Name\n")
    
    while True:
        address = input("Enter Email Address\n")
        if is_valid_email(address):
            break
        print("Invalid email format. Please enter a valid email (e.g., user@example.com)")
    
    while True:
        password = input("Enter Password\n")
        if is_valid_password(password):
            break
        print("Password must be between 8 and 20 characters")

    # Hash the password
    hashed_password = hash_password(password)
    
    # Debug: Print the hashed password
    print(f"Hashed password for sign-up: {hashed_password}")
    
    # Set customer details
    customer.set_first_name(first_name)
    customer.set_last_name(last_name)
    customer.set_password(hashed_password)
    customer.set_address(address)
    
    # Insert customer data into database
    database.sign_up_customer(customer)


def sign_in():
    try:
        # Step 1: Get the Customer ID
        customer_id = int(input("Enter Customer ID\n"))
        
        # Step 2: Get and hash the input password
        password = input("Enter Password: ").strip()
        hashed_password = hash_password(password)
    
        # Debug: Print the input hash to verify it's correct
        print(f"Attempting to log in with Customer ID: {customer_id}")
        print(f"Input hashed password: {hashed_password}")
        
        # Step 3: Call login_customer to check if the credentials are valid
        is_valid = database.login_customer(customer_id, hashed_password)

        # Debug: Output what happened with the login attempt
        if is_valid:
            print("Login successful")
            customer_menu(customer_id)  # Assuming customer_menu() is defined elsewhere
            return True
        else:
            print("Invalid credentials")
            return False
            
    except ValueError:
        print("Invalid Customer ID format. Please enter a valid number.")
        return False
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


    
def customer_menu(customer_id):
    ch = 1
    while ch != 0:
        print("\n--- Menu ---")
        print("1. Available Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Issued Books")
        print("5. Change Password")
        print("0. Logout")

        try:
            ch = int(input())
        except ValueError:
            print("Invalid Choice")
            ch = 1
            continue

        if ch == 1:
            database.avail_book()
        elif ch == 2:
            database.issue_book(customer_id)
        elif ch == 3:
            database.return_book(customer_id)
        elif ch == 4:
            database.issued_books(customer_id)
        elif ch == 5:
            login_menu.change_password(customer_id)
        elif ch == 0:
            print("Logged Out Successfully")
        else:
            print("Invalid Choice")

def admin_sign_in():
    try:
        admin_id = input("\nEnter Admin ID: ")
    except:
        print("Invalid ID")
        return

    password = input("\nEnter Password: ")
    res = database.login_admin(admin_id, password)  # This will hash the password inside login_admin()

    attempt_count = 3  # Allow 3 attempts for login
    while res == False and attempt_count > 0:
        print(f"Wrong ID or Password. Attempts remaining: {attempt_count}")
        try:
            admin_id = input("Enter Admin ID\n")
        except:
            print("Invalid ID")
            return

        password = input("Enter Password\n")
        res = database.login_admin(admin_id, password)  # Recheck after new inputs
        attempt_count -= 1

    if res == True:
        print("Login Successful")
        ch = 1
        while ch != 0:
            print("\n --- Admin Menu --- ")
            print("1. All Books")
            print("2. Available Books")
            print("3. Add Book")
            print("4. Remove Book")
            print("5. All Customers")
            print("6. Remove Customer")
            print("7. Check Issue History")
            print("0. Admin Log Out")

            try:
                ch = int(input("Enter your choice: "))
            except:
                print("Invalid Choice")
                ch = 1
                continue

            # Admin menu actions
            if ch == 1:
                database.all_books()
            elif ch == 2:
                database.avail_book()
            elif ch == 3:
                admin_menu.add_book()
            elif ch == 4:
                admin_menu.remove_book()
            elif ch == 5:
                admin_menu.all_customers()
            elif ch == 6:
                admin_menu.remove_customer()
            elif ch == 7:
                admin_menu.check_history()
            elif ch == 0:
                print("Logged Out Successfully")
            else:
                print("Invalid Choice")

    else:
        print("Sorry, all attempts finished.")



