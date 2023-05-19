import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import datetime as d



date = d.now()

timestamp = date.strftime("%Y-%m-%d %H:%M:%S")

# https://icons.getbootstrap.com/
# python -m pip install --upgrade streamlit-extras
# pip install streamlit-option-menu
# pip install extra-streamlit-components
# https://docs.streamlit.io/library/cheatsheet
# https://docs.streamlit.io/library/api-reference#tags

# use sqlite
import sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, email TEXT, password TEXT)')

def create_usertrackertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstrackertable(username TEXT, datetime TEXT)')

create_usertable()
create_usertrackertable()

def add_usertable(username, email, password):
    c.execute('INSERT INTO userstable(username, email, password) VALUES (?,?,?)', (username, email, password))
    conn.commit()

def add_datetime_table(username, datetime):
    c.execute('INSERT INTO usertrackerstable(username, datetime) VALUES (?,?)', (username, datetime))
    conn.commit()

def fetch_usertable(username, password):
    c.execute('SELECT * FROM userstable WHERE username=? AND password=?', (username, password))
    data = c.fetchall()
    return data

def view_all_access():
    c.execute('SELECT * FROM userstrackertable')
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


st.title("My Streamlit App")
 
def main():
    with st.sidebar:
        selected = option_menu(
                menu_title=None,
                options=["Login", "Sign Up", "Logout"],
                icons=["door-open-fill", "signpost", "door-closed-fill"],
                menu_icon="cast",
                default_index=0,
            )

        if selected == "Login":
            st.subheader("Login")
            username = st.sidebar.text_input("Username")
            password = st.sidebar.text_input("Password", type="password")
                
            if st.sidebar.button("Login"):
                if username is None:
                    st.warning("Login Error")
                else:
                    timestamp = date.strftime("%Y-%m-%d %H:%M:%S")
                    check = fetch_usertable(username, password)
                    log = add_datetime_table(username, timestamp)

                    st.success("Logged In as {}".format(username))

        elif selected == "Sign Up":
            st.sidebar.subheader("Create an account")
            username = st.sidebar.text_input("Username")
            email = st.sidebar.text_input("Email Address")
            password = st.sidebar.text_input("Password", type="password")
                
            if st.sidebar.button("Sign Up"):
                if username == None or email == None or password == None:
                    st.warning("Sign Up Error")
                else:
                    result = add_usertable(username, email, password)
                        
                    st.info("You have been Signed up, please proceed to login page")
                    st.success("Welcome {}".format(username))

        elif selected == "Logout":
            st.info("Logout")
            st.success("Bye")



    col1, col2 = st.columns(2)
    col1.write("")
    col2.write("")
    with col1:
        st.subheader("login Table")
        user_result = view_all_access()
        clean_db = pd.DataFrame(user_result, columns=["username", "datetime"])
        st.dataframe(clean_db)

    with col2:
        st.subheader("User Table")
        user_result = view_all_users()
        clean_db = pd.DataFrame(user_result, columns=["username", "email", "password"])
        st.dataframe(clean_db)


st.markdown("""
<style>
    #MainMenu, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)    
    
if __name__ == "__main__":
    main()