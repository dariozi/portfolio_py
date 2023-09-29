import streamlit as st

st.header("Contact Me")

with st.form(key= "my_form"):
    user_email = st.text_input("Your email address")
    email_body = st.text_area("Write your message")
    button = st.form_submit_button("Press here")
    if button:
        print("button was pressed")