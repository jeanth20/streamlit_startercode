import streamlit as st
from streamlit_lottie import st_lottie
import streamlit_authenticator as stauth
import sqlite3
import bcrypt
import json

# Step 1: Connect to the database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Step 2: Retrieve credentials from the database
cursor.execute("SELECT username, password, name FROM userstable")
credentials = {row[0].lower(): {'password': row[1], 'name': row[2]} for row in cursor.fetchall()}

# Step 3: Hash the passwords in the credentials dictionary
for user in credentials.values():
    password = user['password'].encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    user['password'] = hashed_password.decode('utf-8')

# Step 4: Create the authenticator object
authenticator = stauth.Authenticate(
    {'usernames': credentials},  # Provide the credentials dictionary with 'usernames' key
    'cookie_name',               # Provide the cookie name
    'cookie_key',                # Provide the cookie key
    30,                          # Provide the expiry_days
    []                           # Provide an empty preauthorized list
)

# Step 5: Render the login widget
name, authentication_status, username = authenticator.login('Login', 'sidebar')

# Step 6: Handle authentication status and display appropriate messages
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.sidebar.warning('Please enter your username and password')

# Step 7: Close the database connection
conn.close()

# from dir
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("animations/arrow-doodle.json")
st_lottie(lottie_coding,
          key="hello",
          quality="low",
          height=300,
          width=400,
          )