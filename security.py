import streamlit as st
from streamlit import session_state as sss
import hashlib

def check(arg):
    if 'checked_object' not in sss:
        sss.checked_object=''
    hash_object = hashlib.sha3_512(arg.encode())
    hex_dig = hash_object.hexdigest()
    sss.checked_object=hex_dig
    st.write(sss.checked_object)
    sss.checked_object=""