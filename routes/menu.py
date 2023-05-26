import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import os

from streamlit_login_auth_ui import widgets, utils
# from routes import menu, accounts, extras

def sidebar_menu(username, session):
    with st.sidebar:
        selected = option_menu(
            menu_title=username,
            options=["Home"], 
            icons=["house"],
            menu_icon="person-circle",
            default_index=0
        )
        selected


    if selected == "Home":
        tab_menu()
        st.title(":house:")


# add remove view 
#  Tab Menu must copy and customize for each sidebar menu
def tab_menu():
    selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    selected2
