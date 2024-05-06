import streamlit as st
from korean_menu import make_sidebar

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
make_sidebar()

st.title('네리를 만나러 오신 여러분을 환영합니다!')
st.title('')
st.write("""
네리는 **OpenAI사의 ChatGPT API**를 사용하여 만들어진 **인공지능 챗봇**이에요.
         
현규 : 솔직히 여기서 뭘 말해야할지 좀 고민해봐야겠다..ㅅㅂ...


         

""")