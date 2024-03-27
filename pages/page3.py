from openai import OpenAI
import streamlit as st
from navigation import make_sidebar
import time
import re

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

make_sidebar()
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Psychotherapist", "content": "What's bothering you? Tell me all about it."}]

for msg in st.session_state.messages:
    if msg['role']=="Psychotherapist":
      st.chat_message('assistant').write(msg["content"])
    if msg['role']=="Mental patient":
      st.chat_message('user').write(msg["content"])   

if prompt := st.chat_input():
    client = OpenAI(api_key=st.secrets['api_key'])
    st.session_state.messages.append({"role": "Mental patient", "content": prompt})
    st.chat_message("user").write(prompt)
    ###st.write(len(st.session_state.messages)%6)
    if len(st.session_state.messages)%6==0:
        response = client.chat.completions.create(
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
        st.session_state['message_summary'] = response.choices[0].message.content
        st.session_state['conversations'] = st.session_state.messages[len(st.session_state.messages)-3:]
    if len(st.session_state.messages)%6!=0:
       st.session_state['message_summary'] = 'Nothing has been written to date, and the conversation starts below.'
       st.session_state['conversations'] = st.session_state.messages
    with st.spinner('thinking...'):
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
        - The psychotherapist is talking to only one person with a mental illness(Check the "# Character information")
        - The mentally ill person could give extremely short answers to the psychotherapist because they are talking online, so psychotherapist must continue the conversation considering the previous conversations.
        - Make sure you understand the content of "# Information about the play" and "# Character information" before answering
        '''
        ```
    """
      user_prompt=f"""
          ```
          # My requests
          - Please read this conversation step by step and respond in the form below.
          - Summary of the conversation: {st.session_state.message_summary}
          - Conversation content: {st.session_state.conversations}

          '''                  
          **Three psychotherapist's responses**: 
          [Given the above conversation, what are the 3 correct responses from the psychotherapist?]

          **Best response**: 
          [1 best response given the above conversation(Show the content by enclosing it in " ", like "the context of Best response". Never attach any descriptions or platitudes to this part except for the result sentence.)]

          **Why the best response was chosen**: 
          [Why the response selected in **Best response** is the most correct response]
          '''

          **REMEMBER**: Use this form below. **DO NOT USE LINE BREAKS OR SPACES** that are not depicted in the form below.
          ```
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
        "content": f"{user_prompt}"
      }
    ],
    temperature=0.2,
    max_tokens=1024,
    top_p=0.2,
    frequency_penalty=0.1,
    presence_penalty=0.1
  )
      time.sleep(1)
      msg = response.choices[0].message.content
      st.chat_message("assistant").write(msg)
      response = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
      {
        "role": "system",
        "content": "Your role will be to help me pull out sentences within paragraphs."
      },
      {
        "role": "user",
        "content": f"""
Please only show the sentences from the '**Best response**:' section of what I provided below, with the quotes removed. Keep in mind that you should not seek answers from the "**Why the best response was chosen**:" part.

{msg}
"""
      }
    ],
    temperature=0.1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
      
      new_msg = response.choices[0].message.content.strip('"')
      st.session_state.messages.append({"role": "Psychotherapist", "content": new_msg})
      st.chat_message("assistant").write(new_msg)
      st.write(len(st.session_state.messages))
      st.write(st.session_state.messages)
      
        
