import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from datetime import datetime as d
import pandas as pd
import requests
import json

# User Modules
from routes import mysql

date = d.now()

timestamp = date.strftime("%Y-%m-%d %H:%M:%S")

# https://icons.getbootstrap.com/
# python -m pip install --upgrade streamlit-extras
# pip install streamlit-option-menu
# pip install extra-streamlit-components/test/requirements.txt
# https://docs.streamlit.io/library/cheatsheet
# https://docs.streamlit.io/library/api-reference#tags

st.title("Welcome Please Sign In")

def main():
    # from dir
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    lottie_coding = load_lottiefile("animations/arrow-doodle.json")  # replace link to local lottie file
    st_lottie(lottie_coding,
              key="hello",
              quality="low",
              height=300,
              width=400,
              )
        
    # # from site
    # def load_lottieurl(url: str):
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return None
    #     return r.json()
        
    # lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_Pr3rKjXraf.json")

    # st_lottie(
    #     lottie_hello,
    #     speed=1,
    #     reverse=False,
    #     loop=True,
    #     quality="low", # medium ; high
    #     #renderer="svg", # canvas
    #     height=None,
    #     width=None,
    #     key=None,
    # )
    with st.sidebar:
        selected = option_menu(
                menu_title=None,
                options=["Sign In", "Sign Out", "Sign Up", "Support"],
                icons=["door-open-fill", "door-closed-fill", "signpost", "person-lines-fill"],
                menu_icon="cast",
                default_index=0,
            )

        if selected == "Sign In":
            st.subheader("Sign In")
            username = st.sidebar.text_input("Username")
            password = st.sidebar.text_input("Password", type="password")
                
            if st.sidebar.button("Sign In"):
                if username is None:
                    st.warning("Login Error")
                else:
                    timestamp = date.strftime("%Y-%m-%d %H:%M:%S")
                    check = mysql.fetch_usertable(username, password)
                    log = mysql.add_datetime_table(username, timestamp)

                    st.sidebar.success("Login Tracker fired: {}".format(timestamp))
                    st.sidebar.success("Logged In as {}".format(username))

        elif selected == "Sign Up":
            st.sidebar.subheader("Create an account")
            username = st.sidebar.text_input("Username")
            email = st.sidebar.text_input("Email Address")
            password = st.sidebar.text_input("Password", type="password")
            
            if st.sidebar.button("Sign Up"):
                if username == None or email == None or password == None:
                    st.warning("Sign Up Error")
                else:
                    result = mysql.add_usertable(username, email, password)
                    
                    st.info("You have been Signed up, please proceed to login page")
                    st.success("Welcome {}".format(username))
                    st.balloons()

        elif selected == "Sign Out":
            # import streamlit as st
            # import streamlit.components.v1 as components
            # html_string = '''
            # <h1>HTML string in RED</h1>
            # <script language="javascript">
            # document.querySelector("h1").style.color = "red";
            # console.log("Streamlit runs JavaScript");
            # alert("Streamlit runs JavaScript");
            # </script>
            # '''
            # components.html(html_string)
            # st.markdown(html_string, unsafe_allow_html=True)            
            st.info("Sign Out")
            # st.success("Bye")
            
        elif selected == "Support":
            st.header("")
            coll = st.columns(1)
            # https://formsubmit.co/
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
                        <label for="email">Your Email</label>
                        <input type="email" id="email" name="email" class="form-control">
                    </div>
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
        local_css(".streamlit/style.css")




    
    

    
if __name__ == "__main__":    
    main()
  



