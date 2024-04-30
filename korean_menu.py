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
        st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

* {
	font-family: 'Beeunhye';
	font-size: 30px;
}
p {
	font-family: 'Beeunhye';
	font-size: 30px;
}       
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-ugcgyn.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 > div.st-emotion-cache-16txtl3.eczjsme4 > div > div > div > div > div:nth-child(2) > div > div > div > h1 {
	font-family: 'Beeunhye';
	font-size: 36px;
}       
</style>
""", unsafe_allow_html=True)
        st.markdown("<h1>🧡 네리</h1>",unsafe_allow_html=True)
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", True):
            st.page_link("pages/korean_chatbot.py", label="당신의 카운셀러", icon="🩹")
            st.divider()
            st.page_link("pages/korean_analysis.py", label="내 정보", icon="ℹ️")
            st.divider()
            st.page_link("pages/korean_instruction.py", label="사용법", icon="❓")
            st.divider()

            if st.button("로그아웃",type='primary',use_container_width=True):
                logout()

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
        try:
            del st.session_state.username
        except:
            pass
        try:
            del st.session_state.my_info
        except:
            pass
        try:
            del st.session_state.many_login_attempt
        except:
            pass
        del st.session_state.client
    st.info("다음에 또 뵈어요😊")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
