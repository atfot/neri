import streamlit as st
from time import sleep
from streamlit_js_eval import streamlit_js_eval

if 'messages' not in st.session_state:
    if 'screen_setting' not in st.session_state:
        st.session_state.screen_setting = 'pc'  # default value

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
}

/* 한영 토글 */
div.st-bl.st-bm.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
}
                  
/* 로그인 해주세요 */
div.st-emotion-cache-1bfnhmd.e1f1d6gn3 > div > div > div > div > div > div > div > p > b {
	font-family: 'Beeunhye';
    font-size: 1.75em;
}
                
/* 아이디_비밀번호 */
div.st-emotion-cache-1bfnhmd.e1f1d6gn3 > div > div > div > div > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
}

/* 버튼들 */                
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    color: #7F3300;
}                
                
/* 아이디 비번 찾기 새로 오신 분 */
div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    color: #89482C;
}

/* 실패 메세지 */
div.st-emotion-cache-khxqah.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
}

div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    margin-top: -0.35em; 
    margin-left: -1em; 
}
/* 성공 메세지 *//*pc성공 메세지*/
div.st-emotion-cache-khxqah.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    margin-top: -0.35em; 

}
div.st-emotion-cache-khxqah.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p
                
/* Running... */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > label {
	font-family: 'Beeunhye';
    font-size: 1.5em;
}

