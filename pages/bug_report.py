import streamlit as st
from redmail import EmailSender
from korean_menu import make_sidebar

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="random",
    layout="centered"
)
make_sidebar()

st.subheader('사용하시다 불편하신 점이 계셨나요?')

st.write("""
**저희 프로그램을 사용하시면서 오류가 나거나 맘에 안드는 점이 있으시다면 꼭 알려주세요!**
            
**문제점을 고쳐나가도록 하겠습니다🥰**
""")

# Taking inputs

error_subject = st.text_input('제목')
error_body = st.text_area('내용')
error_image=st.file_uploader('상세사진', accept_multiple_files=True)

col1,col2=st.columns([8,2])
with col2:
    if st.button("Send Email",use_container_width=True):
        if 'send_email' not in st.session_state:
            st.session_state.send_email=True
if st.session_state.send_email==True:
    try:
        email=EmailSender(host='smtp.gmail.com',port=587)
        email.send(
            subject=f'{error_subject}',
            sender=f'{st.secrets.admin_email}',
            receivers=[f'{st.secrets.bug_report_email}'],
            html=f'''
<p><b>{st.session_state.username}</b></p><br><br>
{error_body}
''',
body_images={
'my_image': f'{error_image}',
}
)


        #msg = MIMEText(body)
        #msg['From'] = st.secrets.admin_email
        #msg['To'] = st.secrets.bug_report_email
        #msg['Subject'] = subject

        #server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.starttls()
        #server.login(st.secrets.admin_email, 'hzfemdpfnfczwixe')
        #server.sendmail(st.secrets.admin_email, st.#secrets.bug_report_email, msg.as_string())
        #server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")
else:
    pass