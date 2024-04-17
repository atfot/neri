from openai import OpenAI
import streamlit as st
import time

st.set_page_config(
    page_title="Some AI website",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi! How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message('assistant').write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    progress_text='thinking...'
    my_bar=st.progress(0,text=progress_text)
    
    system_prompt='Some weird prompt'
    
    user_prompt_1="also some weird prompt"
    
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
    my_bar.progress(75,text=progress_text)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    my_bar.progress(100,text=progress_text)
    my_bar.empty()
    
    col1,col2=st.columns([9,1])
    with col1:
      st.chat_message("assistant").write(msg)
      if 'reset_response' not in st.session_state:
        st.write('not sure')
      if 'reset_response' in st.session_state:
         st.write('maybe')
    with col2:
       if st.button('🔄'):
          st.session_state.reset_response=True
