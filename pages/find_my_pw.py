import streamlit as st
import time
from streamlit import session_state as sss
from app_css import find_my_idpw_design

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )
#st.secrets.signin_idpw_css
find_my_idpw_design()

if sss.korean_mode==1:
    if 'id' not in sss:
        sss.id=st.secrets.user_id
    if 'pw' not in sss:
        sss.pw=st.secrets.user_pw
    if 'username' not in sss:
        sss.username=st.secrets.user_name
if sss.korean_mode==0:
    if 'id' not in sss:
        sss.id=st.secrets.user_id
    if 'pw' not in sss:
        sss.pw=st.secrets.user_pw
    if 'username' not in sss:
        sss.username=st.secrets.user_name_2
sss.filled_input=0
sss.new_pw=''

if 'korean_mode' not in sss:
    st.switch_page('streamlit_app.py')


if sss.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del sss.filled_input,sss.new_pw
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>비밀번호 수정</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('유저 이름')
    if nickname:
        if nickname!=sss.username:
            st.error('해당 유저 이름이 존재하지 않습니다')
        else:
            sss.filled_input+=1
    user_id=st.text_input('아이디',type='password')
    if user_id:
        if user_id!=sss.id:
            st.error('사용하시던 아이디가 아닙니다.')
        else:
            sss.filled_input+=1
    new_pw=st.text_input('새로 사용할 비밀번호',key='new_pw')
    if new_pw:
        if new_pw==sss.pw:
            st.error('원래 사용하시던 아이디와 동일합니다.')
        else:
            sss.filled_input+=1
    new_pw_check=st.text_input('새로 사용하실 비밀번호를 다시 한번 적어주세요',type='password',key='new_pw_check')
    if new_pw_check:
        if new_pw_check!=new_pw:
            st.error('새로운 비밀번호와 해당 비밀번호가 서로 다릅니다.')    
        else:
            if 'new_pw' not in sss:
                sss.new_id=new_pw_check
            sss.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('이대로 저장할까요?', type='primary',use_container_width=True):
                if sss.filled_input==4 or sss.filled_input==8:
                    sss.pw=sss.new_pw
                    st.success('수정 내역이 저장되었습니다!')
                    st.markdown(f'<p><center><b>수정한 비밀번호 : {sss.pw}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del sss.filled_input,sss.new_pw
                    st.switch_page('streamlit_app.py')
                else:
                    pass

if sss.korean_mode==0:
    button=st.button("Back to Main")
    if button:
        del sss.filled_input,sss.new_pw
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>Change your Password</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('Your username')
    if nickname:
        if nickname!=sss.username:
            st.error('There are no such username in here.')
        else:
            sss.filled_input+=1
    user_id=st.text_input('Your ID',type='password')
    if user_id:
        if user_id!=sss.id:
            st.error("Doesn't match the ID for an account with that username.")
        else:
            sss.filled_input+=1
    new_pw=st.text_input('New PW',key='new_pw')
    if new_pw:
        if new_pw==sss.pw:
            st.error('This is the same password you originally used.')
        else:
            sss.filled_input+=1
    new_pw_check=st.text_input('Write down the new password you want to use again',type='password',key='new_pw_check')
    if new_pw_check:
        if new_pw_check!=new_pw:
            st.error('The new password and the corresponding password are different.')    
        else:
            if 'new_pw' not in sss:
                sss.new_pw=new_pw_check
            sss.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('Do you want to save it as is?', type='primary',use_container_width=True):
                if sss.filled_input==4 or sss.filled_input==8:
                    sss.pw=sss.new_pw
                    st.success('Your modifications have been saved!')
                    st.markdown(f'<p><center><b>Modified Password : {sss.pw}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del sss.filled_input,sss.new_pw
                    st.switch_page('streamlit_app.py')
                else:
                    pass