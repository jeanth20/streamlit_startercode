import streamlit as st
from streamlit_lottie import st_lottie
import streamlit_authenticator as stauth
import sqlite3
import bcrypt
import json
from routes import mysql, menu, extras
from datetime import datetime as d



date = d.now()
timestamp = date.strftime("%Y-%m-%d %H:%M:%S")

conn = mysql.get_connection()
cursor = conn.cursor()

cursor.execute("SELECT username, password, name FROM userstable")
credentials = {row[0].lower(): {'password': row[1], 'name': row[2]} for row in cursor.fetchall()}

print(credentials)

for user in credentials.values():
    password = user['password'].encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    user['password'] = hashed_password.decode('utf-8')

authenticator = stauth.Authenticate(
    {'usernames': credentials},
    'cookie_name',
    'cookie_key',
    60,
    []
)

def login_widget():
    
    name, authentication_status, username = authenticator.login('Login', 'sidebar')

    if username == None:
        st.sidebar.info("Please enter your Username and Password")

    if username == False:
        st.sidebar.info("Please enter your Username and Password")

    if authentication_status == False:
        st.session_state.authentication_status = False
        st.sidebar.error("Username or Password is incorrect")
        
    if authentication_status == None:
        st.sidebar.info("Please enter your Username and Password")
        # extras.login_animation()
    # if st.session_state.authentication_status is None:
    #     st.sidebar.error('Session state error')

    if authentication_status:
        is_user_logged_in()
        menu.sidebar_menu()
        st.balloons()
        # st.sidebar.success('Successful Sign In')
        return

    # mysql.get_connection().close()
    

def is_user_logged_in():
    if "username" in st.session_state and "login_time" in st.session_state and "expiration_time" in st.session_state:
        current_time = d.datetime.now()
        expiration_time = st.session_state["expiration_time"]
        if current_time <= expiration_time:
            return True
    return False