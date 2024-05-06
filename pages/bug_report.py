import streamlit as st
import smtplib
from email.mime.text import MIMEText
from korean_menu import make_sidebar

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="random",
    layout="centered"
)
make_sidebar()

st.title('Bug report')

st.markdown("""
**if there is anything wrong while using my app plz lemme know**
""")

# Taking inputs

subject = st.text_input('Subject')
body = st.text_area('Body')

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = st.secrets.admin_email
        msg['To'] = st.secrets.user_email
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(st.secrets.admin_email, 'hzfemdpfnfczwixe')
        server.sendmail(st.secrets.admin_email, st.secrets.user_email, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")