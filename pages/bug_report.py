import streamlit as st
from redmail import gmail
import smtplib
from email.mime.text import MIMEText
from korean_menu import make_sidebar
import base64

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
for uploaded_file in error_image:
    bytes_data = uploaded_file.read()
    subtype_name=uploaded_file[uploaded_file.find('.')+1:]
    st.write(subtype_name)

col1,col2=st.columns([8,2])
with col2:
    if st.button("Send Email",use_container_width=True):
        if 'send_email' not in st.session_state:
            st.session_state.send_email=True
if st.session_state.send_email==True:
    try:
        img_list={
            'myimage':[],
            'subtype':[]
            }
        for uploaded_file in error_image:
            base64_str = base64.b64encode(error_image.read())
            imgdata = base64.b64decode(base64_str)
            img_list['myimage'] = imgdata
            subtype_name=uploaded_file[uploaded_file.find('.')+1:]
            img_list['subtype'] = subtype_name            
        gmail.username=st.secrets.admin_email
        gmail.password=st.secrets.admin_pw
        gmail.send(
            subject=f'{error_subject}',
            sender=f'{st.secrets.admin_email}',
            receivers=[f'{st.secrets.bug_report_email}'],
            html=f'''
<h5>{st.session_state.username}</h5>
<p>{error_body}</p>
{{myimage}}
            ''',
            body_images={'myimage':img_list}
)
        del st.session_state.send_email


        #msg = MIMEText(error_body)
        #msg['From'] = st.secrets.admin_email
        #msg['To'] = st.secrets.bug_report_email
        #msg['Subject'] = error_subject

        #server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.starttls()
        #server.login(st.secrets.admin_email, 'hzfemdpfnfczwixe')
        #server.sendmail(st.secrets.admin_email, st.secrets.bug_report_email, msg.as_string())
        #server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")
else:
    pass
