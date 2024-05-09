import streamlit as st
from korean_menu import make_sidebar
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
make_sidebar()

if st.button('try'):
    # PDF 생성
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    pdf_bytes = pdf.output(dest='S').encode('latin1')

    # 이메일 보내기
    from_address = 'nerichatbot@gmail.com'
    to_address = 'nerierror@naver.com'
    subject = "PDF 파일 보내기"
    body = "PDF 파일을 첨부합니다."

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    attachment = MIMEBase('application', 'pdf', filename='tuto1.pdf')
    attachment.set_payload(pdf_bytes)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename='tuto1.pdf')
    msg.attach(attachment)

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(from_address, 'hzfemdpfnfczwixe')
    smtp_server.sendmail(from_address, to_address, msg.as_string())
    smtp_server.quit()