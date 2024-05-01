import streamlit as st
import time

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )
st.markdown("""
<style>
@font-face {
    font-family: 'Beeunhye';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_01@1.0/Beeunhye.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

/* 메인 화면으로 */
div.block-container.st-emotion-cache-gh2jqd.ea3mdgi5 > div > div > div > div:nth-child(2) > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
}

/* share 버튼 */
div.st-emotion-cache-zq5wmm.ezrtsby0 > div > div:nth-child(1) > button > div > span {
	font-family: 'Beeunhye';
    font-size: 2em;
}

/* 타이틀 */ 
.st-emotion-cache-10trblm {
	font-family: 'Beeunhye';
    font-size: 2.25em;
}      

/* 모든 작성란 설명 */
div.block-container.st-emotion-cache-gh2jqd.ea3mdgi5 > div > div > div > div > div > label > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
}

/* 에러 메세지 */
div.block-container.st-emotion-cache-gh2jqd.ea3mdgi5 > div > div > div > div > div > div > div > div > div > div > p  {
	font-family: 'Beeunhye';
    font-size: 1.75em;
}
   
/* 이대로 저장할까요? */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div:nth-child(2) > div > button > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
}

/* 성공 메세지 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div:nth-child(3) > div > div > div > div > div > div > p {
	font-family: 'Beeunhye';
    font-size: 2em;
    font-weight: bold;
}
            
/* 바뀐 아이디 */
div.st-emotion-cache-1sdqqxz.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > div > center > b {
	font-family: 'Beeunhye';
    font-size: 2em;
}

}

</style>
""", unsafe_allow_html=True)

if st.session_state.korean_mode==1:
    st.session_state.id=st.secrets.user_id
    st.session_state.pw=st.secrets.user_pw
    st.session_state.username=st.secrets.user_name
    st.session_state.age=st.secrets.age
    st.session_state.gender=st.secrets.user_gender
    st.session_state.problem=st.secrets.problem
    st.session_state.problem_explanation=st.secrets.problem_explanation
    st.session_state.goal=st.secrets.goal
else:
    st.session_state.id=st.secrets.user_id_2
    st.session_state.pw=st.secrets.user_pw_2
    st.session_state.username=st.secrets.user_name_2
    st.session_state.age=st.secrets.age_2
    st.session_state.gender=st.secrets.user_gender_2
    st.session_state.problem=st.secrets.problem_2
    st.session_state.problem_explanation=st.secrets.problem_explanation_2
    st.session_state.goal=st.secrets.goal_2

st.session_state.filled_input=0

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')


if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>회원가입 양식</h3></center>', unsafe_allow_html=True)
    id=st.text_input('사용하실 아이디를 적어주세요.')
    if id:
        if id==st.session_state.id:
            st.error('해당 아이디가 이미 존재합니다.')
        else:
            st.session_state.id=id
            st.session_state.filled_input+=1
    password=st.text_input('사용하실 비밀번호를 적어주세요.',type='password')
    if password:
        if password==st.session_state.pw:
            st.error('해당 비밀번호가 이미 존재합니다.')
        else:
            st.session_state.pw=password
            st.session_state.filled_input+=1
    pw_check=st.text_input('다시 한번 사용하실 비밀번호를 적어주세요.',key='pw_check',type='password')
    if pw_check:
        if pw_check!=st.session_state.pw:
            st.error('해당 비밀번호와 아까 작성하신 비밀번호가 서로 다릅니다.')
        else:
            st.session_state.filled_input+=1            
    nickname=st.text_input('무슨 이름으로 불리고 싶으신가요?',key='nickname')
    if nickname:
        if nickname==st.session_state.username:
            st.error('이미 사용중인 이름입니다.')
        else:
            st.session_state.username=nickname
            st.session_state.filled_input+=1
    gender=st.selectbox('성별이 어떻게 되시죠?',('남자','여자'),placeholder='남성/여성',key='gender_')
    if gender:
        st.session_state.gender=gender
        st.session_state.filled_input+=1
    age = st.slider(
                '나이가 어떻게 되시나요?',
                7,100,30,key='age_'
                )
    if age:
        st.session_state.age=age
        st.session_state.filled_input+=1
    nationality = st.text_input('어느 나라 분이신가요?',key='nationality_')
    if nationality:
        st.session_state.nationality=nationality
        st.session_state.filled_input+=1
    city = st.text_input('어느 도시에 거주중이신가요?',key='city_')
    if city:
        st.session_state.city=city
        st.session_state.filled_input+=1
    problem = st.text_area("당신을 가장 크게 괴롭히는 것이 무엇인가요?🤔", key='problem_')
    if problem:
        st.session_state.problem=problem
        st.session_state.filled_input+=1
    problem_explanation=st.text_area("문제점을 좀더 자세히 설명해주세요. 자세히 설명해주실수록 좋아요😊", key='problem_explanation_')
    if problem_explanation:
        st.session_state.problem_explanation=problem_explanation
        st.session_state.filled_input+=1
    goal=st.text_area("최종 목표가 무엇인지 말해주세요!", key='goal_')
    if goal:
        st.session_state.goal=goal
        st.session_state.filled_input+=1      
    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('이대로 저장할까요?', type='primary',use_container_width=True):
                if st.session_state.filled_input==11:
                    st.success("""

        "좋아요! 이 내용대로 전부 저장했어요."        
        
        네리에 오신 당신을 환영합니다!

    """)
                    col1,col2=st.columns([5,5])
                    with col1:
                        st.write(f"""
    **아이디**: {st.session_state.id}

    **비밀번호**: {st.session_state.pw}

    **유저 이름**: {st.session_state.username}

    **나이**: {st.session_state.age}

    **국적**: {st.session_state.nationality}

    **도시**: {st.session_state.city}
""")
                    with col2:
                        st.write(f"""
                        **고민**: {st.session_state.problem}

                        **고민에 대한 설명**: {st.session_state.problem_explanation}

                        **목표**: {st.session_state.goal}
""")
                    time.sleep(5)
                    del st.session_state.filled_input
                    st.switch_page('streamlit_app.py')
                else: 
                    pass