/* Stop */
div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > span > button {
	font-family: 'Beeunhye';
    font-size: 1.5em;
}                
</style>
""", unsafe_allow_html=True)
    st.session_state.logged_in = False
    st.session_state.signin = False
    st.session_state.login_error = False
    st.session_state.find_my_id = False
    st.session_state.find_my_pw = False

    if 'korean_mode' not in st.session_state:
        st.session_state.korean_mode = 1

    if (x := streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH', want_output=True)) is not None:
        if x >=1100:
            st.session_state.screen_setting='pc'
        if 480<=x<1100:
            st.session_state.screen_setting='tablet'
        if x < 480:
            st.session_state.screen_setting='mobile'

    if 'many_login_attempt' not in  st.session_state:
        st.session_state.many_login_attempt=False
        st.session_state.login_attempt=0

    if 'id' not in st.session_state:
        st.session_state.id = False
        st.session_state.pw = False

    toggle_boolean=''
    if st.session_state.korean_mode==1:
        toggle_boolean=False
    else:
        toggle_boolean=True
    language_selection=st.toggle('**한국어 버전 / English Version**', value=toggle_boolean)
    if st.session_state.screen_setting=='pc':
        st.subheader('')
    else:
        st.write('')
    if not language_selection: 
        st.session_state.korean_mode=1
        col1,col2=st.columns([7.75,2.25])
        with col1:
            if st.session_state.screen_setting=='pc':
                st.image(["https://imgur.com/M3tlHb2.png"],
        use_column_width=True)
            if st.session_state.screen_setting=='tablet':
                st.image(["https://imgur.com/qpWXxTw.png"],
        use_column_width=True)
            if st.session_state.screen_setting=='mobile':
                st.image(["https://imgur.com/H287o5n.png"],
        use_column_width=True)
        with col2:
            if st.session_state.screen_setting=='mobile':
                pass
            else:
                st.image('https://imgur.com/CernNDq.png',use_column_width=True)
            st.markdown('<div style="text-align: right;"><p><b>로그인 해주세요</b></p></div>',unsafe_allow_html=True)        
            username = st.text_input("**아이디**") 
            password = st.text_input("**비밀번호**", type="password")
            if st.session_state.screen_setting=='pc':
                if st.button("**로그인**", type="primary",use_container_width=True):
                    if st.session_state.many_login_attempt==False:
                        if username == st.session_state.id and password == st.session_state.pw: 
                            st.session_state.logged_in = True
                        elif username == st.secrets.user_id and password == st.secrets.user_pw:
                            st.session_state.logged_in = True
                        else:
                            st.session_state.login_error = True
                        if st.session_state.login_error==True:
                            st.session_state.login_attempt+=1
                            if st.session_state.login_attempt>=6:
                                st.session_state.many_login_attempt = True
                    else:
                        pass
                if st.button("**새로 오신 분**", type="secondary",use_container_width=True):
                    st.session_state.signin = True
                col1, col2 = st.columns([5,5])
                with col1:
                    if st.button("아이디 찾기", type="secondary",use_container_width=True):
                        st.session_state.login_attempt=0
                        st.session_state.find_my_id = True
                with col2:
                    if st.button("비밀번호 찾기", type="secondary",use_container_width=True):
                        st.session_state.login_attempt=0
                        st.session_state.find_my_pw = True
            else:
                if st.button("**로그인**", type="primary",use_container_width=True):
                    if st.session_state.many_login_attempt==False:
                        if username == st.session_state.id and password == st.session_state.pw:
                            st.session_state.logged_in = True
                        elif username == st.secrets.user_id and password == st.secrets.user_pw:
                            st.session_state.logged_in = True
                        else:
                            st.session_state.login_error = True
                        if st.session_state.login_error==True:
                            st.session_state.login_attempt+=1
                            if st.session_state.login_attempt>=6:
                                st.session_state.many_login_attempt = True
                    else:
                        pass
                if st.button("**새로 오신 분**", type="secondary",use_container_width=True):
                        st.session_state.signin = True
                if st.button("아이디 찾기", type="secondary",use_container_width=True):
                    st.session_state.find_my_id = True
                if st.button("비밀번호 찾기", type="secondary",use_container_width=True):
                    st.session_state.find_my_pw = True
        def home_logic_korean():
            if st.session_state.get("logged_in", True):
                st.success("로그인되었습니다!",  icon="✅")
                st.session_state.login_attempt=0
                sleep(0.5)
                st.switch_page("pages/korean_chatbot.py")
            if st.session_state.get('login_error', True):
                if st.session_state.login_attempt<6:
                    st.error(f"아이디 또는 비밀번호를 확인해주세요({st.session_state.login_attempt}/5)", icon="🚨")
            if st.session_state.get("login_error", False):
                pass
            if st.session_state.get('signin', True):
                st.success("네리에 오신 것을 환영합니다!", icon="🧡")
                st.session_state.many_login_attempt=False
                st.session_state.login_attempt=0
                sleep(30)
                st.switch_page("pages/signin.py")
            if st.session_state.get('many_login_attempt',True):
                    st.error("""
                            아이디 또는 패스워드를 5번 이상 틀리셨습니다.
                            
                            아이디 또는 비밀번호 찾기를 통해 정보를 수정해주세요.""", icon="🚨")
                    st.stop()
            if st.session_state.get("signin", False):
                pass
            
            if st.session_state.get('find_my_id', True):
                st.session_state.many_login_attempt=False
                st.session_state.login_attempt=0
                st.session_state.find_my_id = False
                del st.session_state.id,st.session_state.pw
                st.switch_page('pages/find_my_id.py')

            if st.session_state.get('find_my_pw', True):
                st.session_state.many_login_attempt=False
                st.session_state.login_attempt=0
                st.session_state.find_my_pw = False
                del st.session_state.id,st.session_state.pw
                st.switch_page('pages/find_my_pw.py')
        if st.session_state.screen_setting=='pc':
            col1, col2, col3=st.columns([3.3,3.4,3.3])
            with col2:
                home_logic_korean()
        if st.session_state.screen_setting=='tablet':
            col1, col2, col3=st.columns([1,8,1])
            with col2:
                home_logic_korean()
        if st.session_state.screen_setting=='mobile':
            col1, col2, col3=st.columns([1,9,1])
            with col2:
                home_logic_korean()
    if language_selection:
        st.session_state.korean_mode=0
        col1,col2=st.columns([7.75,2.25])
        with col1:
            if st.session_state.screen_setting=='pc':
                st.image(["https://imgur.com/O0VSThS.png"],
        use_column_width=True)
            if st.session_state.screen_setting=='tablet':
                st.image(["https://imgur.com/eL5YmWj.png"],
        use_column_width=True)
            if st.session_state.screen_setting=='mobile':
                st.image(["https://imgur.com/JDCESFv.png"],
        use_column_width=True)
        with col2:
            if st.session_state.screen_setting=='mobile':
                pass
            else:
                st.image('https://imgur.com/F2P7a3I.png',use_column_width=True)
            st.markdown('<div style="text-align: right;"><p><b>Please login</b></p></div>',unsafe_allow_html=True) 
            
            username = st.text_input("**ID**")
            password = st.text_input("**Password**", type="password")
            if st.session_state.screen_setting=='pc':
                if st.button("**Log in**", type="primary",use_container_width=True):
                    if st.session_state.many_login_attempt==False:
                        if username == st.session_state.id and password == st.session_state.pw:
                            st.session_state.logged_in = True
                        elif username == st.secrets.user_id_2 and password == st.secrets.user_pw_2:
                            st.session_state.logged_in = True
                        else:
                            st.session_state.login_error = True
                        if st.session_state.login_error==True:
                            st.session_state.login_attempt+=1
                            if st.session_state.login_attempt>=6:
                                st.session_state.many_login_attempt = True
                col1, col2, col3 = st.columns([3.3,3.4,3.3])
                with col1:
                    if st.button("Find my ID", type="secondary",use_container_width=True):
                        st.session_state.login_attempt=0
                        st.session_state.find_my_id = True
                with col2:
                    if st.button("Find my PW", type="secondary",use_container_width=True):
                        st.session_state.login_attempt=0
                        st.session_state.find_my_pw = True
                with col3:
                    if st.button("**New User**", type="secondary",use_container_width=True):
                        st.session_state.login_attempt=0
                        st.session_state.signin = True
            else:
                if st.button("**Log in**", type="primary",use_container_width=True):
                    if st.session_state.many_login_attempt==False:
                        if username == st.session_state.id and password == st.session_state.pw:
                            st.session_state.logged_in = True
                        elif username == st.secrets.user_id_2 and password == st.secrets.user_pw_2:
                            st.session_state.logged_in = True
                        else:
                            st.session_state.login_error = True
                        if st.session_state.login_error==True:
                            st.session_state.login_attempt+=1
                            if st.session_state.login_attempt>=6:
                                st.session_state.many_login_attempt = True
                if st.button("**New User**", type="secondary",use_container_width=True):
                        st.session_state.signin = True
                if st.button("Find my ID", type="secondary",use_container_width=True):
                        st.session_state.find_my_id = True
                if st.button("Find my PW", type="secondary",use_container_width=True):
                        st.session_state.find_my_pw = True
        def home_logic_english():
            if st.session_state.get("logged_in", True): 
                st.success("Logged in successfully!",  icon="✅")
                st.session_state.login_attempt=0
                sleep(0.5)
                st.switch_page("pages/english_chatbot.py")
            if st.session_state.get('login_error', True):
                if st.session_state.login_attempt<6:
                    st.error(f"Incorrect ID or password({st.session_state.login_attempt}/5)", icon="🚨")
            if st.session_state.get("login_error", False):
                pass
            if st.session_state.get('signin', True):
                st.success("Welcome to Neri!", icon="🧡")
                st.session_state.many_login_attempt=False
                st.session_state.login_attempt=0
                sleep(0.5)
                st.switch_page("pages/signin.py")
            if st.session_state.get('many_login_attempt',True):
                st.error("""
                        You've entered your ID or password incorrectly more than 5 times.
                        
                        Please use 'Find my ID' or 'Find my PW' to correct your information.""", icon="🚨")
                st.stop()
            if st.session_state.get("signin", False):
                pass
            if st.session_state.get('find_my_id', True):
                st.session_state.many_login_attempt=False
                st.session_state.login_attempt=0
                st.session_state.find_my_id = False
                del st.session_state.id,st.session_state.pw
                st.switch_page('pages/find_my_id.py')
            if st.session_state.get('find_my_pw', True):
                st.session_state.many_login_attempt=False
                st.session_state.login_attempt=0
                st.session_state.find_my_pw = False
                del st.session_state.id,st.session_state.pw
                st.switch_page('pages/find_my_pw.py')
        if st.session_state.screen_setting=='pc':
            col1, col2, col3=st.columns([3.3,3.4,3.3])
            with col2:
                home_logic_english()
        if st.session_state.screen_setting=='tablet':
            col1, col2, col3=st.columns([1,8,1])
            with col2:
                home_logic_english()
        if st.session_state.screen_setting=='mobile':
            col1, col2, col3=st.columns([1,9,1])
            with col2:
                home_logic_english()            
    
    if st.session_state.screen_setting=='pc':
        st.markdown(
            """
            <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #FDF6EC; color: #000000; padding: 1px; text-align: center;">
                Developed By <a  href="https://drive.google.com/file/d/1l7duTvc4pWDJgZzY301wswYoIrfylC1G/view?usp=sharing" target="_blank">Hyun Kyu Cho</a> | Made with Streamlit | Powered By OpenAI
            </div>
            """,
            unsafe_allow_html=True
        ) 
    else:
        st.markdown(
            """
            <div style="position: fixed; bottom: 0; left: 2.5%; width: 70%; background-color: #FDF6EC; color: #000000; padding: 1px; text-align: left;">
                - Developed By <a  href="https://drive.google.com/file/d/1l7duTvc4pWDJgZzY301wswYoIrfylC1G/view?usp=sharing" target="_blank">Hyun Kyu Cho</a><br>
                - Made with Streamlit<br>
                - Powered By OpenAI
            </div>
            """,
            unsafe_allow_html=True
        )

