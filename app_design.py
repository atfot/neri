import streamlit as st

def home_design():
    return st.markdown("""
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