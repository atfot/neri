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
    layout="wide"
)
make_sidebar()

def fix_info():
  sss.fix_info=True

if 'client' not in sss:
  sss.client = OpenAI(api_key=st.secrets['api_key'])

if 'username' not in sss:
   sss.username=st.secrets.user_name_2
   sss.age=st.secrets.age_2
   sss.gender=st.secrets.user_gender_2
   sss.problem=st.secrets.problem_2
   sss.problem_explanation=st.secrets.problem_explanation_2
   sss.goal=st.secrets.goal_2

if 'my_info' not in sss:
  with st.spinner('# Now Loading...'):
    problem_analysis = sss.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                  {
                    "role": "system",
                    "content": """Your role as a professional psychotherapist is to score the extent to which the client's problem has improved given the information below and explain why.
                    
                    **Remember**:
                    1. Your score should be much lower than you think.
                    2. You should never speak rudely.
                    """
                  },
                  {
                    "role": "user",
                    "content": f"""
                    # My Request:
                    From a professional psychotherapist's perspective, score the extent to which the client's problem is improved by the information given below and explain why.

                    # Informations you need to know
                    - Client's Name : {sss.username}
                    - Age : {sss.age}
                    - Gender : {sss.gender}
                    - Problem : {sss.problem}
                    - Problem Explanation : {sss.problem_explanation}
                    - Goal : {sss.goal}

                    - Message summary : 
                    {sss.message_summary}

                    - The latest conversations:
                    {sss.conversations}
                  
                    # Answer form
                    - You need to use the form below to answer my request.
                    '''
                    Analysis : [Analyze the information I've given you by not using any bullet points.]

                    Score : [Based on the analysis you did, please score how well the {sss.username}'s problem was solved.]

                    Explanation : [Tell me how the score you gave me was based on your considerations.
                    *Scoring criteria*:
                    10 : The person's psychosis has been cured, or the client is no longer suffering from the problem.
                    9 : The person's mental illness is on the verge of being cured or the issue is on the verge of being completely resolved.
                    6 ~ 8 : The client is directly demonstrating a willingness to work toward a positive direction.
                    3 ~ 5 : The client is not directly demonstrating a willingness to move in a positive direction.
                    2 : The client is directly demonstrating a willingness to work toward a negative direction.
                    1 : The client has a serious mental illness or mental health issue and needs to see a real doctor or psychologist to address it.]

                    Best thing to do : [Tell me what you think is the easiest thing for {sss.username} to do in that situation, using a bullet point summary, as a professional psychologist.]
                    '''
                    **Remember**:
                    1. Your score should be much lower than you think.
                    2. Don't use the word 'client'.
                    3. If you need to use the word 'client', don't use that word and replace it into the client's name, such as {sss.username}.
                    4. You should never speak rudely.
        """
                  }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )    
    problem_analysis = problem_analysis.choices[0].message.content
    problem_analysis=problem_analysis.strip().strip("'''")
    sss.problem_analysis=problem_analysis
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    sss.client_analysis=problem_analysis[:problem_analysis.find('\n')].replace('. ','.\n\n')
    problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    sss.score=problem_analysis[:problem_analysis.find('\n')]
    problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    sss.score_explanation=problem_analysis[:problem_analysis.find('\n')].replace('. ','.\n\n')
    problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    sss.what_to_do=problem_analysis.split('\n')
    sss.my_info=True
    sss.fix_info=False

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
  if sss.fix_info==True:
    st.title('Fix your Profile')      
    st.markdown(f'''
                <p>
                <b>1. Username : </b>{sss.username}

                <b>2. Age : </b>{sss.age}

                <b>3. Gender : </b>{sss.gender}

                <b>4. Problem : </b>{sss.problem}

                <b>5. Problem Explanation : </b>{sss.problem_explanation}

                <b>6. Goal : </b>{sss.goal}
                </p>
                ''', unsafe_allow_html=True)   
with col3:
    if sss.fix_info==False:
        month=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month=month[time.localtime().tm_mon-1]
        sss.date=f'{month} {time.localtime().tm_mday}, {time.localtime().tm_year}'
        st.markdown(f'<p><h4>Analysis results on {sss.date}</h4></p>', unsafe_allow_html=True)
        st.markdown('<p><b>Problem Analysis :</b></p>', unsafe_allow_html=True)
        st.write(f'{sss.client_analysis}')
        st.markdown(f'<p><b>Score : </b>{sss.score}</p>', unsafe_allow_html=True)
        st.markdown('<p><b>Score Explanation :</b></p>', unsafe_allow_html=True)
        st.write(f'{sss.score_explanation}')
    else:
        with st.form('fix_user_info'):
            x=0
            st.write("**Now you can fix your info😊**")
            user_email = st.text_input('**Write down the new email address you want to use.**', key='new_user_email')
            def check_email(text):
                pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$'
                if re.match(pattern, text):
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
if sss.fix_info==False:
    st.title('')
    st.markdown('<p><h4>Actions that might help you :</h4></p>', unsafe_allow_html=True)
    for i in sss.what_to_do:
        st.write(i)
    st.title('')
    st.markdown('<p><h3><center>Problem Resolution Graph</center></h3></p>', unsafe_allow_html=True)
    if time.localtime().tm_mon<10:
        z=f'0{time.localtime().tm_mon}'
    else:
        z=f'{time.localtime().tm_mon}'
    y=f'{time.localtime().tm_year}/{z}/{time.localtime().tm_mday}'
    df = pd.DataFrame({y: [sss.score]})
    x=6
    y='2025/12/03'
    df_1=pd.DataFrame({y: [x]})
    df_2=pd.concat([df,df_1],axis=1).T
    st.line_chart(df_2)
if sss.fix_info==True:
    pass  
