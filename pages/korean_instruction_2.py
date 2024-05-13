import streamlit as st
from korean_menu import make_sidebar
from openai import OpenAI
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from streamlit import session_state as sss
import pdfkit

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
make_sidebar()

if 'client' not in sss:
  sss.client = OpenAI(api_key=st.secrets['api_key'])

if 'username' not in sss:
   sss.username=st.secrets.user_name
   sss.age=st.secrets.age
   sss.gender=st.secrets.user_gender
   sss.problem=st.secrets.problem
   sss.problem_explanation=st.secrets.problem_explanation
   sss.goal=st.secrets.goal

html_content = """
<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
"""

# Convert HTML to PDF
pdf = pdfkit.from_string(html_content, False)

# Display PDF in Streamlit app
st.download_button(
    label="Download PDF",
    data=pdf,
    file_name="hello_world.pdf",
    mime="application/pdf",
)