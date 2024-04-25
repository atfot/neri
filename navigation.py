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
        st.title("💗 Neri")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", True):
            st.page_link("pages/original_chatbot.py", label="My Councelor", icon="💛")
            st.page_link("pages/original_analysis.py", label="My Info", icon="🏋️")

            st.write("")
            st.write("")

        if st.button("Log out",type='primary',use_container_width=True):
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
            del st.session_state.my_info
        except:
            pass
        del st.session_state.client
    st.info("See ya next time😊")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
