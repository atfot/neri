import streamlit as st
from korean_menu import make_sidebar
from streamlit import session_state as sss
from openai import OpenAI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import pdfkit
from send_email import send_analysis_via_email

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="centered"
)
make_sidebar()
if sss.id==False:
    sss.user_email='hk4198@naver.com'
else:
    pass



st.subheader('📌 Neri는 고객님께서 직접 요청하실 때만 고객님의 심리분석 결과를 고객님의 이메일로 발송해드리고 있어요!')
st.write("여러가지 이유가 있겠지만 이러한 이유들 때문이에요.")
st.write('1. **정신과 의사선생님** 또는 **심리상담사님**께 보여드리기 좋은 방식이에요.')
st.write('2. **오늘의 분석 결과를 한번에 확인하기** 좋은 방식이에요.')
st.write('3. **다른 방식 대비 내용 수정이 쉽지 않기 때문**이에요.')         
st.write("""         
**해당 심리분석 결과는 AI가 판단한 것이기 때문에 정확하지 않아요!**
         
따라서 **고객님에 대한 판단**은 **정신과 의사선생님** 혹은 **심리상담사님**께서 좀더 정확히 아실거에요.
""")

if st.button('고객님의 이메일로 분석 결과를 받아보시겠어요?',use_container_width=True):
    send_analysis_via_email()