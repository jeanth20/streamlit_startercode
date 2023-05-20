import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from datetime import datetime, timedelta
import pandas as pd
import bcrypt
import requests
import os


# User Modules
from routes import mysql, login, menu, extras

# Global Var
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv(".env")

# DETA_KEY = os.getenv("DETA_KEY")
  
def main():
    login.login_widget()

if __name__ == "__main__":
    main()
    
    # st.markdown("""
    # <style>
    #     #MainMenu, footer, .header, .css-18ni7ap.e8zbici2 {
    #     visibility: hidden;
    # }
    # </style>
    # """, unsafe_allow_html=True)