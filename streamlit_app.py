import streamlit as st
from time import sleep
from streamlit_js_eval import streamlit_js_eval
from streamlit import session_state as sss

if 'messages' not in sss:
    if 'screen_setting' not in sss:
        sss.screen_setting = 'pc'  # default value

    st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    menu_items=None
)
    #st.secrets.home_css
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
    letter-spacing:0.1em;
}

/* 한영 토글 */
div.st-bl.st-bm.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.1em;
}
div.st-ch.st-ci.st-cj.st-ae.st-af.st-ag.st-ck.st-ai.st-aj.st-cl.st-cm > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.1em;
}
div.st-d6.st-c1.st-bb.st-ax.st-ay.st-az.st-d7.st-b1.st-b2.st-d8.st-d9 > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.1em;
}
                  
/* 로그인 해주세요 */
div.st-emotion-cache-1bfnhmd.e1f1d6gn3 > div > div > div > div > div > div > div > p > b {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.1em;
}
                
/* 아이디_비밀번호 */
div.st-emotion-cache-1bfnhmd.e1f1d6gn3 > div > div > div > div > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.1em;
}

/* 로그인 새로 오신 분 */                
div.st-emotion-cache-1bfnhmd.e1f1d6gn3 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.1em;
}                
                
/* 아이디 비번 찾기 */
div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.1em;
}

/* pc-성공실패 메세지 */
div.st-emotion-cache-khxqah.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    margin-top: -0.4em; 
    margin-left: 0.25em;
    letter-spacing:0.1em;
}
/* 태블릿-성공실패 메세지*/
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    margin-top: -0.4em; 
    margin-left: 0.25em;
    letter-spacing:0.1em;
}
/* 태블릿-성공실패 메세지*/
div.st-emotion-cache-xdw2mk.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    margin-top: -0.4em; 
    margin-left: 0.25em; 
    letter-spacing:0.1em;
}

                
/* Running... */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > label {
	font-family: 'Beeunhye';
    font-size: 1.5em;
    letter-spacing:0.1em;
}

