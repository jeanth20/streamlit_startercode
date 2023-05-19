import pickle
from pathlib import Path

import streamlit_authenticator as stauth

import sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

# names = ["Peter Parker", "Rebecca Miller"]
# usernames = ["pparker", "rmiller"]
# passwords = ["XXX", "XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)