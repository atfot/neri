import streamlit as st
import smtplib
from email.mime.text import MIMEText

st.title('Send Streamlit SMTP Email 💌 🚀')

st.markdown("""
**Enter your email, subject, and email body then hit send to receive an email from `summittradingcard@gmail.com`!**
""")

# Taking inputs

subject = st.text_input('Subject')
body = st.text_area('Body')

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = st.secrets.admin_email
        msg['To'] = 'chohk4198@gmail.com'
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(st.secrets.admin_email, st.secrets.admin_pw)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")