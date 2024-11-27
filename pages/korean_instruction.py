import streamlit as st
from korean_menu import make_sidebar
from streamlit import session_state as sss

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="centered"
)

try:
    del sss.fix_info, sss.auth_email
except:
    pass
make_sidebar()
st.write("이걸 왜 만들었는지 적을 것")
st.write("어떻게 사용해야 하는지 적을 것")
st.write("""
당신의 카운셀러 : 가장 괴롭고 힘들었던 부분들을 챗봇과 함께 대화해보세요.

심리분석 결과 : 대화내용에 대한 기초적인 분석을 고객님의 이메일로 보내드립니다.

내 정보 : 고객님의 정보를 수정하실수 있습니다.

오류 제보 : 사용하시면서 생긴 모든 문제를 여기에 적어서 보내주세요.
""")