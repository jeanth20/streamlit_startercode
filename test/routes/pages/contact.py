import streamlit as st


st.title("Contact")
coll = st.columns(1)
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

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css(".streamlit/style.css")