from openai import OpenAI
import streamlit as st
from navigation import make_sidebar
import time

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

make_sidebar()
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Psychotherapist", "content": "What's bothering you? Tell me all about it."}]
    st.session_state['conversations']=[{"role": "Psychotherapist", "content": "What's bothering you? Tell me all about it."}]   

for msg in st.session_state.messages:
    if msg['role']=="Psychotherapist":
      st.chat_message('assistant').write(msg["content"])
    if msg['role']=="Mental patient":
      st.chat_message('user').write(msg["content"])   

if prompt := st.chat_input():
    client = OpenAI(api_key=st.secrets['api_key'])
    st.session_state.messages.append({"role": "Mental patient", "content": prompt})
    st.session_state.conversations.append({"role": "Mental patient", "content": prompt})
    st.chat_message("user").write(prompt)
    if len(st.session_state.messages)<3:
       st.session_state['message_summary'] = 'Nothing has been written to date, and the conversation starts below.'
    if len(st.session_state.messages)%3==0:
        summary = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
          {
            "role": "system",
            "content": "Please briefly summarize the conversation below."
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
      - Psychotherapist only expresses information from mentally ill person and himself indirectly
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
        # My requests
        - Please read the form below step by step and answer the questions in the exact form below

        - Read this step by step before filling out the form
        **Summary of the conversation**: [{st.session_state.message_summary}]
        **Conversation content**: [{st.session_state.conversations}]      

        - This is the form      
        '''
        **THINGS YOU NEED TO REMEMBER BEFORE THE ANSWER**:[Please write down the content below into the form.

        - Do not use line breaks or spaces.
        - If you get a short answer from the mental patient, ask him/her a related question.
        - Keep your responses between one and three sentences.
        - The best response should be sentences covered with quotes.
        - Never reuse answers that have already been used within a conversation.]

        **Three possible answers from a psychotherapist**: 
        [Given the above summary and the conversation, what are three possible answers a psychotherapist might give here?]

        **Best response**: 
        [Pick the best one from the "**Three possible answers from a psychotherapist**:" and write it down.]
        '''
        ```

        **REMEMBER**: 
        - You must write down "**THINGS YOU NEED TO REMEMBER BEFORE THE ANSWER**" into the form.
        - If you get a short answer from the mental patient, you must ask him/her a related question.
        - Never reuse answers that have already been used within a conversation.
    """
    
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
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
  temperature=0.1,
  max_tokens=512,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
    my_bar.progress(25,text=progress_text)
    msg = response.choices[0].message.content
    sentence_selection = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "system",
      "content": "Your role will be to help me pull out sentences within paragraphs."
    },
    {
      "role": "user",
      "content": f"""
Please only show the sentences from the '**Best response**:' section of what I provided below, with the quotes, or "" removed.
-  Keep in mind that you should not seek answers from the "**What should I consider for the best answer**:" part. 
- Submit only **sentences** as output. Never show "The best response would be:" or "The best response:" or anything resembles those. Only sentences are allowed as an output.

{msg}
"""
    }
  ],
  temperature=0.1,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    my_bar.progress(50,text=progress_text)
    new_msg = sentence_selection.choices[0].message.content.strip('"')
    humanize_sentence = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "system",
      "content": "Your job is to rephrase the sentences I give you."
    },
    {
      "role": "user",
      "content": f"""
In the paragraphs below, end the most important sentence with ".." or "...". Please use '?' or '!' for question marks or exclamation points as they are.

{new_msg}
"""
    }
  ],
  temperature=0.1,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    my_bar.progress(75,text=progress_text)
    humanize_msg = humanize_sentence.choices[0].message.content
    st.session_state.messages.append({"role": "Psychotherapist", "content": humanize_msg})
    st.session_state.conversations.append({"role": "Psychotherapist", "content": humanize_msg})
    my_bar.progress(100,text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.chat_message("assistant").write(humanize_msg)
    #st.chat_message("assistant").write(msg)
    #st.chat_message("assistant").write(user_prompt_1)
    #st.write(len(st.session_state.messages))
    #st.write(st.session_state.messages)
    #st.write(st.session_state.conversations)
