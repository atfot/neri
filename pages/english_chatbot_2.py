from openai import OpenAI
import streamlit as st
from navigation import make_sidebar

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
make_sidebar()

if 'client' not in st.session_state:
  st.session_state.client = OpenAI(api_key=st.secrets['api_key'])

if 'username' not in st.session_state:
   st.session_state.username=st.secrets.user_name
   st.session_state.age=st.secrets.age
   st.session_state.gender=st.secrets.user_gender
   st.session_state.gender=st.secrets.user_gender
   st.session_state.problem=st.secrets.problem
   st.session_state.problem_explanation=st.secrets.problem_explanation

# variables
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Psychotherapist", "content": "What's bothering you?"}]
    st.session_state['conversations']=[{"role": "Psychotherapist", "content": "What's bothering you?"}]   
    st.session_state['message_summary'] = 'Nothing has been written to date, and the conversation starts below.'

if 'repeat' not in st.session_state:
    st.session_state.repeat = False

# functions
def reply_again_cb():
    st.session_state.repeat = True

if st.session_state.repeat==True:
    st.session_state.messages=st.session_state.messages[:-1]

def main():

    # Print msg history.
    last_user_message = None
    for message in st.session_state.messages:

        # Print the user msg if it is not repeating successively.
        if (last_user_message is not None and
            message['role'] == "Psychotherapist" and
            last_user_message == message["content"]
        ):
            pass
        else:
            # Print both msgs from user and assistant
            if message['role']=="Psychotherapist":
                st.chat_message('assistant').write(message["content"])
            if message['role']=="Mental patient":
                st.chat_message('user').write(message["content"])

        # Backup last user msg used to identify successive same user content.
        if message['role'] == "Mental patient":
            last_user_message = message["content"]

    if prompt := st.chat_input("Bring out your worries, your feelings, and the things you've never told anyone.") or st.session_state.repeat:
        def text_logic():
            if st.session_state.repeat==True:
                pass
            else:
                st.session_state.messages.append({"role": "Mental patient", "content": prompt})
                st.session_state.conversations.append({"role": "Mental patient", "content": normalized_prompt})
            if len(st.session_state.messages)%3==0:
                summary = st.session_state.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
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
                - Name: {st.session_state.username}
                - Age: {st.session_state.age}
                - Gender: {st.session_state.gender}
                - Problem : {st.session_state.problem}
                - Problem Explanation: {st.session_state.problem_explanation}

                2. psychological counselor
                - Name : Neri
                - Age : 55 years old
                - Gender: Male
                - Country of Origin : South Korea
                - City of residence : Seoul
                - Characteristics : Neri knows the information of {st.session_state.username}, a mentally ill person, and conducts psychotherapy based on it

                **REMEMBER**: 
                '''
                - Psychotherapist cannot speak information from mentally ill person and himself unless it's really necessary.
                - Keep in mind that the psychotherapist's response is part of the conversation and will be followed by the mentally ill person's response
                - The psychotherapist's response should fit the tone and content of the conversation
                - If mental patient's reply is too short, you need to ask some questions to understand what is going on inside his/her mind
                - The psychotherapist is talking to only one person with a mental illness(Check the "# Character information")
                - If you get a short answer from the mental patient, ask him/her a related question.
                - Never use a tone that suggests you want to do something with the patient.
                - If you get a short answer from the mental patient, ask him/her a related question.
                - Never reuse any sentences that has a same context which have already been used within a conversation.
                - If you get any questions from the mental patient, give him/her an answer.
                - The grammar of the sentences should be perfect.
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
                **Three possible answers from a psychotherapist**: 
                [Given the above summary and the conversation, what are 3 possible answers a psychotherapist might give here?]
                '''
                
                **REMEMBER**: 
                - Never use a tone that suggests you want to do something with the patient.
                - If you get a short answer from the mental patient, ask him/her a related question.
                - Never reuse any sentences that has a same context which have already been used within a conversation.
                - If you get any questions from the mental patient, give him/her an answer.
                - The grammar of the sentences should be perfect.
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
                1. After you pick the best response, then write it down exactly, without leaving out a single letter.
                2. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                3. Submit the original sentences that I gave you if there is no grammar problem.
                4. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                5. Don't use any words or phrases other than the context.
                6. Never use a tone that suggests you want to do something with the patient.
                7. Never reuse any sentences that has a same context which have already been used within a conversation.
                8. If you get any questions from the mental patient, give him/her an answer.
                9. Never choose the sentence that contains 'How does it feel' or anything resembles that.
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

                **Three possible answers from a psychotherapist who wants to know and learn about his patient**: 
                "[{msg}]"

                - After reading the informations above, please **pick the best response from three possible answers** and write it down exactly, without leaving out a single letter. 
                
                **REMEMBER**:
                1. After you pick the best response, then write it down exactly, without leaving out a single letter.
                2. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                3. Submit the original sentences that I gave you if there is no grammar problem.
                4. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                5. Don't use any words or phrases other than the context.
                6. Never use a tone that suggests you want to do something with the patient.
                7. Never reuse any sentences that has a same context which have already been used within a conversation.
                8. If you get any questions from the mental patient, give him/her an answer.
                9. Never choose the sentence that contains 'How does it feel' or anything resembles that.]
        """
            }
            ],
            temperature=1,
            max_tokens=512,
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
                "content": """
                Your role is to rephrase the sentences I give you as if they were spoken by a real person in the middle of a conversation.
      
                **REMEMBER**:
                1. After you pick the best response, then write it down exactly, without leaving out a single letter.
                2. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                3. Submit the original sentences that I gave you if there is no grammar problem.
                4. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                5. Don't use any words or phrases other than the context.
                6. Never reuse any sentences that has a same context which have already been used within a conversation.
                7. Never choose the sentence that contains 'How does it feel' or anything resembles that.
                """
            },
            {
                "role": "user",
                "content": f"""
                # My Request: Rephrase the sentences below.
      
                **REMEMBER**:
                1. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                2. Submit the original sentences that I gave you if there is no grammar problem.
                3. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                4. Don't use any words or phrases other than the context.

                '''
                {new_msg}
                '''
        """
            }
            ],
            temperature=1,
            max_tokens=512,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
            my_bar.progress(75,text=progress_text)
            try:
                humanize_msg = sentence_selection.choices[0].message.content
                humanize_msg = humanize_msg[humanize_msg.index(':')+1:].strip(' ').strip('"')
            except:
                humanize_msg = sentence_selection.choices[0].message.content.strip('"')
            st.session_state.messages.append({"role": "Psychotherapist", "content": humanize_msg})
            st.session_state.conversations.append({"role": "Psychotherapist", "content": humanize_msg})
            my_bar.progress(100,text=progress_text)
            my_bar.empty()

        # Get the last user prompt in the msg history.
        if st.session_state.repeat:
            prompt = st.session_state.messages[-1]['content']
            text_logic()
            col1,col2=st.columns([9,1])
            with col1:
                st.chat_message('assistant').write(st.session_state.messages[-1]['content'])
            with col2:
                st.write('')
                st.button('🔄', on_click=reply_again_cb)
            st.session_state.repeat = False  # reset
            #st.write(st.session_state.messages[:-1])                
        else:
            # Only print the user msg if repeat is false.
            st.chat_message('user').write(prompt)
            text_logic()
            col1,col2=st.columns([9,1])
            with col1:
                st.chat_message('assistant').write(st.session_state.messages[-1]['content'])
            with col2:
                st.write('')
                st.button('🔄', on_click=reply_again_cb)
            #st.write(st.session_state.messages[:-1])


if __name__ == '__main__':
    main()