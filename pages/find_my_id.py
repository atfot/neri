import streamlit as st
import time

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )
st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
            
/* 타이틀 */
#change-your-id > div > span {
	font-family: 'Beeunhye';
    font-size: 2.25em;
}



   

/* 메인 화면으로 */
div.block-container.st-emotion-cache-gh2jqd.ea3mdgi5 > div > div > div > div:nth-child(2) > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
}
            
/* 유저 이름_패스워드_새로 사용할 ID_다시 한번 적기 */
div.block-container.st-emotion-cache-gh2jqd.ea3mdgi5 > div > div > div > div > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
}
            
            
/* 이대로 저장할까요? */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div:nth-child(2) > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
}
            
/* share 버튼 */
div.st-emotion-cache-zq5wmm.ezrtsby0 > div > div:nth-child(1) > button > div > span {
	font-family: 'Beeunhye';
    font-size: 2em;
}

/* 에러 메세지 */
div.block-container.st-emotion-cache-gh2jqd.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p  {
	font-family: 'Beeunhye';
    font-size: 1.75em;
}
            
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div:nth-child(3) > div > div > div > div > div > div > p
            
div.block-container.st-emotion-cache-gh2jqd.ea3mdgi5 > div > div > div > div:nth-child(8) > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
}

            
/* 성공 메세지 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div:nth-child(3) > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
}
            
/* 바뀐 아이디 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > div > center > b {
	font-family: 'Beeunhye';
    font-size: 2em;
}
            </style>
""", unsafe_allow_html=True)

if 'id' not in st.session_state:
    if st.session_state.korean_mode==1:
        st.session_state.id=st.secrets.user_id
    else:
        st.session_state.id=st.secrets.user_id_2
if 'pw' not in st.session_state:
   if st.session_state.korean_mode==1:
    st.session_state.pw=st.secrets.user_pw
   else:
       st.session_state.pw=st.secrets.user_pw_2
if 'username' not in st.session_state:
   if st.session_state.korean_mode==1:
    st.session_state.username=st.secrets.user_name
   else:
       st.session_state.username=st.secrets.user_name_2
st.session_state.filled_input=0

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')


if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>아이디 수정</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('유저 이름')
    if nickname:
        if nickname!=st.session_state.username:
            st.error('해당 유저 이름이 존재하지 않습니다')
        else:
            st.session_state.filled_input+=1
    password=st.text_input('패스워드',type='password')
    if password:
        if password!=st.session_state.pw:
            st.error('사용하시던 패스워드가 아닙니다.')
        else:
            st.session_state.filled_input+=1
    new_id=st.text_input('새로 사용할 ID',key='new_id')
    if new_id:
        if new_id==st.session_state.id:
            st.error('원래 사용하시던 아이디와 동일합니다.')
        else:
            st.session_state.filled_input+=1
    new_id_check=st.text_input('새로 사용하실 ID를 다시 한번 적어주세요',type='password',key='new_id_check')
    if new_id_check:
        if new_id_check!=new_id:
            st.error('새로운 아이디와 해당 아이디가 서로 다릅니다.')    
        else:
            if 'new_id' not in st.session_state:
                st.session_state.new_id=new_id_check
            st.session_state.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('이대로 저장할까요?', type='primary',use_container_width=True):
                if st.session_state.filled_input==4 or st.session_state.filled_input==8:
                    st.session_state.id=st.session_state.new_id
                    st.success('수정 내역이 저장되었습니다!')
                    st.markdown(f'<p><center><b>수정한 아이디 : {st.session_state.id}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del st.session_state.filled_input
                    st.switch_page('streamlit_app.py')
                else:
                    pass

if st.session_state.korean_mode==0:
    button=st.button("Back to Main")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>Change your ID</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('Your username')
    if nickname:
        if nickname!=st.session_state.username:
            st.error('There are no such username in here.')
        else:
            st.session_state.filled_input+=1
    password=st.text_input('Password',type='password')
    if password:
        if password!=st.session_state.pw:
            st.error("Doesn't match the password for an account with that username.")
        else:
            st.session_state.filled_input+=1
    new_id=st.text_input('New ID',key='new_id')
    if new_id:
        if new_id==st.session_state.id:
            st.error('This is the same ID you originally used.')
        else:
            st.session_state.filled_input+=1
    new_id_check=st.text_input('Write down the new ID you want to use again',type='password',key='new_id_check')
    if new_id_check:
        if new_id_check!=new_id:
            st.error('The new ID and the corresponding ID are different.')    
        else:
            if 'new_id' not in st.session_state:
                st.session_state.new_id=new_id_check
            st.session_state.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('Save', type='primary',use_container_width=True):
                if st.session_state.filled_input==4 or st.session_state.filled_input==8:
                    st.session_state.id=st.session_state.new_id
                    st.success('Your modifications have been saved!')
                    st.markdown(f'<p><center><b>Modified ID : {st.session_state.id}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del st.session_state.filled_input
                    st.switch_page('streamlit_app.py')
                else:
                    pass