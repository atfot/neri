import streamlit as st
from korean_navigation import make_sidebar
from openai import OpenAI
import time

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed"
)
make_sidebar()

def fix_info():
  st.session_state.fix_info=True

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])

if 'my_info' not in st.session_state:
  with st.spinner('# 로딩중...'):
    problem_analysis = st.session_state.client.chat.completions.create(
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

                    Best thing to do : [Tell me what you think is the best thing for {st.session_state.username} to do in that situation,using a bullet point summary, as a professional psychologist.]
                    '''
                    **Remember**:
                    1. Use Korean Language to answer my question.
                    2. Your score should be much lower than you think.
                    3. Don't use the word '고객' or '클라이언트'.
                    4. If you need to use the word '고객', don't use that word and replace it into the client's name with '님', such as {st.session_state.username}님.
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
    st.subheader('내 정보')
    st.write(f"""
  1. 고객님 성함: {st.session_state.username}
              
  2. 연령: {st.session_state.age}

  3. 성별: {st.session_state.gender}

  4. 고민 : {st.session_state.problem}

  5. 고민 설명: {st.session_state.problem_explanation}

  6. 목표 : {st.session_state.goal}"""
  )  
    st.button('프로필 수정',use_container_width=True,on_click=fix_info)
  if st.session_state.fix_info==True:
    st.title('프로필 수정')
    st.write(f"""
  1. 고객님 성함: {st.session_state.username}
              
  2. 연령: {st.session_state.age}

  3. 성별: {st.session_state.gender}

  4. 고민 : {st.session_state.problem}

  5. 고민 설명: {st.session_state.problem_explanation}

  6. 목표 : {st.session_state.goal}"""
  )  
with col3:
  if st.session_state.fix_info==False:
    st.subheader(f"{time.localtime().tm_year}년 {time.localtime().tm_mon}월 {time.localtime().tm_mday}일의 분석 결과")
    st.write(f'문제 분석 : {st.session_state.client_analysis}')
    st.write(f'해결 진전도 : {st.session_state.score}')
    st.write(f'채점 기준 : {st.session_state.score_explanation}')
  else:
    with st.form('fix_user_info'):
      st.write("정보를 바꿔주세요!")
      username = st.text_input('무슨 이름으로 불리고 싶으신가요?')
      if username:
          x+=1
          st.session_state.username=username
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
      if st.form_submit_button('완료'):
        if x==4:
          st.write('저장 완료되었습니다!')
          time.sleep(2)
          del st.session_state.my_info
          st.rerun()
if st.session_state.fix_info==False:
  st.title('')
  st.write('도움이 될만한 행동들 : ')
  for i in st.session_state.what_to_do:
    st.write(i)
else:
  pass

