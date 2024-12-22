__author__ = 'user'
import sqlite3
import database
from classes import Customer, Book
import database_admin as db_admin

def change_password(customer_id):
    new_password = input("ENTER NEW PASSWORD: ")
    database.change_password(customer_id, new_password)
