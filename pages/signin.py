import streamlit as st
import pandas as pd
import time
import streamlit.components.v1 as components

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="wide",
        menu_items=None
    )

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')

if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del st.session_state.signin, st.session_state.many_login_attempt
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
        user_id=st.text_input('사용하실 아이디를 적어주세요.')
        if user_id:
            x+=1
            st.session_state.user_id=user_id
        password = st.text_input("비밀번호", key="chatbot_api_key", type="password")
        if password:
            x+=1
            st.session_state.password=password
        username = st.text_input('무슨 이름으로 불리고 싶으신가요?')
        if username:
            x+=1
            st.session_state.username=username
        gender=st.selectbox(
            '성별이 어떻게 되시죠?',
            ('남자','여자'),
            index=None,
            placeholder='남자/여자'
            )
        if gender:
            x+=1
            st.session_state.gender=gender
        age = st.slider(
            '나이가 어떻게 되시나요?',
            7,100,30
            )
        if age:
            x+=1
            st.session_state.age=age
        nationality = st.text_input('어느 나라 분이신가요?')
        if nationality:
            x+=1
            st.session_state.nationality=nationality
        city = st.text_input('어느 도시에 거주중이신가요?')
        if city:
            x+=1
            st.session_state.city=city
        problem = st.text_area("당신을 가장 크게 괴롭히는 것이  무엇인가요?🤔")
        if problem:
            x+=1
            st.session_state.problem=problem
        problem_explanation=st.text_area("문제점을 좀더 자세히 설명해주세요. 자세히 설명해주실수록 좋아요😊")
        if problem_explanation:
            x+=1
            st.session_state.problem_explanation=problem_explanation
        goal=st.text_area("최종 목표가 무엇인지 말해주세요!")
        if goal:
            x+=1
            st.session_state.goal=goal
        col1,col2=st.columns([9,1])
        with col2:
            button=st.form_submit_button('ok')
        if button:
            if x==10:
                col1,col2,col3=st.columns([2,6,2])
                with col2:
                    st.write(
        """

        "좋아요! 전부 저장했어요."

        해당 내용대로 저장했습니다.
        
        
        네리에 오신 당신을 환영합니다!

    """)
                col1,col2=st.columns([5,5])
                with col1:
                    st.write(f"""
    아이디:{user_id}

    비밀번호: {password}

    유저 이름: {username}

    나이: {age}

    국적: {nationality}

    도시: {city}
    """)
                with col2:
                    st.write(f"""
    고민: {problem}

    고민에 대한 설명: {problem_explanation}

    목표: {goal}
    """)
                time.sleep(15)
                try:
                    progress_text = "로딩중"
                    my_bar = st.progress(0, text=progress_text)                    
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        my_bar.progress(percent_complete + 1, text=progress_text)
                    time.sleep(1)
                    my_bar.empty()
                finally:
                    st.switch_page("streamlit_app.py")
            else:
                pass
if st.session_state.korean_mode==0:
    button=st.button("Go to main", "https://neriuut.streamlit.app/")
    if button:
        del st.session_state.signin, st.session_state.many_login_attempt
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
        user_id=st.text_input('Your ID')
        if user_id:
            x+=1
            st.session_state.user_id=user_id
        password = st.text_input("Your Password", key="chatbot_api_key", type="password")
        if password:
            x+=1
            st.session_state.password=password
        username = st.text_input('Tell me the name you want to be called in here.')
        if username:
            x+=1
            st.session_state.username=username
        gender=st.selectbox(
            'What is your gender?',
            ('Male','Female'),
            index=None,
            placeholder='Gentleman/Lady'
            )
        if gender:
            x+=1
            st.session_state.gender=gender
        age = st.slider(
            'How old are you?',
            7,100,30
            )
        if age:
            x+=1
            st.session_state.age=age
        nationality = st.text_input('Where are you from?')
        if nationality:
            x+=1
            st.session_state.nationality=nationality
        city = st.text_input('Tell me which city are you living in.')
        if city:
            x+=1
            st.session_state.city=city
        problem = st.text_area("What's your biggest problem right now?🤔")
        if problem:
            x+=1
            st.session_state.problem=problem
        problem_explanation=st.text_area("Please describe your issue in more detail. The more details you can provide, the better😊")
        if problem_explanation:
            x+=1
            st.session_state.problem_explanation=problem_explanation
        goal=st.text_area("Tell us what your end goal is!")
        if goal:
            x+=1
            st.session_state.goal=goal
        col1,col2=st.columns([9,1])
        with col2:
            button=st.form_submit_button('ok')
        if button:
            if x==10:
                col1,col2,col3=st.columns([3,6,1])
                with col2:
                    st.write(
        """

        "Okay! We saved your form."

        This is your signup information.

        
        Welcome to Amigo

    """)
                col1,col2=st.columns([5,5])
                with col1:
                    st.write(f"""
    ID:{user_id}

    PW: {password}

    User Name: {username}

    Age: {age}

    Nationality: {nationality}

    City: {city}
    """)
                with col2:
                    st.write(f"""
    Your Problem: {problem}

    Detailed Explanation of Your Problem: {problem_explanation}

    Your goal: {goal}
    """)
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
                    st.switch_page("streamlit_app.py")
            else:
                pass