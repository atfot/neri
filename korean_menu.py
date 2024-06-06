import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit import session_state as sss
from openai import OpenAI
from app_css import app_design

def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        #st.secrets.app_design_css
        app_design()
        st.image('https://imgur.com/CernNDq.png',use_column_width=True)
        st.write("")
        st.write("")

        if sss.get("logged_in", True):
            st.page_link("pages/korean_chatbot.py", label="당신의 카운셀러", icon="🩹")
            st.page_link("pages/korean_instruction.py", label="사용법", icon="ℹ️")
            st.page_link("pages/korean_bug_report.py", label="오류 제보", icon="⚠️")
            st.page_link("pages/korean_analysis.py", label="심리분석 결과", icon="🔎")
            st.page_link("pages/korean_about_me.py", label="개발자의 말", icon="💭")
            st.title('')

            if st.button("로그아웃",type='primary',use_container_width=True):
                logout()
            if st.button("내 정보",type='secondary',use_container_width=True):
                st.switch_page("pages/korean_my_info.py")
            if st.button("대화 저장",type='secondary',use_container_width=True):
                st.switch_page("pages/korean_my_info.py")

            st.markdown(
                """
                <div style="left: 0; width: 101%; color: #000000; text-align: left;">
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
