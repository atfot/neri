import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def fix_user_info():
    if get_current_page_name() != "korean_analysis.py":
        # If anyone tries to access a secret page without being logged in,
        # redirect them to the login page
        st.switch_page("korean_analysis.py")
