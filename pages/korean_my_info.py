import streamlit as st
from korean_menu import make_sidebar
from openai import OpenAI
import pandas as pd
import time
from streamlit import session_state as sss
from streamlit import secrets as sct
import re

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="centered"
)
make_sidebar()

if sss.id==False:
    sss.username=sct.user_name_2
    sss.age=sct.age_2
    sss.gender=sct.user_gender_2
    sss.problem=sct.problem_2
    sss.problem_explanation=sct.problem_explanation_2
    sss.goal=sct.goal_2
    sss.user_email=sct.user_email_2

if 'fix_info' not in sss:
    sss.fix_info=False
if 'fix_complete' not in sss:
    sss.fix_complete=False
sss.filled_input=0

def fix_info():
  sss.fix_info=True

col1,col2=st.columns([5,5])
with col1:
    st.write('')
    st.markdown('<h4>내 정보</h4>',unsafe_allow_html=True)
    st.markdown(f'''
                <p>
                <b>1. 닉네임 : </b>{sss.username}

                <b>2. 나이 : </b>{sss.age}

                <b>3. 성별 : </b>{sss.gender}

                <b>4. 문제점 : </b>
                
                {sss.problem}

                <b>5. 문제점 세부설명 : </b>
                
                {sss.problem_explanation}

                <b>6. 목표 : </b>
                
                {sss.goal}
                </p>
                ''', unsafe_allow_html=True)   
    if sss.fix_info==False:
        st.button('내 정보 수정',use_container_width=True,on_click=fix_info)  
    else:
        pass
with col2:  
    if sss.fix_info==True:      
        st.write("**이제 정보를 고칠수 있습니다😊**")

        user_email = st.text_input('**새로 사용하실 이메일 주소를 적어주세요.**', key='new_user_email',type='password')
        if user_email:
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$', user_email): 
                st.error('정확한 이메일을 적어주세요!')
            else:
                if user_email != sct.user_email and user_email !=sct.user_email_2 and sss.user_email:
                    sss.filled_input+=1
                    if 'auth_email' not in sss:
                        sss.auth_email=user_email
                    #sss.user_email=user_email
                elif user_email == sss.user_email:
                    st.error("해당 이메일 주소는 그동안 사용하셨던 이메일 주소와 동일합니다.")
                else:
                    st.error('해당 이메일 주소가 이미 사용중입니다.')
        email_check = st.text_input('**다시 새로 사용하실 이메일을 적어주세요.**',key='email_check',type='password')
        if email_check:
            if email_check!=sss.auth_email:
                st.error('해당 이메일 주소가 이전에 사용하셨던 이메일 주소와 동일합니다.')
            if email_check==sss.auth_email:
                sss.filled_input+=1
        username = st.text_input('**어떤 별명으로 불리고 싶으신지 적어주세요.**',key='new_username')
        if username:
            if username!=sct.user_name and username!=sct.user_name_2 and username!=sss.username:
                sss.filled_input+=1
                #sss.username=username
            elif username==sss.username:
                st.error('해당 별명은 지금껏 사용하셨던 별명과 동일합니다.')
            else:
                st.error('해당 별명이 이미 존재합니다.')
            
        problem = st.text_area("**지금 가장 큰 문제는 무엇인가요?🤔**",key='new_problem')
        if problem:
            sss.filled_input+=1
            #sss.problem=problem
        problem_explanation=st.text_area("**문제를 더 자세히 설명해 주세요. 자세하게 작성해주실수록 좋습니다😊**",key='new_problem_explanation')
        if problem_explanation:
            sss.filled_input+=13
            #sss.problem_explanation=problem_explanation
        goal=st.text_area("**최종 목표가 무엇인지 알려주세요!**",key='new_goal')
        if goal:
            sss.filled_input+=1
            #sss.goal=goal
    else:
        pass
if sss.fix_info==True:
    col1,col2,col3=st.columns([2.5,5,2.5])
    with col2:
        if st.button('**수정**',use_container_width=True):
            if sss.filled_input==6:
                sss.user_email=user_email
                sss.username=username
                sss.problem=problem
                sss.problem_explanation=problem_explanation
                sss.goal=goal
                del sss.fix_info, sss.filled_input, sss.fix_complete, sss.auth_email
                st.success('**사용자 프로필이 수정되었습니다👍**')
                st.rerun()
            else:
                st.error('**빈칸을 모두 채워넣어주세요🙃**')
        
else:
    pass