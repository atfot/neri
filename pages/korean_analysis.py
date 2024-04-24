import streamlit as st
from korean_navigation import make_sidebar
from openai import OpenAI

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
make_sidebar()

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])

st.session_state.analysis_request=False

if 'title' not in st.session_state:
    st.title('대화 분석')
col1,col2=st.columns([8,2])
with col2:
  if st.button('분석 요청',use_container_width=True):
      st.session_state.analysis_request=True
if st.session_state.analysis_request==True:
  problem_analysis = st.session_state.client.chat.completions.create(
              model="gpt-3.5-turbo-0125",
              messages=[
                {
                  "role": "system",
                  "content": """Your role as a Korean professional psychotherapist is to score the extent to which the client's problem has improved given the information below and explain why.
                  
                  **Remember**:
                  1. Use Korean Language to answer my question.
                  2. Your score should be much lower than you think.
                  """
                },
                {
                  "role": "user",
                  "content": f"""
                  # My Request:
                  From a Korean professional psychotherapist's perspective, score the extent to which the client's problem is improved by the information given below and explain why.

                  # Informations you need to know
                  - Client's Name: {st.session_state.username}
                  - Age: {st.session_state.age}
                  - Gender: {st.session_state.gender}
                  - Problem : {st.session_state.problem}
                  - Problem Explanation: {st.session_state.problem_explanation}

                  - Message summary : 
                  {st.session_state.message_summary}

                  - The latest conversations:
                  {st.session_state.conversations}
                
                  # Answer form
                  - You need to use the form below to answer my request using Korean language.
                  '''
                  Client Analysis : [Analyze the information I've given you by not using any bullet points.]

                  Score : [Based on the analysis you did, please score how well the client's problem was solved.]

                  Explanation : [Tell me how the score you gave me was based on your considerations.
                  *Scoring criteria*:
                  10 : The person's psychosis has been cured, or the client is no longer suffering from the problem.
                  9 : The person's mental illness is on the verge of being cured or the issue is on the verge of being completely resolved.
                  6 ~ 8 : The client is directly demonstrating a willingness to work toward a positive direction.
                  3 ~ 5 : The client is not directly demonstrating a willingness to move in a positive direction.
                  2 : The client is directly demonstrating a willingness to work toward a negative direction.
                  1 : The client has a serious mental illness or mental health issue and needs to see a real doctor or psychologist to address it.]

                  Best thing to do : [Tell me what you think is the best thing for the patient to do in that situation,using a bullet point summary, as a professional psychologist.]
                  '''
                  **Remember**:
                  1. Use Korean Language to answer my question.
                  2. Your score should be much lower than you think.
                  3. If you need to use the word '고객', replace it into the client's name.
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
  st.session_state.problem_analysis=problem_analysis
  problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
  client_analysis=problem_analysis[:problem_analysis.find('\n')]
  problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
  problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
  score=problem_analysis[:problem_analysis.find('\n')]
  problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
  problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
  score_explanation=problem_analysis[:problem_analysis.find('\n')]
  problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
  problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
  what_to_do=problem_analysis.split('\n')

  st.write(client_analysis)
  st.write(score)
  st.write(score_explanation)
  st.write(what_to_do)
  st.write(st.session_state.problem_analysis)
  #st.write(st.session_state.conversations)
  #st.write(st.session_state.message_summary)