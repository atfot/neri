import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit import session_state as sss
from openai import OpenAI
from app_css import app_design

if 'client' not in sss:
  sss.client = OpenAI(api_key=st.secrets['api_key'])

if 'success_fail_messages' not in sss:
    sss.success_fail_messages=False

def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        #st.secrets.app_design_css
        app_design()
        st.image('https://imgur.com/CernNDq.png',use_column_width=True)
        st.write("")
        st.write("")

        if sss.get("logged_in", True):
            st.page_link("pages/korean_chatbot.py", label="당신의 카운셀러", icon="🩹")
            st.page_link("pages/korean_instruction.py", label="사용법", icon="ℹ️")
            st.page_link("pages/korean_bug_report.py", label="오류 제보", icon="⚠️")
            st.page_link("pages/korean_analysis.py", label="심리분석 결과", icon="🔎")
            st.page_link("pages/korean_about_me.py", label="개발자의 말", icon="💭")
            st.title('')

            if st.button("로그아웃",type='primary',use_container_width=True):
                logout()
            if st.button("대화 저장",type='secondary',use_container_width=True):
                save_analysis_and_messages()
            if st.button("내 정보",type='secondary',use_container_width=True):
                st.switch_page("pages/korean_my_info.py")
            if sss.success_fail_messages is not False:
                sss.success_fail_messages
                sleep(5)
                st.empty()

            st.title('')
            st.markdown(
                """
                <div style="left: 0; width: 101%; color: #000000; text-align: left;">
                    Developed By <a  href="https://i.imgur.com/JuFxv4h.png" target="_blank">Hyun Kyu Cho</a><br>
                    Made with Streamlit<br>
                    Powered By OpenAI
                </div>
                """,
                unsafe_allow_html=True
            )

        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")


def logout():
    sss.logged_in = False
    if "messages" in sss:
        del sss["messages"]
        del sss['conversations']
        del sss['message_summary']
        try:
            del sss.my_info
        except:
            pass
        try:
            del sss.many_login_attempt
        except:
            pass
        try:
            del sss.problem_analysis
        except:
            pass
        del sss.client
    sss.success_fail_messages=st.info("다음에 또 뵈어요😊")
    sleep(0.5)
    st.switch_page("streamlit_app.py")

def save_analysis_and_messages():    
    with st.spinner('저장중...'):
        if 'problem_analysis' not in sss:
            problem_analysis = sss.client.chat.completions.create(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                        {
                            "role": "system",
                            "content": """Your role as a Korean professional psychotherapist is to score the extent to which the client's problem has improved given the information below and explain why.
                            
                            **Remember**:
                            1. Use Korean Language to answer my question.
                            2. Your score should be much lower than you think.
                            3. You should never speak rudely.
                            """
                        },
                        {
                            "role": "user",
                            "content": f"""
                            # My Request:
                            From a Korean professional psychotherapist's perspective, score the extent to which the client's problem is improved by the information given below and explain why.

                            # Informations you need to know
                            - Client's Name : {sss.username}
                            - Age : {sss.age}
                            - Gender : {sss.gender}
                            - Problem : {sss.problem}
                            - Problem Explanation : {sss.problem_explanation}
                            - Goal : {sss.goal}

                            - Message summary : 
                            {sss.message_summary}

                            - The latest conversations:
                            {sss.conversations}
                        
                            # Answer form
                            - You need to use the form below to answer my request using Korean language.
                            '''
                            Analysis : [Analyze the information I've given you by not using any bullet points.]

                            Score : [Based on the analysis you did, please score how well the {sss.username}'s problem was solved.]

                            Explanation : [Tell me how the score you gave me was based on your considerations.
                            *Scoring criteria*:
                            10 : The person's psychosis has been cured, or the client is no longer suffering from the problem.
                            9 : The person's mental illness is on the verge of being cured or the issue is on the verge of being completely resolved.
                            6 ~ 8 : The client is directly demonstrating a willingness to work toward a positive direction.
                            3 ~ 5 : The client is not directly demonstrating a willingness to move in a positive direction.
                            2 : The client is directly demonstrating a willingness to work toward a negative direction.
                            1 : The client has a serious mental illness or mental health issue and needs to see a real doctor or psychologist to address it.]

                            Best thing to do : [Tell me what you think is the easiest thing for {sss.username} to do in that situation, using a bullet point summary, as a professional psychologist.]
                            '''
                            **Remember**:
                            1. Use Korean Language to answer my question.
                            2. Your score should be much lower than you think.
                            3. Don't use the word '고객' or '클라이언트'.
                            4. If you need to use the word '고객', don't use that word and replace it into the client's name with '님', such as {sss.username}님.
                            5. You should never speak rudely.
                """
                        }
                        ],
                        temperature=1,
                        max_tokens=1024,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                        )    
            problem_analysis = problem_analysis.choices[0].message.content
            problem_analysis=problem_analysis.strip().strip("'''")
            sss.problem_analysis=problem_analysis
            problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
            sss.client_analysis=problem_analysis[:problem_analysis.find('\n')].replace('. ','.\n\n')
            problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
            problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
            sss.score=problem_analysis[:problem_analysis.find('\n')]
            problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
            problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
            sss.score_explanation=problem_analysis[:problem_analysis.find('\n')].replace('. ','.\n\n')
            problem_analysis=problem_analysis[problem_analysis.find('\n'):].strip()
            problem_analysis=problem_analysis[problem_analysis.find(':')+1:].strip()
            sss.what_to_do=problem_analysis.split('\n')
            sss.success_fail_messages=st.success('대화 내역이 저장되었습니다!')