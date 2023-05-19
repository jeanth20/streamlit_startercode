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



# st.title("Simple Login Page")
st.title("My Streamlit App")

 
def main():
    # selected1 = option_menu(
    #     menu_title=None,
    #     options=["Home", "Similar"],
    #     icons=["house", "book"],
    #     menu_icon="cast",
    #     default_index=0,
    #     orientation="horizontal"
    # )
    
    # if selected1 == "similar":
    #     import streamlit as st
    #     import streamlit.components.v1 as components

    #     html_string = '''
    #     <h1>HTML string in RED</h1>

    #     <script language="javascript">
    #     document.querySelector("h1").style.color = "red";
    #     console.log("Streamlit runs JavaScript");
    #     alert("Streamlit runs JavaScript");
    #     </script>
    #     '''

    #     components.html(html_string)
    #     st.markdown(html_string, unsafe_allow_html=True)


    with st.sidebar:
        selected = option_menu(
                menu_title=None,
                options=["Login", "Sign Up"],
                icons=["door-open-fill", "signpost"],
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
                    check = fetch_usertable(username, password)
                    log = add_datetime_table(username, timestamp)

                    st.success("Logged In as {}".format(username))

                    access = st.selectbox("Access", ["swipe", "peter"])
                    if access == "swipe":
                        st.subheader("swipe")
                    elif access == "peter":
                        st.subheader("peter")

            elif selected == "Sign Up":
                st.subheader("Create an account")
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


    col1, col2 = st.columns(2)
    col1.write("")
    col2.write("")


    with col1:
        st.subheader("login Table")
        # user_result = view_all_access()
        # clean_db = pd.DataFrame(user_result, columns=["username", "datetime"])
        # st.dataframe(clean_db)
        # import pandas as pd
        # from faker import Faker
        # import streamlit as st
        # from streamlit_extras.dataframe_explorer import dataframe_explorer

        # def generate_fake_dataframe(size, cols, col_names, seed):
        #     fake = Faker()
        #     Faker.seed(seed)

        #     data = []
        #     for _ in range(size):
        #         row = [fake.date_between(start_date='-30y', end_date='today').strftime('%Y-%m-%d') if col == 'date' else getattr(fake, col)() for col in cols]
        #         data.append(row)

        #     df = pd.DataFrame(data, columns=col_names)
        #     return df

        # dataframe = generate_fake_dataframe(
        #     size=500, cols=["d", "f", "c"], col_names=("date", "income", "person"), seed=1
        # )

        # filtered_df = dataframe_explorer(dataframe, case=False)
        # st.dataframe(filtered_df, use_container_width=True)


    with col2:
        st.subheader("User Table")
    #     user_result = view_all_users()
    #     clean_db = pd.DataFrame(user_result, columns=["username", "email", "password"])
    #     st.dataframe(clean_db)


st.markdown("""
<style>
    #MainMenu, footer, .header, .css-18ni7ap.e8zbici2 {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)    
    
if __name__ == "__main__":
    main()