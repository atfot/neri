import streamlit as st
import smtplib
from email.mime.text import MIMEText

st.title('Send Streamlit SMTP Email 💌 🚀')

st.markdown("""
**Enter your email, subject, and email body then hit send to receive an email from `summittradingcard@gmail.com`!**
""")

# Taking inputs
email_sender = st.text_input('From', 'chohk4198@gmail.com', disabled=True)
email_receiver = st.text_input('To', st.secrets.admin_email, disabled=True)
subject = st.text_input('Subject')
body = st.text_area('Body')

# Hide the password input
password = st.text_input('Password', type="password", disabled=True)  

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(st.secrets.admin_email, st.secrets.admin_pw)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")