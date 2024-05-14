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
try:
    del sss.fix_info, sss.auth_email
except:
    pass
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

error_subject = st.text_input('어떤 오류가 나셨나요?')
error_body = st.text_area('자세한 설명을 해주세요!')
error_images=st.file_uploader('혹시 사진을 찍어두신게 있으시다면 보여주세요!', accept_multiple_files=True)

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
        st.success('오류 보고가 전송되었습니다! 더 나은 서비스로 보답하겠습니다🥰')
    except Exception as e:
        st.error(f"Failed to send email: {e}")
else:
    pass
