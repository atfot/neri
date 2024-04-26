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
   st.session_state.username='test'

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')

if 'fix_id' not in st.session_state:
    st.session_state.fix_id=False

if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        st.switch_page("streamlit_app.py")
    col1,col2=st.columns([5,5])
    with col1:
        st.markdown('<center><h3>아이디 수정</h3></center>', unsafe_allow_html=True)
        if st.session_state.fix_id==False:
            st.write('사용하시던 닉네임과 패스워드를 적어주세요.')
            nickname=st.text_input('닉네임')
            password=st.text_input('패스워드')
            x=0
            if nickname=='test':
                x+=1
            if password=='test':
                x+=1
            if x==2:
                st.session_state.fix_id=True
        if st.session_state.fix_id==True:
            st.write('새로 사용하실 아이디를 적어주세요.')
            new_id=st.text_input('새로 사용할 ID')
            new_id_check=st.text_input('다시 한번 적어주세요',type='password')
            x=0
            if new_id:
                x+=1
            if password:
                x+=1
            if new_id==new_id_check:
                if x==2:
                    st.session_state.new_id=new_id
    with col2:
        st.markdown('<center><h3>패스워드 수정</h3></center>', unsafe_allow_html=True)
    col1,col2,col3=st.columns([2,6,2])
    with col2:
        if st.button('이대로 저장할까요?', type='primary',use_container_width=True):
            st.success('수정 내역이 저장되었습니다!')
            if st.session_state.user_id:
                st.write(st.session_state.user_id)
            if st.session_state.password:
                st.write(st.session_state.password)
            time.sleep(5)
            st.switch_page('streamlit_app.py')

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