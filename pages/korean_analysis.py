import streamlit as st
from korean_menu import make_sidebar
from openai import OpenAI
import time
import pandas as pd
from streamlit import session_state as sss

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
make_sidebar()

def fix_info():
  sss.fix_info=True

if 'client' not in sss:
  sss.client = OpenAI(api_key=st.secrets['api_key'])

  
if 'username' not in sss:
   sss.username=st.secrets.user_name
   sss.age=st.secrets.age
   sss.gender=st.secrets.user_gender
   sss.problem=st.secrets.problem
   sss.problem_explanation=st.secrets.problem_explanation
   sss.goal=st.secrets.goal

if 'my_info' not in sss:
  with st.spinner('# 로딩중...'):
    problem_analysis = sss.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                  {
                    "role": "system",
                    "content": """Your role as a Korean professional psychotherapist is to score the extent to which the client's problem has improved given the information below and explain why.
                    
                    **Remember**:
                    1. Use Korean Language to answer my question.
                    2. Your score should be much lower than you think.
                    3. You should never speak rudely.
                    """
                  },
                  {
                    "role": "user",
                    "content": f"""
                    # My Request:
                    From a Korean professional psychotherapist's perspective, score the extent to which the client's problem is improved by the information given below and explain why.

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
                    - You need to use the form below to answer my request using Korean language.
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
                    1. Use Korean Language to answer my question.
                    2. Your score should be much lower than you think.
                    3. Don't use the word '고객' or '클라이언트'.
                    4. If you need to use the word '고객', don't use that word and replace it into the client's name with '님', such as {sss.username}님.
                    5. You should never speak rudely.
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
    st.markdown('<h4>내 정보</h4>',unsafe_allow_html=True)
    st.markdown(f'''
                <p>
                <b>1. 고객님 성함 : </b>{sss.username}

                <b>2. 연령 : </b>{sss.age}

                <b>3. 성별 : </b>{sss.gender}

                <b>4. 고민 : </b>
                
                {sss.problem}

                <b>5. 고민 설명 : </b>
                
                {sss.problem_explanation}

                <b>6. 목표 : </b>
                
                {sss.goal}
                </p>
                ''', unsafe_allow_html=True)  
    st.button('프로필 수정',use_container_width=True,on_click=fix_info)
  if sss.fix_info==True:
    st.title('프로필 수정')
    st.markdown(f'''
                <p>
                <b>1. 고객님 성함 : </b>{sss.username}

                <b>2. 연령 : </b>{sss.age}

                <b>3. 성별 : </b>{sss.gender}

                <b>4. 고민 : </b>{sss.problem}

                <b>5. 고민 설명 : </b>{sss.problem_explanation}

                <b>6. 목표 : </b>{sss.goal}
                </p>
                ''', unsafe_allow_html=True)  

with col3:
  if sss.fix_info==False:
    st.markdown(f"<p><h4>{time.localtime().tm_year}년 {time.localtime().tm_mon}월 {time.localtime().tm_mday}일의 분석 결과</h4></p>",unsafe_allow_html=True)
    st.markdown('<p><b>문제 분석 : </b></p>',unsafe_allow_html=True)
    st.write(f'{sss.client_analysis}')
    st.markdown(f'<p><b>해결 진전도 : </b>{sss.score}</p>',unsafe_allow_html=True)
    st.markdown('<p><b>채점 기준 : </b></p>',unsafe_allow_html=True)
    st.write(f'{sss.score_explanation}')
  else:
    with st.form('fix_user_info'):
      x=0
      st.write("**정보를 바꿔주세요😊**")
      username = st.text_input('**무슨 이름으로 불리고 싶으신가요?**')
      if username:
          x+=1
          sss.username=username
      problem = st.text_area("**당신을 가장 크게 괴롭히는 것이  무엇인가요?🤔**")
      if problem:
          x+=1
          sss.problem=problem
      problem_explanation=st.text_area("**문제점을 좀더 자세히 설명해주세요. 자세히 설명해주실수록 좋아요😊**")
      if problem_explanation:
          x+=1
          sss.problem_explanation=problem_explanation
      goal=st.text_area("**최종 목표가 무엇인지 말해주세요!**")
      if goal:
          x+=1
          sss.goal=goal
      if st.form_submit_button('**완료**'):
        if x==4:
          st.write('**저장 완료되었습니다👍**')
          time.sleep(1)
          del sss.my_info
          st.rerun()
        else:
          st.write('**빈칸을 전부 채워주세요🙃**')
if sss.fix_info==False:
  st.title('')
  st.markdown('<p><h4>도움이 될만한 행동들 : </h4></p>', unsafe_allow_html=True)
  for i in sss.what_to_do:
    st.markdown(f'<p>{i}</p>',unsafe_allow_html=True)
  st.title('')
  st.markdown('<p><h3><center>고민 해결도 그래프</center></h3></p>', unsafe_allow_html=True)
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
  if st.button('고객님의 정보를 이메일로 받아보시겠어요?',key='send_userinfo',use_container_width=True):
     st.write('hi')
else:
  pass

