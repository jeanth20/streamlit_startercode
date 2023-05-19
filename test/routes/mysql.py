import sqlite3
import threading

# Create a thread-local storage for the SQLite connection
thread_local = threading.local()

def get_connection():
    if not hasattr(thread_local, 'connection') or thread_local.connection is None:
        thread_local.connection = sqlite3.connect('data.db')
    
    return thread_local.connection

def create_usertable():
    conn = get_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, email TEXT, password TEXT)')

def add_usertable(username, email, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username, email, password) VALUES (?,?,?)', (username, email, password))
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

create_usertable()
create_usertrackertable()

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