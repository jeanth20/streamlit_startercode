    col1, col2 = st.columns(2)
    col1.write("")
    col2.write("")
    with col1:
        st.subheader("login Table")
        user_result = mysql.view_all_access()
        clean_db = pd.DataFrame(user_result, columns=["username", "datetime"])
        st.dataframe(clean_db)

    with col2:
        st.subheader("User Table")
        user_result = mysql.view_all_users()
        clean_db = pd.DataFrame(user_result, columns=["username", "email", "password"])
        st.dataframe(clean_db)


    col12, col22, col32 = st.columns(3)
        
    with col12:

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