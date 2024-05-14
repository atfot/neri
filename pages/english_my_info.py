import streamlit as st
from english_menu import make_sidebar
from openai import OpenAI
import pandas as pd
import time
from streamlit import session_state as sss
import re

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="centered"
)
make_sidebar()

def fix_info():
  sss.fix_info=True

col1,col2,col3=st.columns([4,1,5])
with col1:
    if sss.fix_info==False:
        st.write('')
        st.markdown('<h4>My Profile</h4>',unsafe_allow_html=True)
        st.markdown(f'''
                    <p>
                    <b>1. Username : </b>{sss.username}

                    <b>2. Age : </b>{sss.age}

                    <b>3. Gender : </b>{sss.gender}

                    <b>4. Problem : </b>
                    
                    {sss.problem}

                    <b>5. Problem Explanation : </b>
                    
                    {sss.problem_explanation}

                    <b>6. Goal : </b>
                    
                    {sss.goal}
                    </p>
                    ''', unsafe_allow_html=True)   
        st.button('Fix my Info',use_container_width=True,on_click=fix_info)  
    else:
        st.markdown(f'''
            <p>
            <b>1. Username : </b>{sss.username}

            <b>2. Age : </b>{sss.age}

            <b>3. Gender : </b>{sss.gender}

            <b>4. Problem : </b>
            
            {sss.problem}

            <b>5. Problem Explanation : </b>
            
            {sss.problem_explanation}

            <b>6. Goal : </b>
            
            {sss.goal}
            </p>
            ''', unsafe_allow_html=True)   
with col3:
    if sss.fix_info==False:
        st.empty()
    else:
        with st.form('fix_user_info'):
            x=0
            st.write("**Now you can fix your info😊**")
            user_email = st.text_input('**Write down the new email address you want to use.**', key='new_user_email')
            def check_email(text):
                pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$'
                if not re.match(pattern, text):
                    st.error('Please give the correct email!')
                else:
                    if 'auth_email' not in sss:
                        sss.auth_email=True
            if user_email:
                check_email(user_email)
                if sss.auth_email==True:
                    x+=1
                    sss.user_email=user_email
                else:
                    pass
            email_check = st.text_input('**Please write the same email as above again.**',key='email_check')
            if email_check:
                if email_check!=sss.user_email:
                    st.error('That email is different from the one you just wrote down')
                if email_check==sss.user_email:
                    x+=1
            username = st.text_input('**Tell me the name you want to be called in here.**',key='new_username')
            if username:
                if username==st.secrets.user_name:
                    st.error('The username already exists.')
                if username==st.secrets.user_name_2:
                    st.error('This is the same username you were using before.')
                if username!=st.secrets.user_name and username!=st.secrets.user_name_2:
                    x+=1
                    sss.username=username
            problem = st.text_area("**What's your biggest problem right now?🤔**",key='new_problem')
            if problem:
                x+=1
                sss.problem=problem
            problem_explanation=st.text_area("**Please describe your issue in more detail. The more details you can provide, the better😊**",key='new_problem_explanation')
            if problem_explanation:
                x+=1
                sss.problem_explanation=problem_explanation
            goal=st.text_area("**Tell us what your end goal is!**",key='new_goal')
            if goal:
                x+=1
                sss.goal=goal
            if st.form_submit_button('**Submit**'):
                if x==6:
                    st.write('**Your user profile is fixed👍**')
                    time.sleep(2)
                    del sss.my_info
                    st.rerun()
                else:
                    st.write('**Please fill every blanks🙃**')