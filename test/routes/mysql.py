import hashlib
import sqlite3
import threading
import streamlit_authenticator as auth
import streamlit as st
from datetime import datetime, timedelta

# We can also make use of an online db
# go to http://www.detacloud.com/
# setup online db

def hash_password(password):
    # Hash the password using a suitable algorithm (e.g., SHA-256)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
    
# Create a thread-local storage for the SQLite connection
thread_local = threading.local()

def get_connection():
    if not hasattr(thread_local, 'connection') or thread_local.connection is None:
        thread_local.connection = sqlite3.connect('data.db')
    
    return thread_local.connection

def create_usertable():
    conn = get_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, name TEXT, email TEXT, password TEXT)')

def add_usertable(username, email, password):
    conn = get_connection()
    c = conn.cursor()
    password_hashed = hash_password(password)
    c.execute('INSERT INTO userstable (username, name, email, password) VALUES (?, ?, ?, ?)', (username, username, email, password_hashed))
    conn.commit()

def remove_usertable(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute('DELETE FROM userstable WHERE username=?', (username))
    conn.commit()

def create_usertrackertable():
    conn = get_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstrackertable(username TEXT, datetime TEXT)')

def add_datetime_table(username, datetime):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO userstrackertable(username, datetime) VALUES (?,?)', (username, datetime))
    conn.commit()

def fetch_usertable(username, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username=? AND password=?', (username, password))
    data = c.fetchall()
    return data

def view_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def view_all_access():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM userstrackertable')
    data = c.fetchall()
    return data

def all_usernames():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT username FROM userstable')
    data = c.fetchall()
    return data

create_usertable()
create_usertrackertable()

