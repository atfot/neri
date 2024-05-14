import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit import session_state as sss
from openai import OpenAI

def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        #st.secrets.app_design_css
        st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* share 버튼 */
div.st-emotion-cache-zq5wmm.ezrtsby0 > div > div:nth-child(1) > button > div > span {
	font-family: 'Beeunhye';
	font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}  
/* running... */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > label {
	font-family: 'Beeunhye';
	font-size: 1.5em;
    letter-spacing:0.075em;
}

/* stop */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > span > button {
	font-family: 'Beeunhye';
	font-size: 1.5em;
    letter-spacing:0.075em;
}

/* 메뉴 화면 */
/* 메뉴 */
span.st-emotion-cache-rkv7nx.e11k5jya0 > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    margin-top: -0.15em; 
    margin-left: 0.25em; 
    letter-spacing:0.075em;
}       

/* 로그아웃 버튼 */
div.st-emotion-cache-dvne4q.eczjsme4 > div > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
	font-size: 2em;
    letter-spacing:0.075em;
}     

/* 로그아웃 메세지 */      
div.st-emotion-cache-dvne4q.eczjsme4 > div > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.5em;
    letter-spacing:0.075em;
}

/* 챗봇 */  
/* 챗봇 글씨체 */
div.st-emotion-cache-1dp44rk.eeusbqq3 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
	margin-top: -0.35em;
    letter-spacing:0.075em;
}     
div.st-emotion-cache-1ovfu5.eeusbqq3 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
	margin-top: -0.35em;
    letter-spacing:0.075em;
}     

/* thinking... */
div.st-emotion-cache-c6gdys.e18r7x300 > div > p {
	font-family: 'Beeunhye';
	font-size: 2em;
    letter-spacing:0.075em;
}
                    
/* 오류 제보 */
/* 기본 메세지 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
/* 설명란 */                    
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > label > div > p {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
/* 성공 실패 메세지*/
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
                    
/* 내 정보 */
/* 내 프로필 */
.st-emotion-cache-10trblm {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
/* 프로필 내역 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
/* 수정란 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > label > div > p{
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}

/* 내 정보 수정 버튼 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > button > div > p {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
/* 성공 실패 메세지 */
div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p > strong {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
                    
/* 심리분석 결과 */
/* 리스트 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > ol > li {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
/* 버튼 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > button > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
/* 전송중... */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
/*성공 메세지 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}

</style>
"""

, unsafe_allow_html=True)
        st.image('https://imgur.com/CernNDq.png',use_column_width=True)
        st.write("")
        st.write("")

        if sss.get("logged_in", True):
            st.page_link("pages/korean_chatbot.py", label="당신의 카운셀러", icon="🩹")
            st.page_link("pages/korean_analysis.py", label="사용법", icon="ℹ️")
            st.page_link("pages/korean_bug_report.py", label="오류 제보", icon="⚠️")
            st.page_link("pages/korean_analysis_2.py", label="심리분석 결과", icon="🔎")
            st.title('')

            if st.button("로그아웃",type='primary',use_container_width=True):
                logout()
            if st.button("내 정보",type='secondary',use_container_width=True):
                st.switch_page("pages/korean_my_info.py")

            st.markdown(
                """
                <div style="position: fixed; bottom: 0; left: 1%; width: 50%; color: #000000; padding: 1px; text-align: left;">
                    Developed By <a  href="https://i.imgur.com/JuFxv4h.png" target="_blank">Hyun Kyu Cho</a><br>
                    Made with Streamlit<br>
                    Powered By OpenAI
                </div>
                """,
                unsafe_allow_html=True
            )

        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")


def logout():
    sss.logged_in = False
    if "messages" in sss:
        del sss["messages"]
        del sss['conversations']
        del sss['message_summary']
        try:
            del sss.username
        except:
            pass
        try:
            del sss.my_info
        except:
            pass
        try:
            del sss.many_login_attempt
        except:
            pass
        try:
            del sss.problem_analysis
        except:
            pass
        del sss.client
    st.info("다음에 또 뵈어요😊")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
