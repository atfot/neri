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
    st.session_state["messages"] = [{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]
    st.session_state['conversations']=[{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]
    st.session_state['message_summary'] = '아직까지 쓰인 내용은 없고, 여기서부터 대화내용이 시작됩니다.'

if 'repeat' not in st.session_state:
    st.session_state.repeat = False

# functions
def reply_again_cb():
    st.session_state.repeat = True


def main():

    # Print msg history.
    last_user_message = None
    for message in st.session_state.messages:

        # Print the user msg if it is not repeating successively.
        if (last_user_message is not None and
            message['role'] == '내담자' and
            last_user_message == message["content"]
        ):
            pass
        else:
            # Print both msgs from user and assistant
            if messages['role']=="심리상담사":
                st.chat_message('assistant').write(messages["content"])
            if messages['role']=="내담자":
                st.chat_message('user').write(messages["content"])

        # Backup last user msg used to identify successive same user content.
        if message['role'] == '내담자':
            last_user_message = message["content"]

    if prompt := st.chat_input('고민을 최대한 자세히 적어주세요') or st.session_state.repeat:
        def text_logic():
            normal_korean = st.session_state.client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=[
            {
              "role": "system",
              "content": """Your role is to rephrase the Korean sentences into polite Korean sentences if there are any Korean grammar errors.
              
              **Remember**:
              1. If there is anything in the paragraph that is not a normal Korean sentence, such as "ㅋ" or "ㅠ" or similar, please remove it.  
              2. If there is a sentence in the paragraph below that contains a typo, such as "있으뮤ㅠㅠㅠ", please correct the sentence in the same way as "있음".
              3. If the paragraph below contains any portmanteau words, don't rephrase it.
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
              3. If the paragraph below contains any portmanteau words, don't rephrase it.
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
            st.session_state.messages.append({"role": "내담자", "content": prompt})
            st.session_state.conversations.append({"role": "내담자", "content": normalized_prompt})

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
                - The grammar of the sentences should be perfect.
                - Never use a tone that suggests you want to do something with the patient.
                - If you get a short answer from the mental patient, ask him/her a related question.
                - Never reuse any sentences that has a same context which have already been used within a conversation.
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
                # My request:
                Read the summary, dialogue, and examples of the three answers and choose the best sentence from the three. Lets go step by step-

                - Read these informations carefully before answering my question.
                **Summary of the conversation**: [{st.session_state.message_summary}]
                
                **Conversation content**: [{st.session_state.conversations}]

                **Three possible answers from a korean psychotherapist who wants to know about his patient first and heal the patient's mind second**: 
                "[{msg}]"

                - After reading the informations above, please **pick the best response from three possible answers** and write it down exactly, without leaving out a single letter. 
                
                **REMEMBER**:
                1. After you pick the best response, then write it down exactly, without leaving out a single letter.
                2. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                3. Submit the original sentences that I gave you if there is no grammar problem.
                4. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                5. Don't use any words or phrases other than the context.
                6. Never reuse any sentences that has a same context which have already been used within a conversation.
                7. Never choose the sentence that contains 'How does it feel' or anything resembles that.]
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

        # Get the last user prompt in the msg history.
        if st.session_state.repeat:
            st.session_state.msg=st.session_state.msg[:-1]
            prompt = st.session_state.msg[-1]['content']
            text_logic()
            st.write(st.session_state.msg[:-1])
            st.button('Give me another answwer', on_click=reply_again_cb)
            st.session_state.repeat = False  # reset
        else:
            # Only print the user msg if repeat is false.
            st.chat_message('user').write(prompt)
            text_logic()
            st.write(st.session_state.msg[:-1])
            st.button('Give me another answwer', on_click=reply_again_cb)


if __name__ == '__main__':
    main()