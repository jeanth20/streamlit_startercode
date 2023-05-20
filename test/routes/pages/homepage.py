import streamlit as st


st.title("Home")


    # with st.sidebar:
    #     selected = option_menu(
    #             menu_title=None,
    #             options=["Sign In", "Sign Out", "Sign Up", "Support"],
    #             icons=["door-open-fill", "door-closed-fill", "signpost", "person-lines-fill"],
    #             menu_icon="cast",
    #             default_index=0,
    #         )

    #     if selected == "Sign In":
    #         st.subheader("Sign In")
            
    #         extras.login_animation()

    #         if st.sidebar.button("Sign In"):
    #             if username is None:
    #                 st.warning("Login Error")
    #             else:
    #                 timestamp = date.strftime("%Y-%m-%d %H:%M:%S")
    #                 check = mysql.fetch_usertable(username, password)
    #                 log = mysql.add_datetime_table(username, timestamp)

    #                 st.sidebar.success("Login Tracker fired: {}".format(timestamp))
    #                 st.sidebar.success("Logged In as {}".format(username))

    #     elif selected == "Sign Up":
    #         st.sidebar.subheader("Create an account")
    #         username = st.sidebar.text_input("Username")
    #         email = st.sidebar.text_input("Email Address")
    #         password = st.sidebar.text_input("Password", type="password")
            
    #         if st.sidebar.button("Sign Up"):
    #             if username == None or email == None or password == None:
    #                 st.warning("Sign Up Error")
    #             else:
    #                 result = mysql.add_usertable(username, email, password)
                    
    #                 st.info("You have been Signed up, please proceed to login page")
    #                 st.success("Welcome {}".format(username))
    #                 st.balloons()

    #     elif selected == "Sign Out":
    #         login = login.authenticator.logout('Logout', 'sidebar')
            
    #         if login == True:
    #             st.error("Sign Out")
    #             st.success("Bye")
            
    #     elif selected == "Support":
    #         st.header("")
    #         coll = st.columns(1)
    #         contact_form = """
    #         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    #         <script src="https://bootstrapcreative.com/wp-bc/wp-content/themes/wp-bootstrap/codepen/bootstrapcreative.js?v=8"></script>
    #         <div class="col-sm-12 form-column">
    #             <form action="https://formsubmit.co/jeantheron2018@gmail.com" method="POST">
    #                 <input type="hidden" name="_captcha" value="false">
    #                 <input type="hidden" name="_subject" value="New submission!">
    #                 <input type="hidden" name="_template" value="table">
    #                 <input type="hidden" name="_blacklist" value="spammy pattern, banned term, phrase">
    #                 <div class="form-group">
    #                     <label for="email">Your Email</label>
    #                     <input type="email" id="email" name="email" class="form-control">
    #                 </div>
    #                 <div class="form-group">
    #                     <label for="name">Name</label>
    #                     <input type="text" name="name" class="form-control" required>
    #                 </div>
    #                 <div class="form-group">
    #                     <label for="email">Email</label>
    #                     <input type="email" name="email" class="form-control" required >
    #                 </div>
    #                 <div class="form-group">
    #                     <label for="message">Message</label>
    #                     <textarea name="message" class="form-control"></textarea>
    #                 </div>            
    #                 <button type="submit">Send</button>
    #             </form>
    #         </div>
    #         """
    #         st.markdown(contact_form, unsafe_allow_html=True)     

    #     def local_css(file_name):
    #         with open(file_name) as f:
    #             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    #     local_css(".streamlit/style.css")





# # Function to set the login cookie and expiration time
# def set_login_cookie(username):
#     # Set the login time and expiration time
#     login_time = datetime.now()
#     expiration_time = login_time + timedelta(minutes=30)
#     # Store the login information in the session state
#     st.session_state["username"] = username
#     st.session_state["login_time"] = login_time
#     st.session_state["expiration_time"] = expiration_time

# # Function to check if the user is logged in and if the cookie has expired
# def is_user_logged_in():
#     if "username" in st.session_state and "login_time" in st.session_state and "expiration_time" in st.session_state:
#         current_time = datetime.now()
#         expiration_time = st.session_state["expiration_time"]
#         if current_time <= expiration_time:
#             return True
#     return False

# def logout():
#     st.session_state.clear()
#     st.experimental_rerun()








    # col1, col2 = st.columns(2)
    # col1.write("")
    # col2.write("")
    # with col1:
    #     st.subheader("login Table")
    #     user_result = mysql.view_all_access()
    #     clean_db = pd.DataFrame(user_result, columns=["username", "datetime"])
    #     st.dataframe(clean_db)

    # with col2:
    #     st.subheader("User Table")
    #     user_result = mysql.view_all_users()
    #     clean_db = pd.DataFrame(user_result, columns=["username", "email", "password"])
    #     st.dataframe(clean_db)


    # col12, col22, col32 = st.columns(3)
        
    # with col12:

    # import time
    # with col22:
    #     with st.spinner(text='In progress'):
    #         time.sleep(5)
    #         st.success('Done')
    
        # st.progress(progress_variable_1_to_100)

    # with col12:
    #     st.balloons()

    # with col32:
        # st.write("mothing here")
        # # Show different content based on the user's email address.
        # if st.user.email == 'jane@email.com':
        #     display_jane_content()
        # elif st.user.email == 'adam@foocorp.io':
        #     display_adam_content()
        # else:
        #     st.write("Please contact us to get access!")

        # st.error('')
        # st.warning('Warning message')
        # st.info('Info message')
        # st.success('Success message')
        # st.exception(e)