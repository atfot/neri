import streamlit as st
import time

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )

if 'user_id' not in st.session_state:
   st.session_state.user_id='test'
if 'password' not in st.session_state:
   st.session_state.password='test'
if 'username' not in st.session_state:
    st.session_state.username=st.secrets.user_name
st.session_state.filled_input=0
st.session_state.save_success=False

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')


if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>아이디 수정</h3></center>', unsafe_allow_html=True)
    with st.form('my_form'):
        nickname=st.text_input('닉네임')
        if nickname:
            if nickname!=st.session_state.username:
                st.error('사용하시던 닉네임이 아닙니다.')
            else:
                st.session_state.filled_input+=1
        password=st.text_input('패스워드',type='password')
        if password:
            if password!=st.session_state.password:
                st.error('사용하시던 패스워드가 아닙니다.')
            else:
                st.session_state.filled_input+=1
        new_id=st.text_input('새로 사용할 ID',key='new_id')
        if new_id:
            if new_id==st.session_state.user_id:
                st.error('원래 사용하시던 아이디와 동일합니다.')
            else:
                st.session_state.filled_input+=1
        new_id_check=st.text_input('새로 사용하실 ID를 다시 한번 적어주세요',type='password',key='new_id_check')
        if new_id_check:
            if new_id_check!=new_id:
                st.error('새로운 아이디와 해당 아이디가 서로 다릅니다.')    
            else:
                st.session_state.filled_input+=1
        col1,col2=st.columns([8.9,1.1])
        with col2:
            submitted=st.form_submit_button('저장',use_container_width=True)
            if submitted:
                if st.session_state.filled_input==4:
                    st.session_state.save_success=True
                else:
                    st.error('빈칸을 전부 채워넣어주세요.')
        if st.session_state.save_success==True:
            st.success('수정 내역이 저장되었습니다!')
            if st.session_state.user_id:
                st.write(st.session_state.user_id)
            if st.session_state.password:
                st.write(st.session_state.password)
            time.sleep(5)
            del st.session_state.filled_input,st.session_state.save_success
            st.switch_page('streamlit_app.py')
        else:
            pass
if st.session_state.korean_mode==0:
    button=st.button("Go to main", "https://neriuut.streamlit.app/")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>Change your ID</h3></center>', unsafe_allow_html=True)
    with st.form('my_form'):
        nickname=st.text_input('Username')
        if nickname:
            if nickname!=st.session_state.username:
                st.error('This is not the username you were using.')
            else:
                st.session_state.filled_input+=1
        password=st.text_input('Password',type='password')
        if password:
            if password!=st.session_state.password:
                st.error('This is not the password you are using.')
            else:
                st.session_state.filled_input+=1
        new_id=st.text_input('New ID',key='new_id')
        if new_id:
            if new_id==st.session_state.user_id:
                st.error('This is the same username you originally used.')
            else:
                st.session_state.filled_input+=1
        new_id_check=st.text_input('Write down the new ID you want to use again.',type='password',key='new_id_check')
        if new_id_check:
            if new_id_check!=new_id:
                st.error('The new ID and the corresponding ID are different.')    
            else:
                st.session_state.filled_input+=1
        col1,col2=st.columns([8.9,1.1])
        with col2:
            submitted=st.form_submit_button('Save',use_container_width=True)
            if submitted:
                if st.session_state.filled_input==4:
                    st.success('Your modifications have been saved!')
                    if st.session_state.user_id:
                        st.write(st.session_state.user_id)
                    if st.session_state.password:
                        st.write(st.session_state.password)
                    time.sleep(5)
                    del st.session_state.filled_input
                    st.switch_page('streamlit_app.py')
                else:
                    st.error('Fill in all the blanks.')