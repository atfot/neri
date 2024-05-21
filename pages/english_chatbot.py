from openai import OpenAI
import streamlit as st
from english_menu import make_sidebar
from streamlit import session_state as sss

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="centered"
)
try:
    del sss.fix_info, sss.auth_email
except:
    pass
make_sidebar()

if 'client' not in sss:
  sss.client = OpenAI(api_key=st.secrets['api_key'])

if sss.id==False:
    sss.username=st.secrets.user_name_2
    sss.age=st.secrets.age_2
    sss.gender=st.secrets.user_gender_2
    sss.problem=st.secrets.problem_2
    sss.problem_explanation=st.secrets.problem_explanation_2
    sss.goal=st.secrets.goal_2
    sss.user_email=st.secrets.user_email_2

# variables
if "messages" not in sss:
    sss["messages"] = [{"role": "Psychotherapist", "content": "What's bothering you?"}]
    sss['conversations']=[{"role": "Psychotherapist", "content": "What's bothering you?"}]   
    sss['message_summary'] = 'Nothing has been written to date, and the conversation starts below.'

if 'repeat' not in sss:
    sss.repeat = False

# functions
def reply_again_cb():
    sss.repeat = True

if sss.repeat==True:
    sss.messages=sss.messages[:-1]
    sss.conversations=sss.conversations[:-1]

