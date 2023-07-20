import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from routes import menu

st.set_page_config(page_title="Umbrella", page_icon="☂️", layout="wide")

st.markdown("""
    <style>
    #MainMenu, footer, .header, .css-18ni7ap.e8zbici2 {
        visibility: hidden;
    }

    .css-1je5a9p.e1tzin5v2, .css-5rimss.e16nr0p34 {
        display: none;
    }
        
    .stAlert {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)


__login__obj = __login__(auth_token = "courier_auth_token",
                    company_name = "Panda",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_dn6rwtwl.json')

LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

if LOGGED_IN == True:

   # st.markdown(st.session_state)
   # st.write(username)
   
   menu.sidebar_menu(username, st.session_state)
   st.title(":house:")
