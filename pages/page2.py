import streamlit as st
from korean_navigation import make_sidebar

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
make_sidebar()

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])
  
if 'title' not in st.session_state:
    st.title('Hi')
if st.button('show the message'):
    problem_analysis = st.session_state.client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=[
            {
              "role": "system",
              "content": """Your role as a Korean professional psychotherapist is to score the extent to which the patient's problem has improved given the information below and explain why.
              
              **Remember**:
              1. Use Korean Language to answer my question
              """
            },
            {
              "role": "user",
              "content": f"""
              # My Request:
              From a Korean professional psychotherapist's perspective, score the extent to which the patient's problem is improved by the information given below and explain why.

              # Informations you need to know
              - Patient's Name: {st.session_state.username}
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
              Patient Analysis : [Analyze the information I've given you.]

              Score : [Based on the analysis you did, please score how well the patient's problem was solved.]

              Explanation : [Tell me how the score you gave me was based on your considerations.
              *Scoring criteria*:
              10 : The person's psychosis has been cured, or the patient is no longer suffering from the problem.
              9 : The person's mental illness is on the verge of being cured or the issue is on the verge of being completely resolved.
              6 ~ 8 : The patient is directly demonstrating a willingness to work toward a positive direction.
              3 ~ 5 : The patient is not directly demonstrating a willingness to move in a positive direction.
              2 : The patient is directly demonstrating a willingness to work toward a negative direction.
              1 : The person has a serious mental illness or mental health issue and needs to see a real doctor or psychologist to address it.]

              Best thing to do : [Tell me what you think is the best thing for the patient to do in that situation,using a bullet point summary, as a professional psychologist.]
              '''
              **Remember**:
              1. Use Korean Language to answer my question
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
    st.write(problem_analysis)
    st.write(st.session_state.conversations)
    st.write(st.session_state.message_summary)