def main():

    # Print msg history.
    last_user_message = None
    for message in sss.messages:

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

    if prompt := st.chat_input("Feel free to tell me all your problems.") or sss.repeat:
        def text_logic():
            if sss.repeat==True:
                pass
            else:
                sss.messages.append({"role": "Mental patient", "content": prompt})
                sss.conversations.append({"role": "Mental patient", "content": prompt})
            if len(sss.messages)%3==0:
                summary = sss.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                    "role": "system",
                    "content": "Your role is to summarize the paragraph I give to you."
                    },
                    {
                    "role": "user",
                    "content": f"""                    
Please briefly summarize the conversation below.

{sss.messages}"""
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
                sss['message_summary'] = summary.choices[0].message.content
                sss['conversations'] = sss.messages[-3:]
            
            progress_text='thinking...'
            my_bar=st.progress(0,text=progress_text)
            
            system_prompt=f"""```
                # Primary System Guidance
                Your goal is to help me, the playwright, write a script for a play. Let's go step-by-step:

                # Information about the play
                - Conversation between one mentally ill person and one psychotherapist
                - The two are now meeting and talking online
                - Psychotherapist uses the most respectful tone of voice possible, and the person with mental illness prefers it
                - Person with mental illness wants to talk with his/her psychotherapist
                - The psychotherapist wants to have a deep and wide conversation with the mentally ill person

                # Character information
                1. mentally ill person
                - Name: {sss.username}
                - Age: {sss.age}
                - Gender: {sss.gender}
                - Problem : {sss.problem}
                - Problem Explanation: {sss.problem_explanation}
                - Goal : {sss.goal}

                2. psychological counselor
                - Name : Neri
                - Age : 55 years old
                - Gender: Male
                - Country of Origin : South Korea
                - City of residence : Seoul
                - Characteristics : Neri has information about {sss.username}, who is mentally ill, and engages in an extensive conversation with him/her, but also asks any questions if he wants to understand more about him/her

                '''
                **REMEMBER**: 
                - Psychotherapist cannot speak information from mentally ill person and himself unless it's really necessary.
                - Keep in mind that the psychotherapist's response is part of the conversation and will be followed by the mentally ill person's response
                - The psychotherapist's response should fit the tone and content of the conversation
                - If you get a short answer from the mental patient, ask him/her a related question
                - The psychotherapist is talking to only one person with a mental illness(Check the "# Character information")
                - Never reuse any sentences that has a same context which have already been used within a conversation
                - The grammar of the sentences should be perfect
                - If you get any questions from the mental patient, give him/her an answer
                - Never use a tone that suggests you want to do something with the patient
                - Make sure you understand the content of "# Information about the play" and "# Character information" before answering
                '''   
                ```
            """
            
            user_prompt_1=f"""
                ```
                # My requests: 
                Your goal is to help me, the playwright, write a script for a play. Let's go step-by-step:

                - Read this step by step before filling out the form
                **Summary of the conversation**: [{sss.message_summary}]
                **Latest Conversations**: [{sss.conversations}]     
                
                - This is the form      
                '''
                **Three possible answers from a psychotherapist**: 
                [Given the above summary and the conversation, what are 3 possible answers a psychotherapist might give here?]
                '''
                
                '''
                **REMEMBER**: 
                - The grammar of the sentences should be perfect.
                - Never use a tone that suggests you want to do something with the patient.
                - If you get a short reply from the mental patient, ask him/her a related question.
                - Never reuse any sentences that has a same context which have already been used within a conversation.
                - If you get any questions from the mental patient, give him/her an answer.
                '''
                ```

            """
            
            response = sss.client.chat.completions.create(
            model="gpt-4o",
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
            msg = response.choices[0].message.content
            sentence_selection = sss.client.chat.completions.create(
            model="gpt-4o",
            messages=[
            {
                "role": "system",
                "content": f"""                
                #Primary System Guidance
                Your role is to read the script's dialogue, summary, and examples of the three answers and choose the best sentence from the three. Let's go step-by-step:

                # Information about the play
                - Conversation between one mentally ill person and one psychotherapist
                - The two are now meeting and talking online
                - Psychotherapist uses the most respectful tone of voice possible, and the person with mental illness prefers it
                - Person with mental illness wants to talk with his/her psychotherapist
                - The psychotherapist wants to have a deep and wide conversation with the mentally ill person

                # Character information
                1. mentally ill person
                - Name: {sss.username}
                - Age: {sss.age}
                - Gender: {sss.gender}
                - Problem : {sss.problem}
                - Problem Explanation: {sss.problem_explanation}
                - Goal : {sss.goal}

                2. psychological counselor
                - Name : Neri
                - Age : 55 years old
                - Gender: Male
                - Country of Origin : South Korea
                - City of residence : Seoul
                - Characteristics : Neri has information about {sss.username}, who is mentally ill, and engages in an extensive conversation with him/her, but also asks any questions if he wants to understand more about him/her

                '''
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
                '''
                """
            },
            {
                "role": "user",
                "content": f"""
                # My request:
                Read the summary, dialogue, and examples of the three answers and choose the best sentence from the three. Lets go step by step-

                - Read these informations carefully before answering my question.
                **Summary of the conversation**: [{sss.message_summary}]
                
                **Conversation content**: [{sss.conversations}]

                **Three possible answers from a psychotherapist who wants to learn about his patient and heal his patient's mind**: 
                "[{msg}]"

                - After reading the informations above, please **pick the best response from three possible answers** considering psychotherapist's intention, and write it down exactly, without leaving out a single letter. 
                
                '''
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
            my_bar.progress(50,text=progress_text)
            selected_msg = sentence_selection.choices[0].message.content.strip('"')
            humanize_sentence = sss.client.chat.completions.create(
            model="gpt-4o",
            messages=[
            {
                "role": "system",
                "content": """
                Your role is to rephrase the sentences I give you as if they were spoken by a real person in the middle of a conversation.
      
                '''
                **REMEMBER**:
                1. After you pick the best response, then write it down exactly, without leaving out a single letter.
                2. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                3. Submit the original sentences that I gave you if there is no grammar problem.
                4. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                5. Don't use any words or phrases other than the context.
                6. Never reuse any sentences that has a same context which have already been used within a conversation.
                7. Never choose the sentence that contains 'How does it feel' or anything resembles that.
                '''
                """
            },
            {
                "role": "user",
                "content": f"""
                # My Request: Rephrase the sentences below.
      
                '''
                **REMEMBER**:
                1. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                2. Submit the original sentences that I gave you if there is no grammar problem.
                3. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                4. Don't use any words or phrases other than the context.
                '''

                '''
                {selected_msg}
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
            humanize_msg = sentence_selection.choices[0].message.content
            try:
                junk=[':',')','}',']','>','**']
                for i in junk:
                    if humanize_msg.find(i)!=-1:
                      humanize_msg = humanize_msg[humanize_msg.find(i)+1:]
                      humanize_msg=humanize_msg.strip()
                      humanize_msg=humanize_msg.strip()
                      humanize_msg=humanize_msg.strip('"')
                      humanize_msg=humanize_msg.strip('"')
                      humanize_msg=humanize_msg.strip("'")
                      humanize_msg=humanize_msg.strip("'")
            except:
                humanize_msg=humanize_msg.strip()
                humanize_msg=humanize_msg.strip()
                humanize_msg=humanize_msg.strip('"')
                humanize_msg=humanize_msg.strip('"')
                humanize_msg=humanize_msg.strip("'")
                humanize_msg=humanize_msg.strip("'")
            sss.messages.append({"role": "Psychotherapist", "content": humanize_msg})
            sss.conversations.append({"role": "Psychotherapist", "content": humanize_msg})
            my_bar.progress(100,text=progress_text)
            my_bar.empty()

        # Get the last user prompt in the msg history.
        if sss.repeat:
            prompt = sss.messages[-1]['content']
            text_logic()
            col1,col2=st.columns([9,1])
            with col1:
                st.chat_message('assistant').write(sss.messages[-1]['content'])
                #st.write(sss.messages)
                #st.write(sss.conversations)
            with col2:
                st.write('')
                st.button('🔄', on_click=reply_again_cb)
            sss.repeat = False  # reset
            #st.write(sss.messages[:-1])                
        else:
            # Only print the user msg if repeat is false.
            st.chat_message('user').write(prompt)
            text_logic()
            col1,col2=st.columns([9,1])
            with col1:
                st.chat_message('assistant').write(sss.messages[-1]['content'])
            with col2:
                st.write('')
                st.button('🔄', on_click=reply_again_cb)
            #st.write(sss.messages[:-1])

if __name__ == '__main__':
    main()
