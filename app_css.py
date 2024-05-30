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
div.st-emotion-cache-15ecox0.ezrtsby0 > div > div > button > div > span {
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

def app_design():
    return st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* share 버튼 */
div.st-emotion-cache-15ecox0.ezrtsby0 > div > div > button > div > span {
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
span.st-emotion-cache-rkv7nx.e11k5jya0 > div > p {
	font-family: 'Beeunhye';
	font-size: 1.75em;
    margin-top: -0.15em; 
    margin-left: 0.25em; 
    letter-spacing:0.075em;
}       

/* 로그아웃 버튼 */
div.st-emotion-cache-qeahdt.eczjsme9 > div > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
	font-size: 2em;
    letter-spacing:0.075em;
}     

/* 로그아웃 메세지 */      
div.st-emotion-cache-qeahdt.eczjsme9 > div > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
	font-size: 1.5em;
    letter-spacing:0.075em;
}

/* 챗봇 */  
/* 챗봇 글씨체 */
div.st-emotion-cache-1dp44rk.eeusbqq3 > div > div > div > div > div > div > p {
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
                    
/* 오류 제보 */
/* 기본 메세지 */
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
/* 성공 실패 메세지*/
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
                    
/* 내 정보 */
/* 내 프로필 */
.st-emotion-cache-10trblm {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
/* 프로필 내역 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
/* 수정란 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > label > div > p{
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}

/* 내 정보 수정 버튼 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > button > div > p {
font-family: 'Beeunhye';
font-size: 2em;
letter-spacing:0.075em;
}
/* 성공 실패 메세지 */
div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p > strong {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
                    
/* 심리분석 결과 */
/* 리스트 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > ol > li {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
/* 버튼 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > button > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
/* 전송중... */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}
/*성공 메세지 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
font-family: 'Beeunhye';
font-size: 1.75em;
letter-spacing:0.075em;
}

</style>
"""

, unsafe_allow_html=True)

def find_my_idpw_design():
    return st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

/* 메인 화면으로 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* share 버튼 */
div.st-emotion-cache-15ecox0.ezrtsby0 > div > div > button > div > span {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* 타이틀 */ 
h3 {
	font-family: 'Beeunhye';
    font-size: 3em;
    letter-spacing:0.075em;
}      

/* 모든 작성란 설명 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* 에러 메세지 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p  {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.075em;
}
   
/* 이대로 저장할까요? */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

/* 성공 메세지 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}
div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}
            
/* 바뀐 아이디 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > center > b {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

/* 회원가입 저장내역 */
div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

</style>
""", unsafe_allow_html=True)

def signup_design():
    return st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

/* 메인 화면으로 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* share 버튼 */
div.st-emotion-cache-15ecox0.ezrtsby0 > div > div > button > div > span {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* 타이틀 */ 
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > center > div {
	font-family: 'Beeunhye';
    font-size: 2.25em;
    letter-spacing:0.075em;
}      

/* 모든 작성란 설명 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}

/* 에러 메세지 */
div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p  {
	font-family: 'Beeunhye';
    font-size: 1.75em;
    letter-spacing:0.075em;
}
   
/* 이대로 저장할까요? */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

/* 성공 메세지 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}
div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
    letter-spacing:0.075em;
}
            
/* 바뀐 아이디 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div > div > div > center > b {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

/* 회원가입 저장내역 */
div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    letter-spacing:0.075em;
}

</style>
""", unsafe_allow_html=True)