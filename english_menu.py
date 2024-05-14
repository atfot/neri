import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit import session_state as sss
from openai import OpenAI
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import pdfkit


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        #st.secrets.app_design_css
        st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* share 버튼 */
div.st-emotion-cache-zq5wmm.ezrtsby0 > div > div:nth-child(1) > button > div > span {
	font-family: 'Beeunhye';
	font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}  
/* running... */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > label {
	font-family: 'Beeunhye';
	font-size: 1.5em;
    letter-spacing:0.075em;
}

/* stop */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > span > button {
	font-family: 'Beeunhye';
	font-size: 1.5em;
    letter-spacing:0.075em;
}

/* 메뉴 화면 */
/* 메뉴 */
span.st-emotion-cache-icvz16.e11k5jya0 > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    margin-top: -0.15em; 
    margin-left: 0.25em; 
    letter-spacing:0.075em;
}       

/* 로그아웃 버튼 */
div.st-emotion-cache-dvne4q.eczjsme4 > div > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
	font-size: 2em;
    letter-spacing:0.075em;
}     

/* 로그아웃 메세지 */      
div.st-emotion-cache-dvne4q.eczjsme4 > div > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.5em;
    letter-spacing:0.075em;
}

/* 챗봇 */  
/* 챗봇 글씨체 */
div.st-emotion-cache-in40sa.eeusbqq3 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
	margin-top: -0.35em;
    letter-spacing:0.075em;
}     
div.st-emotion-cache-1ovfu5.eeusbqq3 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
	margin-top: -0.35em;
    letter-spacing:0.075em;
}     

/* thinking... */
div.st-emotion-cache-c6gdys.e18r7x300 > div > p {
	font-family: 'Beeunhye';
	font-size: 2em;
    letter-spacing:0.075em;
}
                    
/* 내 정보 */
/* 내 정보 내용 */
div.st-emotion-cache-1yycg8b.e1f1d6gn3 > div > div > div > div > div > div > p{
	font-family: 'Beeunhye';
	font-size: 1.75em;
    letter-spacing:0.075em;
}
            
/* 내 정보_분석 결과_도움이 될만한 행동들_고민 해결도 그래프*/
.st-emotion-cache-10trblm {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    letter-spacing:0.075em;
}

            
/* 분석결과 내용 */            
div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    letter-spacing:0.075em;
}     

/* 프로필 수정 버튼 */         
div.st-emotion-cache-1yycg8b.e1f1d6gn3 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    letter-spacing:0.075em;
}     

/* 도움이 될만한 행동들 리스트 */      
div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div > div > div > ul > li {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    letter-spacing:0.075em;
}        
div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    letter-spacing:0.075em;
}        

/* 정보를 바꿔주세요 */
div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > div > div:nth-child(1) > div > div > p {
    font-family: 'Beeunhye';
    font-size: 2.25em;
    letter-spacing:0.075em;
}

/* 정보 수정칸 */
div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > label > div > p {
    font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.075em;
}

/* 저장 버튼 */
div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > button > div > p {
    font-family: 'Beeunhye';
    font-size: 1.75em;
}

/* 저장완료 메세지 */
div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
    font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.075em;
}
                    
/* 이메일로 고객 정보 전송버튼 */
div.st-emotion-cache-fplge5.e1f1d6gn3 > div > div > div > div > div > button > div > p {
    font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.075em;
}
                    
/* 성공 실패 메세지 */
div.st-emotion-cache-fplge5.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
                    
