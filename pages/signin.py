import streamlit as st
import pandas as pd

if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del st.session_state.signin
        st.switch_page("streamlit_app.py")
    st.title('')
    st.write(
        """
    # 반갑습니다! 
    # 회원가입 양식을 작성해주세요.
    
    현재 회원가입 페이지는 작동되지 않는 기능입니다.
    """
    )
    x=0
    with st.chat_message("assistant").form("Sign up Form"):
        st.write('빈칸을 전부 채워 넣어주세요.')
        st.write('"ok" 버튼을 누르시면 저희가 당신의 양식을 저장해드릴게요.')
        username = st.text_input('무슨 이름으로 불리고 싶으신가요?')
        if username:
            x+=1
        password = st.text_input("비밀번호", key="chatbot_api_key", type="password")
        if password:
            x+=1
        age = st.text_input('나이가 어떻게 되시나요?')
        if age:
            x+=1
        nationality = st.text_input('어느 나라 분이신가요?')
        if nationality:
            x+=1
        city = st.text_input('어느 도시에 거주중이신가요?')
        if city:
            x+=1
        problem = st.text_input("당신을 가장 크게 괴롭히는 것이  무엇인가요?")
        if problem:
            x+=1
        col1,col2=st.columns([9,1])
        with col2:
            button=st.form_submit_button('ok')
        if button:
            if x==6:
                col1,col2,col3=st.columns([3,6,1])
                with col2:
                    st.write(
        """

        "좋아요! 전부 저장했어요."
        이 내용대로 저장할게요.
        
        네리에 오신 당신을 환영합니다!

    """)
                df = pd.DataFrame({
                    "User Name": [username],
                    "Password": [password],
                    "age": [age],
                    "nationality": [nationality],
                    "city": [city],
                    "problem": [problem]
                })
                df.to_csv('c:/chatbot_test_1/user_database.csv', index=None)
                st.dataframe(df, use_container_width=True, hide_index=True)
                time.sleep(5)
                try:
                    progress_text = "로딩중"
                    my_bar = st.progress(0, text=progress_text)
                    
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        my_bar.progress(percent_complete + 1, text=progress_text)
                    time.sleep(1)
                    my_bar.empty()
                finally:
                    st.switch_page('pages/page1')
            else:
                pass
if st.session_state.korean_mode==0:
    button=st.button("Go to main", "https://neriuut.streamlit.app/")
    if button:
        del st.session_state.signin
        st.switch_page("streamlit_app.py")
    st.title('')
    st.write(
        """
    # Okay! Nice to meet you sir. 
    # Please fill in the blanks for sign up.

    The signup page is currently a non-functional feature.
    """
    )
    x=0
    with st.chat_message("assistant").form("Sign up Form"):
        st.write('Please fill all the blanks.')
        st.write('If you press "ok" button, we will save your sign up form on your desktop.')
        username = st.text_input('Tell me the name you want to be called in here.')
        if username:
            x+=1
        password = st.text_input("Your Password", key="chatbot_api_key", type="password")
        if password:
            x+=1
        age = st.text_input('How old are you?')
        if age:
            x+=1
        nationality = st.text_input('Where are you from?')
        if nationality:
            x+=1
        city = st.text_input('Tell me which city are you living in.')
        if city:
            x+=1
        problem = st.text_input("What's your biggest problem right now?")
        if problem:
            x+=1
        col1,col2=st.columns([9,1])
        with col2:
            button=st.form_submit_button('ok')
        if button:
            if x==6:
                col1,col2,col3=st.columns([3,6,1])
                with col2:
                    st.write(
        """

        "Okay! We saved your form."
        This is your signup information.
        
        Welcome to Amigo

    """)
                df = pd.DataFrame({
                    "User Name": [username],
                    "Password": [password],
                    "age": [age],
                    "nationality": [nationality],
                    "city": [city],
                    "problem": [problem]
                })
                df.to_csv('c:/chatbot_test_1/user_database.csv', index=None)
                st.dataframe(df, use_container_width=True, hide_index=True)
                time.sleep(5)
                try:
                    progress_text = "Operation in progress. Please wait."
                    my_bar = st.progress(0, text=progress_text)
                    
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        my_bar.progress(percent_complete + 1, text=progress_text)
                    time.sleep(1)
                    my_bar.empty()
                finally:
                    st.switch_page('pages/page1')
            else:
                pass