from openai import OpenAI
import streamlit as st
from korean_navigation import make_sidebar
import time

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])

make_sidebar()

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]
    st.session_state['conversations']=[{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]

for msg in st.session_state.messages:
    if msg['role']=="심리상담사":
      st.chat_message('assistant').write(msg["content"])
    if msg['role']=="내담자":
      st.chat_message('user').write(msg["content"])   

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "내담자", "content": prompt})
    st.session_state.conversations.append({"role": "내담자", "content": prompt})
    st.chat_message("user").write(prompt)
    if len(st.session_state.messages)<3:
      st.session_state['message_summary'] = '아직까지 쓰인 내용은 없고, 여기서부터 대화내용이 시작됩니다.'
    if len(st.session_state.messages)%3==0:
        summary = st.session_state.client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
          {
            "role": "system",
            "content": "최대한 짧고 간략하게 내용을 요약 정리해주세요."
          },
          {
            "role": "user",
            "content": f"{st.session_state.messages}"
          }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        st.session_state['message_summary'] = summary.choices[0].message.content
        st.session_state['conversations'] = st.session_state.messages[-3:]
    progress_text='thinking...'
    my_bar=st.progress(0,text=progress_text)
    system_prompt=f"""```
      # Primary Assistant Guidance
      Your goal is to help me, the playwright, write a script for a play. Let's go step-by-step:

      # Information about the play
      - Conversation between one mentally ill person and one psychotherapist
      - The two are now meeting and talking online
      - Psychologist uses the most respectful tone of voice possible, and the person with mental illness prefers it
      - Person with mental illness want empathy and comfort for him/herself
      - The psychotherapist wants to heal the mentally ill person by building a strong relationship with them

      # Character information
      1. mentally ill person
      - Name: {st.secrets['user_name']}
      - Age: {st.secrets['age']}
      - Gender: {st.secrets['user_gender']}
      - Place of Origin : {st.secrets['nationality']}
      - City of residence: {st.secrets['city']}

      2. psychological counselor
      - Name : Neri
      - Age : 55 years old
      - Gender: Male
      - Country of Origin : South Korea
      - City of residence : Seoul
      - Characteristics : Neri knows the information of {st.secrets['user_name']}, a mentally ill person, and conducts psychotherapy based on it

      # Things to know before writing
      '''
      - Psychotherapists can indirectly express information about the mentally ill person and themselves
      - Keep in mind that the psychotherapist's response is part of the conversation and will be followed by the mentally ill person's response
      - The psychotherapist's response should fit the tone and content of the conversation
      - If mental patient's reply is too short, you need to ask some questions to understand what is going on inside his/her mind
      - The psychotherapist is talking to only one person with a mental illness(Check the "# Character information")
      - Make sure you understand the content of "# Information about the play" and "# Character information" before answering
      '''
      ```
  """
    
    user_prompt_1=f"""
        ```
        # My requests: 
        Your goal is to help me, the playwright, write a script for a play. Let's go step-by-step:
        - Please read the form below step by step and answer the questions in the exact form below

        - Read this step by step before filling out the form
        **Summary of the conversation**: [{st.session_state.message_summary}]
        **Latest Conversations**: [{st.session_state.conversations}]      
        
        **THINGS YOU NEED TO REMEMBER BEFORE THE ANSWER**:
        - Do not use line breaks or spaces.
        - If you get a short answer from the mental patient, ask him/her a related question.
        - Keep your responses below three sentences.
        - Never reuse answers that have already been used within a conversation.

        - This is the form      
        '''
        **Best possible answer from a korean psychotherapist, written in Korean language**: 
        [Given the above summary and the conversation, what are the best possible answer a psychotherapist might give here?]
        '''
        ```

        **REMEMBER**: 
        - Never reuse answers that have already been used within a conversation.
        - If you get a short answer from the
         mental patient, you must ask him/her a related question.
    """
    
    response = st.session_state.client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "system",
      "content": f"{system_prompt}"
    },
    {
      "role": "user",
      "content": f"{user_prompt_1}"
    }
  ],
  temperature=1,
  max_tokens=1028,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
    my_bar.progress(25,text=progress_text)
    msg = response.choices[0].message.content.strip('"')
    humanize_sentence = st.session_state.client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "system",
      "content": """Your role is to check the korean grammar of the korean sentences and rephrase it if it has any wrong grammars.
      
      **REMEMBER**:
      1. Never attach embellishments or explanation to your answers. Submit only **context** as output. That means **there should be no "" marks in your answer, and no : or - marks to show the answer.** And don't use any words or phrases other than the context.
      2. Submit the original sentences that I gave you if there is no grammar problem.
      """
    },
    {
      "role": "user",
      "content": f"""
      # My request:
      Check the korean grammar of the korean sentences below and rephrase it if it has any wrong grammars.

      [{msg}]
        
        **REMEMBER**:
        1. Never attach embellishments or explanation to your answers. Submit only **context** as output. That means **there should be no "" marks in your answer, and no : or - marks to show the answer.** And don't use any words or phrases other than the context.
        2. Submit the original sentences that I gave you if there is no grammar problem.
"""
    }
  ],
  temperature=1,
  max_tokens=1028,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
    humanize_msg = humanize_sentence.choices[0].message.content.strip('"')
    st.session_state.messages.append({"role": "심리상담사", "content": humanize_msg})
    st.session_state.conversations.append({"role": "심리상담사", "content": humanize_msg})
    my_bar.progress(100,text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.chat_message("assistant").write(humanize_msg)
    st.chat_message("assistant").write(msg)
    
    st.chat_message("assistant").write(user_prompt_1)
    st.write(len(st.session_state.messages))
    st.write(st.session_state.messages)
    st.write(st.session_state.conversations)
