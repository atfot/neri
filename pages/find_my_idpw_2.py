import streamlit as st
import time

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="wide",
        menu_items=None
    )

if 'user_id' not in st.session_state:
   st.session_state.user_id='test'
   st.session_state.password='test'
if 'username' not in st.session_state:
    st.session_state.username=st.secrets.user_name

st.session_state.filled_input=0
st.session_state.fix_id=False
st.session_state.fix_pw=False

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')


if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로", "https://neriuut.streamlit.app/")
    if button:
        del st.session_state.filled_input, st.session_state.username
        st.switch_page("streamlit_app.py")
    if st.session_state.fix_id==False:
        st.markdown('<center><h1>둘 중 어떤 것을 수정하고 싶으신가요?</h1></center>', unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns([3,4,4,3])
        with col2:
            id_checkbox=st.checkbox('아이디')
            if id_checkbox:
                st.session_state.fix_id=True
        with col3:
            st.checkbox('패스워드')
    if st.session_state_fix_id==True:
        st.write('hi')

            

if st.session_state.korean_mode==0:
    button=st.button("Go to main", "https://neriuut.streamlit.app/")
    if button:
        st.switch_page("streamlit_app.py")
    col1,col2=st.columns([5,5])
    with col1:
        st.markdown('<center><h3>Fix your ID</h3></center>', unsafe_allow_html=True)
    with col2:
        st.markdown('<center><h3>Fix your PW</h3></center>', unsafe_allow_html=True)
    if st.button('Do you wanna save your modifications?'):
        st.success('Your modifications have been applied!')
        st.write(st.session_state.user_id)
        st.write(st.session_state.password)
        time.sleep(5)
        st.switch_page('streamlit_app.py')
