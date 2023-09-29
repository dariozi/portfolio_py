import streamlit as st
import send_emails
st.header("Contact Me")

with st.form(key= "my_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Write your message")
    message =f"""\
Subject: New Email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Press here")
    if button:
        send_emails.send_email(message)
        st.info("Email was sent successfully")