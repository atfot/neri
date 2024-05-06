import streamlit as st
import time

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )
#st.secrets.signin_idpw_css
st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

/* 메인 화면으로 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* share 버튼 */
div.st-emotion-cache-zq5wmm.ezrtsby0 > div > div:nth-child(1) > button > div > span {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* 타이틀 */ 
.st-emotion-cache-10trblm {
	font-family: 'Beeunhye';
    font-size: 2.25em;
    letter-spacing:0.075em;
}      

/* 모든 작성란 설명 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* 에러 메세지 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p  {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.075em;
}
   
/* 이대로 저장할까요? */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    color: #89482C;
    letter-spacing:0.075em;
}

/* 성공 메세지 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}
div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}
            
/* 바뀐 아이디 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > center > b {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

/* 회원가입 저장내역 */
div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

</style>
""", unsafe_allow_html=True)
st.write(st.session_state.korean_mode)
st.write(st.session_state.username)
st.write(st.secrets.user_name_2)
if 'id' not in st.session_state:
    if st.session_state.korean_mode==1:
        st.session_state.id=st.secrets.user_id
    if st.session_state.korean_mode==0:
        st.session_state.id=st.secrets.user_id_2
if 'pw' not in st.session_state:
   if st.session_state.korean_mode==1:
    st.session_state.pw=st.secrets.user_pw
   if st.session_state.korean_mode==0:
       st.session_state.pw=st.secrets.user_pw_2
if 'username' not in st.session_state:
   if st.session_state.korean_mode==1:
    st.session_state.username=st.secrets.user_name
   if st.session_state.korean_mode==0:
       st.session_state.username=st.secrets.user_name_2
st.session_state.filled_input=0

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')


if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>비밀번호 수정</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('유저 이름')
    if nickname:
        if nickname!=st.session_state.username:
            st.error('해당 유저 이름이 존재하지 않습니다')
        else:
            st.session_state.filled_input+=1
    user_id=st.text_input('아이디',type='password')
    if user_id:
        if user_id!=st.session_state.id:
            st.error('사용하시던 아이디가 아닙니다.')
        else:
            st.session_state.filled_input+=1
    new_pw=st.text_input('새로 사용할 비밀번호',key='new_pw')
    if new_pw:
        if new_pw==st.session_state.pw:
            st.error('원래 사용하시던 아이디와 동일합니다.')
        else:
            st.session_state.filled_input+=1
    new_pw_check=st.text_input('새로 사용하실 비밀번호를 다시 한번 적어주세요',type='password',key='new_pw_check')
    if new_pw_check:
        if new_pw_check!=new_pw:
            st.error('새로운 비밀번호와 해당 비밀번호가 서로 다릅니다.')    
        else:
            if 'new_pw' not in st.session_state:
                st.session_state.new_id=new_pw_check
            st.session_state.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('이대로 저장할까요?', type='primary',use_container_width=True):
                if st.session_state.filled_input==4 or st.session_state.filled_input==8:
                    st.session_state.pw=st.session_state.new_pw
                    st.success('수정 내역이 저장되었습니다!')
                    st.markdown(f'<p><center><b>수정한 비밀번호 : {st.session_state.pw}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del st.session_state.filled_input,st.session_state.id,st.session_state.pw,st.session_state.username
                    st.switch_page('streamlit_app.py')
                else:
                    pass

if st.session_state.korean_mode==0:
    button=st.button("Back to Main")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>Change your Password</h3></center>', unsafe_allow_html=True)
    nickname=st.text_input('Your username')
    if nickname:
        if nickname!=st.session_state.username:
            st.error('There are no such username in here.')
        else:
            st.session_state.filled_input+=1
    user_id=st.text_input('Your ID',type='password')
    if user_id:
        if user_id!=st.session_state.id:
            st.error("Doesn't match the ID for an account with that username.")
        else:
            st.session_state.filled_input+=1
    new_pw=st.text_input('New PW',key='new_pw')
    if new_pw:
        if new_pw==st.session_state.pw:
            st.error('This is the same password you originally used.')
        else:
            st.session_state.filled_input+=1
    new_pw_check=st.text_input('Write down the new password you want to use again',type='password',key='new_pw_check')
    if new_pw_check:
        if new_pw_check!=new_pw:
            st.error('The new password and the corresponding password are different.')    
        else:
            if 'new_pw' not in st.session_state:
                st.session_state.new_pw=new_pw_check
            st.session_state.filled_input+=1

    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('Save', type='primary',use_container_width=True):
                if st.session_state.filled_input==4 or st.session_state.filled_input==8:
                    st.session_state.pw=st.session_state.new_pw
                    st.success('Your modifications have been saved!')
                    st.markdown(f'<p><center><b>Modified Password : {st.session_state.pw}</b></center><p>',unsafe_allow_html=True)
                    time.sleep(5)
                    del st.session_state.filled_input,st.session_state.id,st.session_state.pw,st.session_state.username
                    st.switch_page('streamlit_app.py')
                else:
                    pass