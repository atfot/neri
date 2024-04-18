from openai import OpenAI
import streamlit as st
from korean_navigation import make_sidebar

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

make_sidebar()

if 'username' not in st.session_state:
   st.session_state.username=st.secrets.user_name
   st.session_state.age=st.secrets.age
   st.session_state.gender=st.secrets.user_gender
   st.session_state.gender=st.secrets.user_gender
   st.session_state.problem=st.secrets.problem
   st.session_state.problem_explanation=st.secrets.problem_explanation

if 'repeat' not in st.session_state:
    st.session_state.repeat = False

# functions
def reply_again_cb():
    st.session_state.repeat = True

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])

# variables
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]
    st.session_state['conversations']=[{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]
    st.session_state['message_summary'] = '아직까지 쓰인 내용은 없고, 여기서부터 대화내용이 시작됩니다.'

def main():

    # Print msg history.
    last_user_message = None
    for message in st.session_state.messages:

        # Print the user msg if it is not repeating successively.
        if (last_user_message is not None and
            message['role'] == 'user' and
            last_user_message == message["content"]
        ):
            pass
        else:
            # Print both msgs from user and assistant
            if msg['role']=="심리상담사":
                st.chat_message('assistant').write(message["content"])
            if msg['role']=="내담자":
                st.chat_message('user').write(message["content"])   

        # Backup last user msg used to identify successive same user content.
        if message['role'] == 'user':
            last_user_message = message["content"]

    if prompt := st.chat_input("enter your prompt") or st.session_state.repeat:

        # Get the last user prompt in the msg history.
        if st.session_state.repeat:
            prompt = st.session_state.messages[-2]['content']
            st.session_state.messages=st.session_state.messages[:-2]
            st.session_state.repeat = False  # reset
        else:
            # Only print the user msg if repeat is false.
            with st.chat_message("user"):
                st.markdown(prompt)

        # Always backup the conversation.
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=model,
                temperature=1,
                max_tokens=16,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )

            response = st.write_stream(stream)

        st.session_state.messages.append({"role": "assistant", "content": response})

        st.button('Give me another answwer', on_click=reply_again_cb)


if __name__ == '__main__':
    main()