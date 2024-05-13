import streamlit as st
from korean_menu import make_sidebar
from openai import OpenAI
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from streamlit import session_state as sss
import requests
import tempfile

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
make_sidebar()

if 'client' not in sss:
  sss.client = OpenAI(api_key=st.secrets['api_key'])

if 'username' not in sss:
   sss.username=st.secrets.user_name
   sss.age=st.secrets.age
   sss.gender=st.secrets.user_gender
   sss.problem=st.secrets.problem
   sss.problem_explanation=st.secrets.problem_explanation
   sss.goal=st.secrets.goal

if st.button('try'):
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

    def regular_font(arg):
        if 'regular_font_dir' not in sss:
            response_regular = requests.get("https://github.com/atfot/neri/raw/main/pdf_dir/NotoSansKR-Regular.ttf", stream=True)        
            sss.regular_font_dir = tempfile.NamedTemporaryFile(delete=False)
            with open(sss.regular_font_dir.name, 'wb') as f:
                for chunk in response_regular.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                pdf.add_font('NotoSansKR-Regular.ttf','',sss.regular_font_dir.name, uni=True)
                pdf.set_font('NotoSansKR-Regular.ttf', '', arg)
        else:
            pdf.add_font('NotoSansKR-Regular.ttf','',sss.regular_font_dir.name, uni=True)
    def thick_font(arg):
        if 'thick_font_dir' not in sss:
            response_thick = requests.get("https://github.com/atfot/neri/raw/main/pdf_dir/NotoSansKR-SemiBold.ttf", stream=True)        
            sss.thick_font_dir = tempfile.NamedTemporaryFile(delete=False)
            with open(sss.thick_font_dir.name, 'wb') as f:
                for chunk in response_regular.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                pdf.add_font('NotoSansKR-SemiBold.ttf','',sss.thick_font_dir.name, uni=True)
                pdf.set_font('NotoSansKR-SemiBold.ttf', '', arg)
        else:
            pdf.add_font('NotoSansKR-SemiBold.ttf','',sss.thick_font_dir.name, uni=True)
            
    class PDF(FPDF):
        def header(self):
            regular_font(8)
            # Title
            self.cell(30, 10, '', 0, 0, 'C')
            # Line break
            self.ln(20)
        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            regular_font(8)
            # Page number
            self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    # Margin
    m = 10 
    # Page width: Width of A4 is 210mm
    pw = 210 - 2*m
    # Cell height
    ch = 50

    # PDF 객체 생성
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    thick_font(24)    
    pdf.cell(w=190, h=20, txt="{sss.username}의 심리 분석결과", align='C', border=0, ln=1) #풀사이즈 h값=266, 풀사이즈 w값=190
    pdf.cell(w=190, h=20, txt="", align='C', border=0, ln=1)

    normal_font(10)
    pdf.text(x= 142, y= 55, txt= 'Analyzed by')
    # 로고
    # 로고는 깃허브에서 자주 나가리되니까 계속 새로 복붙해주면서 사용할 것 - 내 깃허브 레포 디렉토리에 있음
    pdf.image("https://raw.githubusercontent.com/atfot/neri/main/pdf_dir/chatbot_mobile_home_korean.png", x = 154, y = 48, w = 42, h = 18, type='PNG') 

    #2페이지
    thick_font(15)
    pdf.cell(w=190, h=12, txt="인공지능 네리가 분석한 보고서입니다!", border=0, ln=1)
    normal_font(12)
    pdf.multi_cell(w=0, h=7.5, txt="네리는 OpenAI사의 GPT 3.5와 4.0을 사용해 제작된 인공지능 심리상담 챗봇입니다. 이 보고서는 금일 해당 사용자가 네리와 대화하며 도출된 분석결과입니다. 참고만 하시길 바라며 자세한건 가까운 정신과나 심리상담사를 직접 방문하셔서 도움을 받으세요.", border = 0, align = 'J', fill = False)

    thick_font(15)
    pdf.cell(w=0, h=20, txt="고객님의 정보", border=0, ln=1)
    thick_font(12)
    pdf.cell(w=30, h=10, txt="1. 별명 : ", border=0, ln=0)
    normal_font(12)
    pdf.cell(w=0, h=10, txt=f"{sss.username}", border=0, ln=1)
    thick_font(12)
    pdf.cell(w=30, h=10, txt="2. 연령 : ", border=0, ln=0)
    normal_font(12)
    pdf.cell(w=0, h=10, txt=f"{sss.age}", border=0, ln=1)
    thick_font(12)
    pdf.cell(w=30, h=10, txt="3. 성별 : ", border=0, ln=0)
    normal_font(12)
    pdf.cell(w=0, h=10, txt=f"{sss.gender}", border=0, ln=1)
    thick_font(12)
    pdf.cell(w=30, h=10, txt="4. 고민 : ", border=0, ln=0)
    normal_font(12)
    pdf.multi_cell(w=0, h=10, txt=f"""{sss.problem}""", border=0, align = 'J', fill = False)
    thick_font(12)
    pdf.cell(w=0, h=10, txt="5. 고민 설명 : ", border=0, ln=0)
    normal_font(12)
    pdf.multi_cell(w=0, h=10, txt=f"""{sss.problem_explanation}""", border=0, align = 'J', fill = False)
    thick_font(12)
    pdf.cell(w=30, h=10, txt="5. 목표 : ", border=0, ln=0)
    normal_font(12)
    pdf.multi_cell(w=0, h=10, txt=f"""{sss.goal}""", border=0, align = 'J', fill = False)
    ""

    sss.date=f"{time.localtime().tm_year}년 {time.localtime().tm_mon}월 {time.localtime().tm_mday}일"

    thick_font(15)
    pdf.cell(w=0, h=20, txt=f"{sss.date}의 분석 결과", border=0, ln=1)
    thick_font(12)
    pdf.cell(w=40, h=10, txt="문제 분석 :", border=0, ln=0)
    normal_font(12)
    pdf.multi_cell(w=0, h=10, txt=f"""{sss.client_analysis}""", border=0, align = 'J', fill = False)
    thick_font(12)
    pdf.cell(w=40, h=10, txt="해결 진전도 :", border=0, ln=0)
    normal_font(12)
    pdf.cell(w=0, h=10, txt=f"{sss.score}", border=0, ln=1)
    thick_font(12)
    pdf.cell(w=40, h=10, txt="채점기준 :", border=0, ln=0)
    normal_font(12)
    pdf.multi_cell(w=0, h=10, txt=f"""{sss.score_explanation}""", border=0, align = 'J', fill = False)
    pdf.cell(w=0, h=10, txt="", border=0, ln=1)

    thick_font(12)
    pdf.cell(w=0, h=10, txt="", border=0, ln=0)
    pdf.cell(w=0, h=10, txt="도움이 될만한 행동들 : ", border=0, ln=1)
    for i in sss.what_to_do:
        pdf.cell(w=0, h=10, txt="", border=0, ln=0)
        pdf.cell(w=0, h=10, txt=i, border=0, ln=1)

    pdf.cell(w=0, h=10, txt="", border=0, ln=1)
    thick_font(15)
    pdf.cell(w=0, h=10, txt="고민 해결도 그래프", align="C", border=0, ln=1)
    pdf.cell(w=20, h=10, txt="", align="C", border=0, ln=0)
    pdf.cell(w=0,h=0,link=pdf.image("https://raw.githubusercontent.com/atfot/neri/main/pdf_dir/chatbot_mobile_home_english.png", w = 150, h = 70, type='PNG'), border=0, ln=1) # W값 중요하니까 절대 바꾸지 말것 - 190
    pdf.cell(w=20, h=10, txt="", align="C", border=0, ln=0)

    pdf_bytes = pdf.output(dest='S').encode('latin1')

    # 이메일 보내기
    from_address = 'nerichatbot@gmail.com'
    to_address = 'nerierror@naver.com'
    subject = "PDF 파일 보내기"
    body = "PDF 파일을 첨부합니다."

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    attachment = MIMEBase('application', 'pdf', filename='tuto1.pdf')
    attachment.set_payload(pdf_bytes)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename='tuto1.pdf')
    msg.attach(attachment)

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(from_address, 'hzfemdpfnfczwixe')
    smtp_server.sendmail(from_address, to_address, msg.as_string())
    smtp_server.quit()
    st.write('했당')