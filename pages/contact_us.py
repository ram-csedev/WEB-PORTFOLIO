import streamlit as st
import sending_email

st.header('CONTACT US')
with st.form(key='email_forms'):
    email = st.text_input('Your Email address')
    raw_message=st.text_area('Enter your message')
    button = st.form_submit_button('Submit')
    message= f"""\
Subject: New email from {email}

From: {email}

{raw_message}
"""
    if button:
        sending_email.send_email(message)
        st.info('Email sent successfully')