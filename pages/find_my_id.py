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
sss.new_id=''
st.write(sss.id)

if 'korean_mode' not in sss:
    st.switch_page('streamlit_app.py')


if sss.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del sss.filled_input, sss.new_id
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>아이디 수정</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('유저 이름')
    if nickname:
        if nickname!=sss.username:
            st.error('해당 유저 이름이 존재하지 않습니다')
        else:
            sss.filled_input+=1
    password=st.text_input('패스워드',type='password')
    if password:
        if password!=sss.pw:
            st.error('사용하시던 패스워드가 아닙니다.')
        else:
            sss.filled_input+=1
    new_id=st.text_input('새로 사용할 ID',key='new_id_')
    if new_id:
        if new_id==sss.id:
            st.error('원래 사용하시던 아이디와 동일합니다.')
        else:
            sss.filled_input+=1
    new_id_check=st.text_input('새로 사용하실 ID를 다시 한번 적어주세요',type='password',key='new_id_check')
    if new_id_check:
        if new_id_check!=new_id:
            st.error('새로운 아이디와 해당 아이디가 서로 다릅니다.')    
        else:
            if 'new_id' not in sss:
                sss.new_id=new_id_check
            sss.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('이대로 저장할까요?', type='primary',use_container_width=True):
                if sss.filled_input==4 or sss.filled_input==8:
                    sss.id=sss.new_id
                    st.success('수정 내역이 저장되었습니다!')
                    st.markdown(f'<p><center><b>수정한 아이디 : {sss.id}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del sss.filled_input,sss.new_id
                    st.switch_page('streamlit_app.py')
                else:
                    pass

if sss.korean_mode==0:
    button=st.button("Back to Main")
    if button:
        del sss.filled_input, sss.new_id
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>Change your ID</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('Your username')
    if nickname:
        if nickname!=sss.username:
            st.error('There are no such username in here.')
        else:
            sss.filled_input+=1
    password=st.text_input('Password',type='password')
    if password:
        if password!=sss.pw:
            st.error("Doesn't match the password for an account with that username.")
        else:
            sss.filled_input+=1
    new_id=st.text_input('New ID',key='new_id')
    if new_id:
        if new_id==sss.id:
            st.error('This is the same ID you originally used.')
        else:
            sss.filled_input+=1
    new_id_check=st.text_input('Write down the new ID you want to use again',type='password',key='new_id_check')
    if new_id_check:
        if new_id_check!=new_id:
            st.error('The new ID and the corresponding ID are different.')    
        else:
            if 'new_id' not in sss:
                sss.new_id=new_id_check
            sss.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('Do you want to save it as is?', type='primary',use_container_width=True):
                if sss.filled_input==4 or sss.filled_input==8:
                    sss.id=sss.new_id
                    st.success('Your modifications have been saved!')
                    st.markdown(f'<p><center><b>Modified ID : {sss.id}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del sss.filled_input,sss.new_id
                    st.switch_page('streamlit_app.py')
                else:
                    pass