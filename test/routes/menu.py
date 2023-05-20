import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

from routes import mysql, menu, extras

def sidebar_menu():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", "Users", "Support", "Settings", "Sign Out"], 
            icons=["house", "person-vcard", "patch-question", "gear", "door-closed-fill"], menu_icon="cast", default_index=1)
        selected

    if selected == "Users":
        users_tab_menu()

    if selected == "Support":
        support()

    if selected == "Logout":
        users_tab_menu()

def users_tab_menu():
    selecteduser = option_menu(None, ["Add", "Remove", "View All", 'View Activity'], 
        icons=['person-fill-add', 'person-fill-x', "person-rolodex", 'card-list'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    selecteduser

    if selecteduser == "Add":
        st.subheader("Create an account")
        username = st.text_input("Username")
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

        if st.button("Sign Up"):
            if username == None or email == None or password == None:
                st.warning("Sign Up Error")
            else:
                result = mysql.add_usertable(username, email, password)
                hashed = mysql.hash_password(password)
                st.info("Credentials Username:{} Password:{}".format(username, hashed))
                st.info("User has been created, and will be able to sign in.")
                
    if selecteduser == "Remove":
        st.subheader("Remove an account")
        usernames = mysql.all_usernames()
        username = st.selectbox("Select a username", usernames)

        if st.button("Remove"):
            if username == None:
                st.warning("Remove Error")
            else:
                result = mysql.remove_usertable(username)
                st.info("User has been removed, and will not be able to sign in.")

    if selecteduser == "View All":
        st.subheader("View All User Accounts")
        st.subheader("User Table")
        user_result = mysql.view_all_users()
        clean_db = pd.DataFrame(user_result, columns=["username", "name", "email", "password"])
        st.dataframe(clean_db)

    if selecteduser == "View Activity":
        st.subheader("View All User Accounts Activity")
        st.subheader("login Table")
        user_result = mysql.view_all_access()
        clean_db = pd.DataFrame(user_result, columns=["username", "datetime"])
        st.dataframe(clean_db)

def support():
    st.subheader("Create an account")
    contact_form = """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://bootstrapcreative.com/wp-bc/wp-content/themes/wp-bootstrap/codepen/bootstrapcreative.js?v=8"></script>
    <div class="col-sm-12 form-column">
        <form action="https://formsubmit.co/jeantheron2018@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_subject" value="New submission!">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_blacklist" value="spammy pattern, banned term, phrase">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" name="name" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" name="email" class="form-control" required >
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea name="message" class="form-control"></textarea>
            </div>
            <button type="submit">Send</button>
        </form>
    </div>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    # Load custom stylesheet
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("./.streamlit/style.css")



# add remove view 
#  Tab Menu must copy and customize for each sidebar menu
# def tab_menu():
#     selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#         icons=['house', 'cloud-upload', "list-task", 'gear'], 
#         menu_icon="cast", default_index=0, orientation="horizontal")
#     selected2
    
    