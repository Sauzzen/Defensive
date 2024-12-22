__author__ = 'user'
from abc import ABC, abstractmethod
import sqlite3
class Customer:
    def __init__(self, first_name=None, last_name=None, customer_id=None, password=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.password = password
        self.address = address

    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_password(self, password):
        self.password = password

    def set_address(self, address):
        self.address = address

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_customer_id(self):
        return self.customer_id

    def get_password(self):
        return self.password

    def get_address(self):
        return self.address


class Book:
    def __init__(self, title=None, author=None, publication=None, pub_year=None, book_id=None, status=None):
        self.title = title
        self.author = author
        self.publication = publication
        self.pub_year = pub_year
        self.book_id = book_id
        self.status = status

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_publish(self, publication):
        self.publication = publication

    def set_pub_year(self, pub_year):
        self.pub_year = pub_year

    def set_b_id(self, book_id):
        self.book_id = book_id

    def set_status(self, status):
        self.status = status

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publish(self):
        return self.publication

    def get_pub_year(self):
        return self.pub_year

    def get_b_id(self):
        return self.book_id

    def get_status(self):
        return self.status
