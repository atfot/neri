from openai import OpenAI
import streamlit as st


# variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if 'repeat' not in st.session_state:
    st.session_state.repeat = False


# functions
def reply_again_cb():
    st.session_state.repeat = True


def main():
    model = 'gpt-3.5-turbo'
    st.title(f"Chat with {model}")

    client = OpenAI(api_key=st.secrets["api_key"])

    for message in st.session_state.messages:
        if st.session_state.repeat == True:
            pass
        if st.session_state.repeat == False:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("enter your prompt") or st.session_state.repeat:

        # Get the last user prompt in the msg history.
        if st.session_state.repeat:
            prompt = st.session_state.messages[-2]['content']
            st.session_state.messages=st.session_state.messages[-2:]
            st.session_state.repeat = False  # reset
        if st.session_state.repeat==False:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

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