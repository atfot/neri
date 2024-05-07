import streamlit as st
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
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
        content = MIMEText(error_body, "plain")
        msg.attach(content)
        
        # 이미지 파일 추가
        img = MIMEImage(error_image.read())
        img.add_header('Content-Disposition', 'attachment', filename=image_name)
        msg.attach(img)
        
        # 받는 메일 유효성 검사 거친 후 메일 전송
        smtp.sendmail(st.secrets.admin_email, st.secrets.bug_report_email, msg.as_string())
        
        # smtp 서버 연결 해제
        smtp.quit()
        st.success('Email sent successfully! 🚀')
        st.session_state.send_email=False
    except Exception as e:
        st.error(f"Failed to send email: {e}")
else:
    pass
