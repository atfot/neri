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
    normal_korean = st.session_state.client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
          {
            "role": "system",
            "content": """Your role is to rephrase the Korean sentences into polite Korean sentences if there are any Korean grammar errors.
            
            **Remember**:
            1. If there is anything in the paragraph that is not a normal Korean sentence, such as "ㅋ" or "ㅠ" or similar, please remove it.  
            2. If there is a sentence in the paragraph below that contains a typo, such as "있으뮤ㅠㅠㅠ", please correct the sentence in the same way as "있음".
            3. If the paragraph below contains "전남친" or similar portmanteau, don't rephrase it.
            """
          },
          {
            "role": "user",
            "content": f"""
            # My Request:
            Please rephrase the paragraph below into polite Korean sentences.

            {prompt}

            **Remember**:
            1. If there is anything in the paragraph that is not a normal Korean sentence, such as "ㅋ" or "ㅠ" or similar, please remove it.  
            2. If there is a sentence in the paragraph below that contains a typo, such as "있으뮤ㅠㅠㅠ", please correct the sentence in the same way as "있음".
"""
          }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    try:
      normalized_korean = normal_korean.choices[0].message.content
      normalized_prompt = normalized_korean.index(':').strip('').strip('"')
    except:
       normalized_prompt = normal_korean.choices[0].message.content.strip('"')
    st.session_state.messages.append({"role": "내담자", "content": normalized_prompt})
    st.session_state.conversations.append({"role": "내담자", "content": normalized_prompt})
    st.chat_message("user").write(prompt)
    if len(st.session_state.messages)<3:
      st.session_state['message_summary'] = '아직까지 쓰인 내용은 없고, 여기서부터 대화내용이 시작됩니다.'
    if len(st.session_state.messages)%3==0:
        summary = st.session_state.client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
          {
            "role": "system",
            "content": "전달된 내용을 요약 정리해주세요."
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

      **REMEMBER**: 
      '''
      - Psychotherapist cannot speak information from mentally ill person and himself unless it's really necessary.
      - Keep in mind that the psychotherapist's response is part of the conversation and will be followed by the mentally ill person's response
      - The psychotherapist's response should fit the tone and content of the conversation
      - If mental patient's reply is too short, you need to ask some questions to understand what is going on inside his/her mind
      - The psychotherapist is talking to only one person with a mental illness(Check the "# Character information")
      - If you get a short answer from the mental patient, ask him/her a related question.
      - Never reuse any sentences that has a same context which have already been used within a conversation.
      - The grammar of the sentences should be perfect.
      - If you get any questions from the mental patient, give him/her an answer.
      - Never use a tone that suggests you want to do something with the patient.
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
        
        - This is the form      
        '''
        **Three possible answers from a korean psychotherapist, written in Korean language**: 
        [Given the above summary and the conversation, what are 3 possible answers a psychotherapist might give here?]
        '''
        
        **REMEMBER**: 
        - Never use a tone that suggests you want to do something with the patient.
        - If you get a short answer from the mental patient, ask him/her a related question.
        - Never reuse any sentences that has a same context which have already been used within a conversation.
        - The grammar of the sentences should be perfect.
        - If you get any questions from the mental patient, give him/her an answer.
        ```

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
  top_p=0.9,
  frequency_penalty=1,
  presence_penalty=1
)
    my_bar.progress(25,text=progress_text)
    msg = response.choices[0].message.content
    sentence_selection = st.session_state.client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "system",
      "content": """Your role is to read the dialogue, summary, and examples of the three answers and choose the best sentence from the three.
      
      **REMEMBER**:
      1. Never attach embellishments or explanation to your answers. Submit only **context** as output. That means **there should be no "" marks in your answer, and no : or - marks to show the answer.** And don't use any words or phrases other than the sentence you chose from the three examples.
      2. Never choose the sentence that contains 'How does it feel' or anything resembles that.
      """
    },
    {
      "role": "user",
      "content": f"""
      # My request:
      Read the summary, dialogue, and examples of the three answers and choose the best sentence from the three. Lets go step by step-

      - Read these informations carefully before answering my question.
        **Summary of the conversation**: [{st.session_state.message_summary}]
        
        **Conversation content**: [{st.session_state.conversations}]

        **Three possible answers from a korean psychotherapist who wants to know about his patient and heal the patient's mind**: 
        "[{msg}]"

      - After reading the informations above, please **pick the best response from three possible answers** and write it down exactly, without leaving out a single letter. 
        
      **REMEMBER**:
      1. After you pick the best response, then write it down exactly, without leaving out a single letter.
      2. Never attach embellishments or explanation to your answers. Submit only **context** as output. That means **there should be no "" marks in your answer, and no : or - marks to show the answer.** And don't use any words or phrases other than the sentence you chose from the three examples.
      3. Never choose the sentence that contains 'How does it feel' or anything resembles that.]
"""
    }
  ],
  temperature=1,
  max_tokens=1028,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
    my_bar.progress(50,text=progress_text)
    selected_msg = sentence_selection.choices[0].message.content.strip('"')
    humanize_sentence = st.session_state.client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "system",
      "content": """Your role is to check the korean grammar of the korean sentences and rephrase it if it has any wrong grammars, or if it is too rude.
      
      **REMEMBER**:
      1. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
      2. Submit the original sentences that I gave you if there is no grammar problem.
      3. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
      4. Don't use any words or phrases other than the context.
      """
    },
    {
      "role": "user",
      "content": f"""
      # My request:
      Check the korean grammar of the korean sentences below and rephrase it if it has any wrong grammars, or if it is too rude.

      [{selected_msg}]
        
        **REMEMBER**:
        1. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
        2. Submit the original sentences that I gave you if there is no grammar problem.
        3. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
        4. Don't use any words or phrases other than the context.
"""
    }
  ],
  temperature=1,
  max_tokens=1028,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
    try:
      humanize_msg = sentence_selection.choices[0].message.content
      humanize_msg = humanize_msg.index(':').strip('').strip('"')
    except:
       humanize_msg = sentence_selection.choices[0].message.content.strip('"')
    st.session_state.messages.append({"role": "심리상담사", "content": humanize_msg})
    st.session_state.conversations.append({"role": "심리상담사", "content": humanize_msg})
    my_bar.progress(100,text=progress_text)
    my_bar.empty()
    st.write('최종 메세지:')
    st.chat_message("assistant").write(humanize_msg)
    st.write('유저 메세지 변환: ')
    st.chat_message("assistant").write(normalized_prompt)
    st.write('1차 메세지:')
    st.chat_message("assistant").write(msg)
    #st.write('1차 프롬프트:')
    #st.chat_message("assistant").write(user_prompt_1)
    #st.write('저장 대화 갯수:')
    #st.write(len(st.session_state.messages))
    #st.write('저장 메세지:')
    #st.write(st.session_state.messages)
    #st.write('최근 메세지:')
    #st.write(st.session_state.conversations)