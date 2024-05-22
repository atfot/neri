from openai import OpenAI
import streamlit as st
from korean_menu import make_sidebar
from streamlit import session_state as sss
import re

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
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
    sss.username=st.secrets.user_name
    sss.age=st.secrets.age
    sss.gender=st.secrets.user_gender
    sss.problem=st.secrets.problem
    sss.problem_explanation=st.secrets.problem_explanation
    sss.goal=st.secrets.goal
    sss.user_email=st.secrets.user_email


# variables
if "messages" not in sss:
    sss["messages"] = [{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]
if 'conversations' not in sss:
    sss['conversations']=[{"role": "심리상담사", "content": "무엇이 고민이신가요?"}]
if 'message_summary' not in sss:
    sss['message_summary'] = '아직은 요약된 내용이 없습니다.'
def saved_dialogues():
    if "message_for_summary" not in sss:
        sss.message_for_summary = ""
    result=""
    # dialogue를 result로 변환
    for entry in sss.messages:
        result += f'{entry["role"]} : {entry["content"]}\n\n'
    # 마지막 줄바꿈 문자 제거
    result = result.strip()
    sss.message_for_summary=result

if 'repeat' not in sss:
    sss.repeat = False

# functions
def reply_again_cb():
    sss.repeat = True
    sss.click_counter=0

if sss.repeat==True:
    sss.messages=sss.messages[:-1]
    sss.conversations=sss.conversations[:-1]

def main():

    # Print msg history.
    last_user_message = None
    for message in sss.messages:

        # Print the user msg if it is not repeating successively.
        if (last_user_message is not None and
            message['role'] == '내담자' and
            last_user_message == message["content"]
        ):
            pass
        else:
            # Print both msgs from user and assistant
            if message['role']=="심리상담사":
                st.chat_message('assistant').write(message["content"])
            if message['role']=="내담자":
                st.chat_message('user').write(message["content"])

        # Backup last user msg used to identify successive same user content.
        if message['role'] == '내담자':
            last_user_message = message["content"]

    if prompt := st.chat_input('맘 편히 당신의 모든 고민을 말해주세요.') or sss.repeat:
        def text_logic():
            normal_korean = sss.client.chat.completions.create(
          model="gpt-4o",
          messages=[
            {
              "role": "system",
              "content": """Your role is to rephrase the Korean sentences into polite Korean sentences if there are any Korean grammar errors.
              
              '''
              **Remember**:
              1. If there is anything in the paragraph that is not a normal Korean sentence, such as "ㅋ" or "ㅠ" or similar, please remove it.  
              2. If there is a sentence in the paragraph below that contains a typo, such as "있으뮤ㅠㅠㅠ", please correct the sentence in the same way as "있음".
              3. If the paragraph below contains any portmanteau words, don't rephrase it.
              '''
              """
            },
            {
              "role": "user",
              "content": f"""
              # My Request:
              Please rephrase the paragraph below into polite Korean sentences.

              {prompt}

              '''
              **Remember**:
              1. If there is anything in the paragraph that is not a normal Korean sentence, such as "ㅋ" or "ㅠ" or similar, please remove it.  
              2. If there is a sentence in the paragraph below that contains a typo, such as "있으뮤ㅠㅠㅠ", please correct the sentence in the same way as "있음".
              3. If the paragraph below contains any portmanteau words, don't rephrase it.
              '''
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
            if sss.repeat==True:
                pass
            else:
                sss.messages.append({"role": "내담자", "content": prompt})
                sss.conversations.append({"role": "내담자", "content": normalized_prompt})
            if len(sss.messages)%3==0:
                saved_dialogues()
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
아래의 내용을 요약해주세요.

{sss.message_for_summary}"""
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
                sss['message_summary'] = summary.choices[0].message.content
                sss['conversations'] = sss.conversations[-3:]
            
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
                - Psychotherapist cannot speak information from mentally ill person and himself unless it's really necessary
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

                - Read this step by step before filling out the form.
                **Summary of the conversation**: [{sss.message_summary}]
                **Latest Conversations**: [{sss.conversations}]     
                
                - This is the form.
                '''
                **Three possible answers from a korean psychotherapist, written in Korean language**: 
                [Given the above summary and the conversation, what are 3 possible answers a psychotherapist might give here?]
                '''
                
                **REMEMBER**: 
                '''
                - The grammar of the sentences should be perfect.
                - Never use a tone that suggests you want to do something with the patient.
                - If you get a short reply from the mental patient, ask him/her a related question.
                - Never reuse any sentences that has a same context which have already been used within a conversation.
                - If you get any questions from the mental patient, give him/her an answer.
                '''
                ```

            """
            sss.user_prompt_1=user_prompt_1
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
            top_p=0.9,
            frequency_penalty=1,
            presence_penalty=1
        )
            my_bar.progress(25,text=progress_text)
            msg = response.choices[0].message.content
            sss.msg=msg
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
                Read the summary, dialogue, and examples of the three answers and choose the best sentence from the three. Lets go step by step:

                - Read these informations carefully before answering my question.
                **Summary of the conversation**: [{sss.message_summary}]
                
                **Conversation content**: [{sss.conversations}]

                **Three possible answers from a korean psychotherapist who wants to heal the patient's mind**: 
                "[{msg}]"

                - After reading the informations above, please **pick the best response from three possible answers** considering psychotherapist's intention. 
                
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
                "content": f"""Your role is to check the korean grammar of the korean sentences and rephrase it if it has any wrong grammars, or if it is too rude.
                
                '''
                **REMEMBER**:
                1. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                2. Submit the original sentences that I gave you if there is no grammar problem.
                3. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                4. Don't use any words or phrases other than the context.
                5. If there is a "너(you)" in a given sentence, please replace it with "{sss.username}씨".
                '''
                """
            },
            {
                "role": "user",
                "content": f"""
                # My request:
                Check the korean grammar of the korean sentences below and rephrase it if it has any wrong grammars, or if it is too rude.

                [{selected_msg}]
                
                '''
                **REMEMBER**:
                1. **There should be no "" marks in your answer, and no : or - marks to show the answer.**
                2. Submit the original sentences that I gave you if there is no grammar problem.
                3. Never attach embellishments or explanation to your answers. Submit only **context** as output. 
                4. Don't use any words or phrases other than the context.
                5. If there is a "너(you)" in a given sentence, please replace it with "{sss.username}씨".
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
            sss.final_msg=humanize_msg
            try:
                junk=[':',')','}',']','>','**']
                for i in junk:
                    if humanize_msg.find(i)!=-1:
                      humanize_msg = humanize_msg[humanize_msg.find(i)+1:]
                      humanize_msg=humanize_msg.strip()
                      humanize_msg=humanize_msg.strip('"')
                      humanize_msg=humanize_msg.strip("'")
            except:
                humanize_msg=humanize_msg.strip()
                humanize_msg=humanize_msg.strip('"')
                humanize_msg=humanize_msg.strip("'")
            sss.messages.append({"role": "심리상담사", "content": humanize_msg})
            sss.conversations.append({"role": "심리상담사", "content": humanize_msg})
            my_bar.progress(100,text=progress_text)
            my_bar.empty()

        # Get the last user prompt in the msg history.
        if sss.repeat:
            prompt = sss.messages[-1]['content']
            text_logic()
            saved_dialogues()
            col1,col2=st.columns([9,1])
            with col1:
                st.chat_message('assistant').write(sss.messages[-1]['content'])
                #st.write(sss.user_prompt_1)
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
            saved_dialogues()
            col1,col2=st.columns([9,1])
            with col1:
                st.chat_message('assistant').write(sss.messages[-1]['content'])
                #st.write(sss.messages)
                #sss.conversations
            with col2:
                st.write('')
                st.button('🔄', on_click=reply_again_cb)
            #st.write(sss.messages[:-1])


if __name__ == '__main__':
    main()
