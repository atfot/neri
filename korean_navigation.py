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
        st.title("💗 Amigo")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            st.page_link("pages/page1.py", label="나의 노력의 결과는?", icon="🏋️")
            st.page_link("pages/page4.py", label="당신의 카운셀러", icon="💛")

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()
            
            if st.button('fix user info'):
                 st.switch_page('pages/signin.py')

        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")


def logout():
    st.session_state.logged_in = False
    if "message_summary" in st.session_state:
        del st.session_state["messages"]
        del st.session_state['conversations']
        del st.session_state['message_summary']
        del st.session_state.client
    if "message_summary" not in st.session_state:
        del st.session_state["messages"]
        del st.session_state['conversations']
        del st.session_state.client
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
