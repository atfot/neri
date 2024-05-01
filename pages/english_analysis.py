import streamlit as st
from english_menu import make_sidebar
from openai import OpenAI
import pandas as pd
import time

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
make_sidebar()
st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

.st-emotion-cache-10trblm {
	font-family: 'Beeunhye';
	font-size: 1.75em;
}       
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-1yycg8b.e1f1d6gn3 > div > div > div > div:nth-child(3) > div > div > p{
	font-family: 'Beeunhye';
	font-size: 1.75em;
}     
            
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
}     
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-1yycg8b.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
}     
            
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div > p > b {
	font-family: 'Beeunhye';
	font-size: 1.75em;
}     
            
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
}     

            
div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div > div > div > ul > li {
	font-family: 'Beeunhye';
	font-size: 2em;
}
            
</style>
""", unsafe_allow_html=True)
def fix_info():
  st.session_state.fix_info=True

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])

if 'username' not in st.session_state:
   st.session_state.username=st.secrets.user_name_2
   st.session_state.age=st.secrets.age_2
   st.session_state.gender=st.secrets.user_gender_2
   st.session_state.problem=st.secrets.problem_2
   st.session_state.problem_explanation=st.secrets.problem_explanation_2
   st.session_state.goal=st.secrets.goal_2

if 'my_info' not in st.session_state:
  with st.spinner('# Now Loading...'):
    problem_analysis = st.session_state.client.chat.completions.create(
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
                    - Client's Name : {st.session_state.username}
                    - Age : {st.session_state.age}
                    - Gender : {st.session_state.gender}
                    - Problem : {st.session_state.problem}
                    - Problem Explanation : {st.session_state.problem_explanation}
                    - Goal : {st.session_state.goal}

                    - Message summary : 
                    {st.session_state.message_summary}

                    - The latest conversations:
                    {st.session_state.conversations}
                  
                    # Answer form
                    - You need to use the form below to answer my request using Korean language.
                    '''
                    Analysis : [Analyze the information I've given you by not using any bullet points.]

                    Score : [Based on the analysis you did, please score how well the {st.session_state.username}'s problem was solved.]

                    Explanation : [Tell me how the score you gave me was based on your considerations.
                    *Scoring criteria*:
                    10 : The person's psychosis has been cured, or the client is no longer suffering from the problem.
                    9 : The person's mental illness is on the verge of being cured or the issue is on the verge of being completely resolved.
                    6 ~ 8 : The client is directly demonstrating a willingness to work toward a positive direction.
                    3 ~ 5 : The client is not directly demonstrating a willingness to move in a positive direction.
                    2 : The client is directly demonstrating a willingness to work toward a negative direction.
                    1 : The client has a serious mental illness or mental health issue and needs to see a real doctor or psychologist to address it.]

                    Best thing to do : [Tell me what you think is the easiest thing for {st.session_state.username} to do in that situation, using a bullet point summary, as a professional psychologist.]
                    '''
                    **Remember**:
                    1. Your score should be much lower than you think.
                    2. Don't use the word 'client'.
                    3. If you need to use the word 'client', don't use that word and replace it into the client's name, such as {st.session_state.username}.
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
    st.session_state.problem_analysis=problem_analysis
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    st.session_state.client_analysis=problem_analysis[:problem_analysis.find('\n')].replace('. ','.\n\n')
    problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    st.session_state.score=problem_analysis[:problem_analysis.find('\n')]
    problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    st.session_state.score_explanation=problem_analysis[:problem_analysis.find('\n')].replace('. ','.\n\n')
    problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
    problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
    st.session_state.what_to_do=problem_analysis.split('\n')
    st.session_state.my_info=True
    st.session_state.fix_info=False

col1,col2,col3=st.columns([4,1,5])
with col1:
  if st.session_state.fix_info==False:
    st.write('')
    st.subheader('Your Profile')
    st.markdown(f'''
                <p>
                <b>1. Your Name : </b>{st.session_state.username}

                <b>2. Age : </b>{st.session_state.age}

                <b>3. Gender : </b>{st.session_state.gender}

                <b>4. Problem : </b>
                
                {st.session_state.problem}

                <b>5. Problem Explanation : </b>
                
                {st.session_state.problem_explanation}

                <b>6. Goal : </b>
                
                {st.session_state.goal}
                </p>
                ''', unsafe_allow_html=True)   
    st.button('Fix my Info',use_container_width=True,on_click=fix_info)
  if st.session_state.fix_info==True:
    st.title('Fix your Profile')      
    st.markdown(f'''
                <p>
                <b>1. Your Name : </b>{st.session_state.username}

                <b>2. Age : </b>{st.session_state.age}

                <b>3. Gender : </b>{st.session_state.gender}

                <b>4. Problem : </b>{st.session_state.problem}

                <b>5. Problem Explanation : </b>{st.session_state.problem_explanation}

                <b>6. Goal : </b>{st.session_state.goal}
                </p>
                ''', unsafe_allow_html=True)   
with col3:
  if st.session_state.fix_info==False:
    month=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month=month[time.localtime().tm_mon-1]
    st.markdown(f'<p><h4>Analysis results on {month} {time.localtime().tm_mday}, {time.localtime().tm_year}</h4></p>', unsafe_allow_html=True)
    st.markdown('<p><b>Problem Analysis :</b></p>', unsafe_allow_html=True)
    st.write(f'{st.session_state.client_analysis}')
    st.markdown(f'<p><b>Score : </b>{st.session_state.score}</p>', unsafe_allow_html=True)
    st.markdown('<p><b>Score Explanation :</b></p>', unsafe_allow_html=True)
    st.write(f'{st.session_state.score_explanation}')
  else:
    with st.form('fix_user_info'):
      x=0
      st.write("Now you can fix your info😊")
      username = st.text_input('Tell me the name you want to be called in here.')
      if username:
          x+=1
          st.session_state.username=username
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
      if st.form_submit_button('Submit'):
        if x==4:
          st.write('Your user profile is fixed👍')
          time.sleep(2)
          del st.session_state.my_info
          st.rerun()
        else:
          st.write('Please fill every blanks🙃')
if st.session_state.fix_info==False:
  st.title('')
  st.markdown('<p><b>Actions that might help you :</b></p>', unsafe_allow_html=True)
  for i in st.session_state.what_to_do:
    st.write(i)
  st.title('')
  st.markdown('<p><h3><center>Problem Resolution Graph</center></h3></p>', unsafe_allow_html=True)
  if time.localtime().tm_mon<10:
      z=f'0{time.localtime().tm_mon}'
  else:
      z=f'{time.localtime().tm_mon}'
  y=f'{time.localtime().tm_year}/{z}/{time.localtime().tm_mday}'
  df = pd.DataFrame({y: [st.session_state.score]})
  x=6
  y='2025/12/03'
  df_1=pd.DataFrame({y: [x]})
  df_2=pd.concat([df,df_1],axis=1).T
  st.line_chart(df_2)
else:
  pass

  #st.write(st.session_state.problem_analysis)
  #st.write(st.session_state.conversations)
  #st.write(st.session_state.message_summary)