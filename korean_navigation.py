import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("💗 네리")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", True):
            st.page_link("pages/korean_chatbot_2.py", label="당신의 카운셀러", icon="💛")
            st.page_link("pages/korean_analysis.py", label="내 정보", icon="ℹ️")

            st.write("")
            st.write("")

            col1,col2=st.columns([3,7])
            with col1:
                st.empty()
            with col2:
                if st.button("로그아웃",type='primary',use_container_width=True):
                    logout()
                if st.button('내 정보 수정',use_container_width=True):
                    st.switch_page('pages/signin.py')

        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")


def logout():
    st.session_state.logged_in = False
    if "messages" in st.session_state:
        del st.session_state["messages"]
        del st.session_state['conversations']
        del st.session_state['message_summary']
        del st.session_state.client
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
