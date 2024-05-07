import streamlit as st
import smtplib
from email.message import EmailMessage
import imghdr
from korean_menu import make_sidebar

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="random",
    layout="centered"
)
make_sidebar()
if 'send_email' not in st.session_state:
    st.session_state.send_email=False
if 'username' not in st.session_state:
    st.session_state.username=st.secrets.user_name

st.subheader('사용하시다 불편하신 점이 계셨나요?')

st.write("""
**저희 프로그램을 사용하시면서 오류가 나거나 맘에 안드는 점이 있으시다면 꼭 알려주세요!**
            
**문제점을 고쳐나가도록 하겠습니다🥰**
""")

# Taking inputs

error_subject = st.text_input('제목')
error_body = st.text_area('내용')
error_image=st.file_uploader('상세사진')

col1,col2=st.columns([8,2])
with col2:
    if st.button("Send Email",use_container_width=True):
        st.session_state.send_email=True
if st.session_state.send_email==True:
    try:
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 465
        
        message = EmailMessage()
        message.set_content(error_body)

        message["Subject"] = error_subject
        message["From"] = st.secrets.admin_email
        message["To"] = st.secrets.bug_report_email

        if error_image is not None:
            image_file = error_image.read()
            image_type = imghdr.what('chatbot_pc_home_english_3',image_file)
            message.add_attachment(image_file,maintype='image',subtype=image_type)

        smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
        smtp.login(st.secrets.admin_email,st.secrets.admin_pw)
        smtp.send_message(message)
        smtp.quit()

        st.success('Email sent successfully! 🚀')
        st.session_state.send_email=False
    except Exception as e:
        st.error(f"Failed to send email: {e}")
else:
    pass