/* Stop */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > span > button {
	font-family: 'Beeunhye';
    font-size: 1.5em;
    letter-spacing:0.1em;
}                
</style>
""", unsafe_allow_html=True)
    sss.logged_in = False
    sss.signin = False
    sss.login_error = False
    sss.find_my_id = False
    sss.find_my_pw = False

    if 'korean_mode' not in sss:
        sss.korean_mode = 1

    if (x := streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH', want_output=True)) is not None:
        if x >=1100:
            sss.screen_setting='pc'
        if 480<=x<1100:
            sss.screen_setting='tablet'
        if x < 480:
            sss.screen_setting='mobile'

    if 'many_login_attempt' not in  sss:
        sss.many_login_attempt=False
        sss.login_attempt=0

    if 'id' not in sss:
        sss.id = False
        sss.pw = False

    toggle_boolean=''
    if sss.korean_mode==1:
        toggle_boolean=False
    else:
        toggle_boolean=True
    language_selection=st.toggle('**한국어 버전 / English Version**', value=toggle_boolean)
    if not language_selection: 
        sss.korean_mode=1
        col1,col2=st.columns([7.75,2.25])
        with col1:
            if sss.screen_setting=='pc':
                st.title('')
                st.image(["https://imgur.com/w0wYl3d.png"],
        use_column_width=True)
            if sss.screen_setting=='tablet':
                st.title('')
                st.image(["https://imgur.com/dr9iqhS.png"],
        use_column_width=True)
            if sss.screen_setting=='mobile':
                st.write('')
                st.image(["https://imgur.com/H287o5n.png"],
        use_column_width=True)
        with col2:
            if sss.screen_setting=='mobile':
                pass
            else:
                st.image('https://imgur.com/CernNDq.png',use_column_width=True)
            st.markdown('<div style="text-align: right;"><p><b>로그인 해주세요</b></p></div>',unsafe_allow_html=True)        
            id = st.text_input("**아이디**") 
            password = st.text_input("**비밀번호**", type="password")
            if sss.screen_setting=='pc':
                if st.button("**로그인**", type="primary",use_container_width=True):
                    if sss.many_login_attempt==False:
                        if id == sss.id and password == sss.pw: 
                            sss.logged_in = True
                        elif id == st.secrets.user_id and password == st.secrets.user_pw:
                            sss.logged_in = True
                        else:
                            sss.login_error = True
                        if sss.login_error==True:
                            sss.login_attempt+=1
                            if sss.login_attempt>=6:
                                sss.many_login_attempt = True
                    else:
                        pass
                if st.button("**새로 오신 분**", type="secondary",use_container_width=True):
                    sss.signin = True
                col1, col2 = st.columns([5,5])
                with col1:
                    if st.button("아이디 찾기", type="secondary",use_container_width=True):
                        sss.login_attempt=0
                        sss.find_my_id = True
                with col2:
                    if st.button("비밀번호 찾기", type="secondary",use_container_width=True):
                        sss.login_attempt=0
                        sss.find_my_pw = True
            else:
                if st.button("**로그인**", type="primary",use_container_width=True):
                    if sss.many_login_attempt==False:
                        if id == sss.id and password == sss.pw:
                            sss.logged_in = True
                        elif id == st.secrets.user_id and password == st.secrets.user_pw:
                            sss.logged_in = True
                        else:
                            sss.login_error = True
                        if sss.login_error==True:
                            sss.login_attempt+=1
                            if sss.login_attempt>=6:
                                sss.many_login_attempt = True
                    else:
                        pass
                if st.button("**새로 오신 분**", type="secondary",use_container_width=True):
                        sss.signin = True
                if st.button("아이디 찾기", type="secondary",use_container_width=True):
                    sss.find_my_id = True
                if st.button("비밀번호 찾기", type="secondary",use_container_width=True):
                    sss.find_my_pw = True
        def home_logic_korean():
            if sss.get("logged_in", True):
                st.success("로그인되었습니다!",  icon="✅")
                sss.login_attempt=0
                sleep(0.5)
                st.switch_page("pages/korean_chatbot.py")
            if sss.get('login_error', True):
                if sss.login_attempt<6:
                    st.error(f"아이디 또는 비밀번호를 확인해주세요({sss.login_attempt}/5)", icon="🚨")
            if sss.get("login_error", False):
                pass
            if sss.get('signin', True):
                st.success("네리에 오신 것을 환영합니다!", icon="🧡")
                sss.many_login_attempt=False
                sss.login_attempt=0
                sleep(0.5)
                st.switch_page("pages/signin.py")
            if sss.get('many_login_attempt',True):
                    st.error("""
                            아이디 또는 패스워드를 5번 이상 틀리셨습니다.
                            
                            아이디 또는 비밀번호 찾기를 통해 정보를 수정해주세요.""", icon="🚨")
                    st.stop()
            if sss.get("signin", False):
                pass
            
            if sss.get('find_my_id', True):
                sss.many_login_attempt=False
                sss.login_attempt=0
                sss.find_my_id = False
                st.switch_page('pages/find_my_id.py')

            if sss.get('find_my_pw', True):
                sss.many_login_attempt=False
                sss.login_attempt=0
                sss.find_my_pw = False
                st.switch_page('pages/find_my_pw.py')
        if sss.screen_setting=='pc':
            col1, col2, col3=st.columns([3.3,3.4,3.3])
            with col2:
                home_logic_korean()
        if sss.screen_setting=='tablet':
            col1, col2, col3=st.columns([1,8,1])
            with col2:
                home_logic_korean()
        if sss.screen_setting=='mobile':
            col1, col2, col3=st.columns([1,9,1])
            with col2:
                home_logic_korean()
    if language_selection:
        sss.korean_mode=0
        col1,col2=st.columns([7.75,2.25])
        with col1:
            if sss.screen_setting=='pc':
                st.title('')
                st.image(["https://imgur.com/Ye5F8qs.png"],
        use_column_width=True)
            if sss.screen_setting=='tablet':
                st.title('')
                st.image(["https://imgur.com/chYXJ98.png"],
        use_column_width=True)
            if sss.screen_setting=='mobile':
                st.write('')
                st.image(["https://imgur.com/JDCESFv.png"],
        use_column_width=True)
        with col2:
            if sss.screen_setting=='mobile':
                pass
            else:
                st.image('https://imgur.com/F2P7a3I.png',use_column_width=True)
            st.markdown('<div style="text-align: right;"><p><b>Please login</b></p></div>',unsafe_allow_html=True) 
            
            id = st.text_input("**ID**")
            password = st.text_input("**Password**", type="password")
            if sss.screen_setting=='pc':
                if st.button("**Log in**", type="primary",use_container_width=True):
                    if sss.many_login_attempt==False:
                        if id == sss.id and password == sss.pw:
                            sss.logged_in = True
                        elif id == st.secrets.user_id_2 and password == st.secrets.user_pw_2:
                            sss.logged_in = True
                        else:
                            sss.login_error = True
                        if sss.login_error==True:
                            sss.login_attempt+=1
                            if sss.login_attempt>=6:
                                sss.many_login_attempt = True
                if st.button("**New User**", type="secondary",use_container_width=True):
                    sss.login_attempt=0
                    sss.signin = True
                col1, col2 = st.columns([5,5])
                with col1:
                    if st.button("Find my ID", type="secondary",use_container_width=True):
                        sss.login_attempt=0
                        sss.find_my_id = True
                with col2:
                    if st.button("Find my PW", type="secondary",use_container_width=True):
                        sss.login_attempt=0
                        sss.find_my_pw = True
            else:
                if st.button("**Log in**", type="primary",use_container_width=True):
                    if sss.many_login_attempt==False:
                        if id == sss.id and password == sss.pw:
                            sss.logged_in = True
                        elif id == st.secrets.user_id_2 and password == st.secrets.user_pw_2:
                            sss.logged_in = True
                        else:
                            sss.login_error = True
                        if sss.login_error==True:
                            sss.login_attempt+=1
                            if sss.login_attempt>=6:
                                sss.many_login_attempt = True
                if st.button("**New User**", type="secondary",use_container_width=True):
                        sss.signin = True
                if st.button("Find my ID", type="secondary",use_container_width=True):
                        sss.find_my_id = True
                if st.button("Find my PW", type="secondary",use_container_width=True):
                        sss.find_my_pw = True
        def home_logic_english():
            if sss.get("logged_in", True): 
                st.success("Logged in successfully!",  icon="✅")
                sss.login_attempt=0
                sleep(0.5)
                st.switch_page("pages/english_chatbot.py")
            if sss.get('login_error', True):
                if sss.login_attempt<6:
                    st.error(f"Incorrect ID or password({sss.login_attempt}/5)", icon="🚨")
            if sss.get("login_error", False):
                pass
            if sss.get('signin', True):
                st.success("Welcome to Neri!", icon="🧡")
                sss.many_login_attempt=False
                sss.login_attempt=0
                sleep(0.5)
                st.switch_page("pages/signin.py")
            if sss.get('many_login_attempt',True):
                st.error("""
                        You've entered your ID or password incorrectly more than 5 times.
                        
                        Please use 'Find my ID' or 'Find my PW' to correct your information.""", icon="🚨")
                st.stop()
            if sss.get("signin", False):
                pass
            if sss.get('find_my_id', True):
                sss.many_login_attempt=False
                sss.login_attempt=0
                sss.find_my_id = False
                st.switch_page('pages/find_my_id.py')
            if sss.get('find_my_pw', True):
                sss.many_login_attempt=False
                sss.login_attempt=0
                sss.find_my_pw = False
                st.switch_page('pages/find_my_pw.py')
        if sss.screen_setting=='pc':
            col1, col2, col3=st.columns([3.3,3.4,3.3])
            with col2:
                home_logic_english()
        if sss.screen_setting=='tablet':
            col1, col2, col3=st.columns([1,8,1])
            with col2:
                home_logic_english()
        if sss.screen_setting=='mobile':
            col1, col2, col3=st.columns([1,9,1])
            with col2:
                home_logic_english()            

    if sss.screen_setting=='mobile':
        st.markdown('''<p>
                    Developed By <a  href="https://i.imgur.com/JuFxv4h.png" target="_blank">Hyun Kyu Cho</a><br>
                    Made with Streamlit<br>
                    Powered By OpenAI
                    </p>''',unsafe_allow_html=True)
        st.markdown('',unsafe_allow_html=True)
        st.markdown(
            """
            <div style="bottom: 0; left: 0; width: 101%; background-color: #ffffff; color: #000000; text-align: left;">
                Developed By <a  href="https://i.imgur.com/JuFxv4h.png" target="_blank">Hyun Kyu Cho</a><br>
                Made with Streamlit<br>
                Powered By OpenAI
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #FDF6EC; color: #000000; padding: 1px; text-align: center;">
                Developed By <a  href="https://imgur.com/JuFxv4h.png" target="_blank">Hyun Kyu Cho</a>  |  Made with Streamlit  |  Powered By OpenAI
            </div>
            """,
            unsafe_allow_html=True
        ) 