if st.session_state.korean_mode==0:
    button=st.button("Go to main")
    if button:
        del st.session_state.filled_input
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>Sign in Form</h3></center>', unsafe_allow_html=True)
    id=st.text_input('Your ID')
    if id:
        if id==st.session_state.id:
            st.error('This ID already exists.')
        else:
            st.session_state.id=id
            st.session_state.filled_input+=1
    password=st.text_input('Your Password',type='password')
    if password:
        if password==st.session_state.pw:
            st.error('This password already exists.')
        else:
            st.session_state.pw=password
            st.session_state.filled_input+=1
    pw_check=st.text_input('Retype the password you want to use.',key='pw_check',type='password')
    if pw_check:
        if pw_check!=st.session_state.pw:
            st.error('This password is different from the password you wrote earlier.')
        else:
            st.session_state.filled_input+=1            
    nickname=st.text_input('Tell me the name you want to be called in here.',key='nickname')
    if nickname:
        if nickname==st.session_state.username:
            st.error('The name is already in use.')
        else:
            st.session_state.username=nickname
            st.session_state.filled_input+=1
    gender=st.selectbox('What is your gender?',('Male','Female'),placeholder='Gentleman/Lady',key='gender_')
    if gender:
        st.session_state.gender=gender
        st.session_state.filled_input+=1
    age = st.slider(
                'How old are you?',
                7,100,30,key='age_'
                )
    if age:
        st.session_state.age=age
        st.session_state.filled_input+=1
    nationality = st.text_input('Where are you from?',key='nationality_')
    if nationality:
        st.session_state.nationality=nationality
        st.session_state.filled_input+=1
    city = st.text_input('Tell me which city are you living in.',key='city_')
    if city:
        st.session_state.city=city
        st.session_state.filled_input+=1
    problem = st.text_area("What's your biggest problem right now?🤔", key='problem_')
    if problem:
        st.session_state.problem=problem
        st.session_state.filled_input+=1
    problem_explanation=st.text_area("Please describe your issue in more detail. The more details you can provide, the better😊", key='problem_explanation_')
    if problem_explanation:
        st.session_state.problem_explanation=problem_explanation
        st.session_state.filled_input+=1
    goal=st.text_area("Tell us what your end goal is!", key='goal_')
    if goal:
        st.session_state.goal=goal
        st.session_state.filled_input+=1   
    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('Do you want to save it as is?', type='primary',use_container_width=True):
                if st.session_state.filled_input==11:
                    st.success("""

        "Great! I saved everything just like this."        
        
        Welcome to Neri!

    """)
                    col1,col2=st.columns([5,5])
                    with col1:
                        st.write(f"""
    **ID**: {st.session_state.id}

    **Password**: {st.session_state.pw}

    **Username**: {st.session_state.username}

    **Age**: {st.session_state.age}

    **Nationality**: {st.session_state.nationality}

    **City**: {st.session_state.city}
""")
                    with col2:
                        st.write(f"""
                        **Problem**: {st.session_state.problem}

                        **Problem description**: {st.session_state.problem_explanation}

                        **Goal**: {st.session_state.goal}
""")
                    time.sleep(5)
                    del st.session_state.filled_input
                    st.switch_page('streamlit_app.py')
                else: 
                    pass