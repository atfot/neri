import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


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
/* 타이틀 */
div.st-emotion-cache-dvne4q.eczjsme4 > div > div > div > div > div > div > div > div > div > h1 {
	font-family: 'Beeunhye';
	font-size: 2.5em;
    margin-top: -0.4em; 
    margin-left: 0.25em; 
    letter-spacing:0.075em;
}
   
/* 메뉴 */
span.st-emotion-cache-icvz16.e11k5jya0 > div > p {
	font-family: 'Beeunhye';
	font-size: 2em;
    margin-top: -0.1em; 
    margin-left: 0.25em; 
    letter-spacing:0.075em;
}       

/* 로그아웃 버튼 */
div.st-emotion-cache-dvne4q.eczjsme4 > div > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
	font-size: 2em;
    color: #b5651d;
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
</style>
"""

, unsafe_allow_html=True)
        st.image('https://imgur.com/CernNDq.png',use_column_width=True)
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", True):
            st.page_link("pages/korean_chatbot.py", label="당신의 카운셀러", icon="🩹")
            st.page_link("pages/korean_analysis.py", label="내 정보", icon="ℹ️")
            st.page_link("pages/korean_instruction.py", label="사용법", icon="❓")
            st.title('')

            if st.button("로그아웃",type='primary',use_container_width=True):
                logout()

        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")


def logout():
    st.session_state.logged_in = False
    if "messages" in st.session_state:
        del st.session_state["messages"]
        del st.session_state['conversations']
        del st.session_state['message_summary']
        try:
            del st.session_state.username
        except:
            pass
        try:
            del st.session_state.my_info
        except:
            pass
        try:
            del st.session_state.many_login_attempt
        except:
            pass
        del st.session_state.client
    st.info("다음에 또 뵈어요😊")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