/* 오류 제보 */
/* 기본 문구 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > p {
    font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.075em;
}
                    
/* 설명란 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > label > div > p {
    font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}
/* 성공 실패 메세지 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p {
    font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}
</style>
""", unsafe_allow_html=True)
        st.image('https://imgur.com/F2P7a3I.png',use_column_width=True)
        st.write("")
        st.write("")

        if sss.get("logged_in", True):
            st.page_link("pages/english_chatbot.py", label="My Councellor", icon="🩹")
            st.page_link("pages/english_analysis.py", label="My Info", icon="ℹ️")
            st.page_link("pages/english_bug_report.py", label="Any Errors?", icon="⚠️")
            st.page_link("pages/english_instruction.py", label="How To Use", icon="❓")
            st.title('')

            if st.button("Logout",type='primary',use_container_width=True):
                logout()
            if st.button("Analysis Results",type='secondary',use_container_width=True):
                send_analysis_via_email()

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
            del sss.username
        except:
            pass
        try:
            del sss.my_info
        except:
            pass
        try:
            del sss.many_login_attempt
        except:
            pass
        del sss.client
    st.info("See ya next time😊")
    sleep(0.5)
    st.switch_page("streamlit_app.py")

def send_analysis_via_email():
    if 'date' not in sss:
        month=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month=month[time.localtime().tm_mon-1]
        sss.date=f'{month} {time.localtime().tm_mday}, {time.localtime().tm_year}'
    with st.spinner('loading..'):
        if 'problem_analysis' not in sss:
            problem_analysis = sss.client.chat.completions.create(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                        {
                            "role": "system",
                            "content": """Your role as a professional psychotherapist is to score the extent to which the client's problem has improved given the information below and explain why.
                            
                            **Remember**:
                            1. Your score should be much lower than you think.
                            2. You should never speak rudely.
                            """
                        },
                        {
                            "role": "user",
                            "content": f"""
                            # My Request:
                            From a professional psychotherapist's perspective, score the extent to which the client's problem is improved by the information given below and explain why.

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
                            - You need to use the form below to answer my request.
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
                            1. Your score should be much lower than you think.
                            2. Don't use the word 'client'.
                            3. If you need to use the word 'client', don't use that word and replace it into the client's name, such as {sss.username}.
                            4. You should never speak rudely.
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

        html_problem=sss.problem.replace('\n','<br>')
        html_problem_explanation=sss.problem_explanation.replace('\n','<br>')
        html_goal=sss.goal.replace('\n','<br>')
        html_client_analysis=sss.client_analysis.replace('\n','<br>')
        html_score_explanation=sss.score_explanation.replace('\n','<br>')
        #인라인 css 태그 전부 style에 옮겨줄것
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Psychometric analysis results</title>
            <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap');
            .noto-sans-<uniquifier> {
  font-family: "Noto Sans", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
  letter-spacing: 2px;
  line-height: 10px;
  font-variation-settings:
    "wdth" 100;
}
            body{font-family: 'Noto Sans'; letter-spacing: 2px; line-height: 10px;}
            </style>
        </head>"""
        html_content_1=f'''<body style="margin: 0; padding: 50px 0 50px 0;">
            <table align="center" border="0" cellpadding="10" cellspacing="10" width="900" style="border: 1px solid #cccccc;">
                <tr>
                    <td align="center" style="padding: 30px 0 0 0; font-size:40px;">
                        <b>Analysis results on {sss.date}</b>
                    </td>
                </tr>
                <tr>
                    <td bgcolor="#ffffff" style="padding: 30px 10px 30px 10px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td>
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                        <tr>
                                            <td align="right" width="720" valign="top">
                                                Powered by
                                            </td>
                                            <td align="right" width="140" valign="top">
                                                <img src="https://imgur.com/H287o5n.png" alt="Logo" width="140" height="60" style="display: block;" />
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td style="color: #000000; font-size: 36px;">
                                    <b>This report was analyzed by Neri AI!</b>
                                </td>
                            </tr> 
                            <tr style="color: #000000; font-size: 24px; line-height: 30px;"
                            >
                                <td style="padding: 20px 0 30px 0;">
                                    Neri is an artificial intelligence psychological counseling chatbot built using GPT 3.5 and 4.0 by OpenAI. This report is based on the user's interaction with Neri today. It is intended as a guide only and you should visit your local psychiatrist or psychologist for more information.
                                </td>
                            </tr>
                            <tr style="color: #000000; font-size: 24px; line-height: 25px;"
                            >
                                <td>
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                        <tr>
                                            <td width="260" valign="top">
                                                <h2>Client's Info</h2>
                                                <p><b>1. Username : </b>{sss.username}</p>
                                                <p><b>2. Age : </b>{sss.age}</p>
                                                <p><b>3. Gender : </b>{sss.gender}</p>
                                                <p><b>4. Problem : </b>{html_problem}</p>
                                                <p><b>5. Problem_explanation : </b></p>
                                                <p>{html_problem_explanation}</p>
                                                <p><b>6. Goal : </b></p>
                                                <p>{html_goal}</p>
                                            </td>
                                            <td style="font-size: 0; line-height: 0;" width="20">
                                            &nbsp;
                                            </td>
                                            <td width="260" valign="top">
                                                <h2>{sss.username}'s analytics results</h2>
                                                <p><b>Problem analysis : </b></p>
                                                <p>{html_client_analysis}</p>
                                                <p><b>Score : </b>{sss.score}</p>
                                                <p><b>Score Explanation : </b></p>
                                                <p>{html_score_explanation}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td style="color: #000000; font-size: 16px; line-height: 15px;">
                                    <p><br></p>
                                </td>
                            </tr>
                            <tr>
                                <td style="color: #000000; font-size: 24px; line-height: 30px; border-radius: 5px; align-self: center; width: 100%; margin: 0 auto; border: 0.1px solid #cccccc; padding: 20px;">
                                    <p><b>Actions that might help you : </b></p>'''

        todolist_format="""
        <ul>
            <li>
                <p><b>{}</b></p>
            </li>
        </ul>
        """
        html_text_2=''
        for i in sss.what_to_do:
            html_text_2+=todolist_format.format(i)

        html_text_3='''
                                </td>
                            </tr>
                            <tr>
                                <td style="color: #000000; font-size: 16px; line-height: 15px;">
                                    <p><br></p>
                                </td>
                            </tr>
                            <tr align="center" width="100%" style="color: #000000; line-height: 15px;">
                                <td>
                                    <h2>Problem Resolution Graph</h2>
                                </td>
                            </tr>
                            <tr align="center" width="100%">
                                <td>
                                    <img src="https://imgur.com/MvfBBoV.png" width="360" height="140" style="display: block;" />
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 30px 30px 30px 30px; bottom: 0; left: 0; width: 100%; background-color: #FFFFFF; color: #000000; padding: 10px; text-align: center;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td>
                                    Developed By <a href="https://imgur.com/JuFxv4h.png" color="#000000" target="_blank"><font color="#000000">Hyun Kyu Cho</font></a> |  Made with Streamlit  |  Powered By OpenAI
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        '''
        html=html_content+html_content_1+html_text_2+html_text_3
        pdf = pdfkit.from_string(html, False)
        pdf_bytes = bytes(pdf)
        from_address = st.secrets.admin_email
        to_address = st.secrets.user_email
        subject = f"Analysis results on {sss.date}"

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        gratitude_email=f'''
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Email_Design</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>
    <body style="margin: 0; padding: 20px 20px 20px 20px;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" width="800" style="border: 1px solid #FDF6EC;">
            <tr>
                <td bgcolor="#FDF6EC" style="padding: 0 0 10px 0;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tr>
                            <td style="padding-left:10px;">
                                <h3>Dear {sss.username},</h3>
                            </td>
                        </tr> 
                        <tr>
                            <td>
                                <img src="https://pbs.twimg.com/profile_images/1688611811933982720/_tovpXIN_400x400.jpg" alt='welcome_message' width="100%" style="display: block;" />
                            </td>
                        </tr>
                        <tr>
                            <td align="right" style="padding-right:10px;">
                                <p>Yours sincerely,</p>
                                <h3>Hyun Kyu Cho</h3>
                            </td>
                        </tr> 
                        <tr>
                            <td style="bottom: 0; left: 0; padding: 50px 0 0 0; width: 100%; background-color: #FDF6EC; color: #562400; text-align: center;">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td>
                                            Developed By <a href="https://imgur.com/JuFxv4h.png" style="color:#562400;" target="_blank"><font color="#562400">Hyun Kyu Cho</font></a> |  Made with Streamlit  |  Powered By OpenAI
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
</html>
        '''
        msg.attach(MIMEText(gratitude_email, 'html'))
        attachment = MIMEBase('application', 'pdf', pdf_name=f'Analysis results on {sss.date}.pdf')
        attachment.set_payload(pdf_bytes)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=f'Analysis results on {sss.date}.pdf')
        msg.attach(attachment)

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(from_address, st.secrets.admin_pw)
        smtp_server.sendmail(from_address, to_address, msg.as_string())
        smtp_server.quit()
        st.success("I've compiled your Neri analysis and sent it to you via email😊")