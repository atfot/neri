import streamlit as st
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
from english_menu import make_sidebar

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="random",
    layout="centered"
)
try:
    del sss.fix_info, sss.auth_email
except:
    pass
make_sidebar()
if 'send_email' not in st.session_state:
    st.session_state.send_email=False
if 'username' not in st.session_state:
    st.session_state.username=st.secrets.user_name

st.subheader('Have you experienced any inconveniences while using it?')

st.write("""
**If you find any errors or don't like something about our program, please let us know!**
            
**I'll try to fix it🥰**
""")

# Taking inputs

error_subject = st.text_input('What error did you get?')
error_body = st.text_area('Please provide a detailed explanation!')
error_images=st.file_uploader('If you have any pictures, show them to me!', accept_multiple_files=True)

col1,col2=st.columns([9,1])
with col2:
    if st.button("📧",use_container_width=True):
        st.session_state.send_email=True
if st.session_state.send_email==True:
    try:
        # smpt 서버와 연결
        gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
        gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
        smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
        
        # 로그인
        smtp.login(st.secrets.admin_email, st.secrets.admin_pw)
        
        # 메일 기본 정보 설정
        msg = MIMEMultipart()
        msg["Subject"] = error_subject
        msg["From"] = st.secrets.admin_email
        msg["To"] = st.secrets.bug_report_email
        
        # 메일 본문 내용
        email_body=f'{st.session_state.username}'+'\n'+error_body
        content = MIMEText(email_body, "plain")
        msg.attach(content)
        
        # 이미지 파일 추가
        if error_images is not None:
            for image in error_images:
                img = MIMEImage(image.read())
                img.add_header('Content-Disposition', 'attachment', filename=image.name)
                msg.attach(img)
        else:
            pass
        
        # 받는 메일 유효성 검사 거친 후 메일 전송
        smtp.sendmail(st.secrets.admin_email, st.secrets.bug_report_email, msg.as_string())
        
        # smtp 서버 연결 해제
        smtp.quit()
        st.session_state.send_email=False
        st.success('Your error report has been sent! I will make it better to please you🥰')
    except Exception as e:
        st.error(f"Failed to send email: {e}")
else:
    pass
