import streamlit as st
import time
from streamlit import session_state as sss

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )
st.markdown(st.secrets.signin_idpw_css, unsafe_allow_html=True)
if sss.korean_mode==1:
    if 'username' in sss:
        del sss.id, sss.pw, sss.username, sss.age, sss.gender, sss.problem, sss.problem_explanation, sss.goal
    else:
        pass
    if 'id' in sss:
        del sss.id, sss.pw
    else:
        pass
    if 'id' not in sss:
        sss.id=st.secrets.user_id
        sss.pw=st.secrets.user_pw
        sss.username=st.secrets.user_name
        sss.age=st.secrets.age
        sss.gender=st.secrets.user_gender
        sss.problem=st.secrets.problem
        sss.problem_explanation=st.secrets.problem_explanation
        sss.goal=st.secrets.goal
else:
    if 'id' in sss:
        if 'username' in sss:
            del sss.id, sss.pw, sss.username, sss.age, sss.gender, sss.problem, sss.problem_explanation, sss.goal
        else:
            del sss.id, sss.pw
    if 'id' not in sss:
        sss.id=st.secrets.user_id_2
        sss.pw=st.secrets.user_pw_2
        sss.username=st.secrets.user_name_2
        sss.age=st.secrets.age_2
        sss.gender=st.secrets.user_gender_2
        sss.problem=st.secrets.problem_2
        sss.problem_explanation=st.secrets.problem_explanation_2
        sss.goal=st.secrets.goal_2

sss.filled_input=0

if 'korean_mode' not in sss:
    st.switch_page('streamlit_app.py')


if sss.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        if 'id' in sss:
            del sss.id
        else:
            pass
        if 'pw' in sss:
            del sss.pw
        else:
            pass
        if 'username' in sss:
            del sss.username
        else:
            pass
        if 'filled_input' in sss:
            del sss.filled_input
        else:
            pass
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>회원가입 양식</h3></center>', unsafe_allow_html=True)
    id=st.text_input('사용하실 아이디를 적어주세요.')
    if id:
        if id==sss.id:
            st.error('해당 아이디가 이미 존재합니다.')
        else:
            sss.id=''
            sss.id=id
            sss.filled_input+=1
    password=st.text_input('사용하실 비밀번호를 적어주세요.',type='password')
    if password:
        if password==sss.pw:
            st.error('해당 비밀번호가 이미 존재합니다.')
        else:
            sss.pw=''
            sss.pw=password
            sss.filled_input+=1
    pw_check=st.text_input('다시 한번 사용하실 비밀번호를 적어주세요.',key='pw_check',type='password')
    if pw_check:
        if pw_check!=sss.pw:
            st.error('해당 비밀번호와 아까 작성하신 비밀번호가 서로 다릅니다.')
        else:
            sss.filled_input+=1            
    nickname=st.text_input('무슨 이름으로 불리고 싶으신가요?',key='nickname')
    if nickname:
        if nickname==sss.username:
            st.error('이미 사용중인 이름입니다.')
        else:
            sss.username=''
            sss.username=nickname
            sss.filled_input+=1
    gender=st.selectbox('성별이 어떻게 되시죠?',('남자','여자'),placeholder='남성/여성',key='gender_')
    if gender:
        sss.gender=''
        sss.gender=gender
        sss.filled_input+=1
    age = st.slider(
                '나이가 어떻게 되시나요?',
                7,100,30,key='age_'
                )
    if age:
        sss.age=''
        sss.age=age
        sss.filled_input+=1
    nationality = st.text_input('어느 나라 분이신가요?',key='nationality_')
    if nationality:
        sss.nationality=''
        sss.nationality=nationality
        sss.filled_input+=1
    city = st.text_input('어느 도시에 거주중이신가요?',key='city_')
    if city:
        sss.city=''
        sss.city=city
        sss.filled_input+=1
    problem = st.text_area("당신을 가장 크게 괴롭히는 것이 무엇인가요?🤔", key='problem_')
    if problem:
        sss.problem=''
        sss.problem=problem
        sss.filled_input+=1
    problem_explanation=st.text_area("문제점을 좀더 자세히 설명해주세요. 자세히 설명해주실수록 좋아요😊", key='problem_explanation_')
    if problem_explanation:
        sss.problem_explanation=''
        sss.problem_explanation=problem_explanation
        sss.filled_input+=1
    goal=st.text_area("최종 목표가 무엇인지 말해주세요!", key='goal_')
    if goal:
        sss.goal=''
        sss.goal=goal
        sss.filled_input+=1      
    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('이대로 저장할까요?', type='primary',use_container_width=True):
                if sss.filled_input==11:
                    st.success("""

        "좋아요! 이 내용대로 전부 저장했어요."        
        
        네리에 오신 당신을 환영합니다!

    """)
                    if 'user_info' not in sss:
                        sss.user_info=True
                else: 
                    pass
    if 'user_info' in sss:
        col1,col2=st.columns([5,5])
        with col1:
            st.write(f"""
**아이디**: {sss.id}

**비밀번호**: {sss.pw}

**유저 이름**: {sss.username}

**나이**: {sss.age}

**국적**: {sss.nationality}

**도시**: {sss.city}
""")
        with col2:
            st.write(f"""
            **고민**: {sss.problem}

            **고민에 대한 설명**: {sss.problem_explanation}

            **목표**: {sss.goal}
""")
        time.sleep(60)
        del sss.filled_input,sss.user_info
        st.switch_page('streamlit_app.py')

if sss.korean_mode==0:
    button=st.button("Go to main")
    if button:
        if 'id' in sss:
            del sss.id
        else:
            pass
        if 'pw' in sss:
            del sss.pw
        else:
            pass
        if 'username' in sss:
            del sss.Username
        else:
            pass
        if 'filled_input' in sss:
            del sss.filled_input
        else:
            pass
        st.switch_page("streamlit_app.py")
    st.markdown('<center><h3>Sign in Form</h3></center>', unsafe_allow_html=True)
    id=st.text_input('Your ID')
    if id:
        if id==sss.id:
            st.error('This ID already exists.')
        else:
            sss.id=''
            sss.id=id
            sss.filled_input+=1
    password=st.text_input('Your Password',type='password')
    if password:
        if password==sss.pw:
            st.error('This password already exists.')
        else:
            sss.pw=''
            sss.pw=password
            sss.filled_input+=1
    pw_check=st.text_input('Retype the password you want to use.',key='pw_check',type='password')
    if pw_check:
        if pw_check!=sss.pw:
            st.error('This password is different from the password you wrote earlier.')
        else:
            sss.filled_input+=1            
    nickname=st.text_input('Tell me the name you want to be called in here.',key='nickname')
    if nickname:
        if nickname==sss.username:
            st.error('The name is already in use.')
        else:
            sss.username=''
            sss.username=nickname
            sss.filled_input+=1
    gender=st.selectbox('What is your gender?',('Male','Female'),placeholder='Gentleman/Lady',key='gender_')
    if gender:
        sss.gender=''
        sss.gender=gender
        sss.filled_input+=1
    age = st.slider(
                'How old are you?',
                7,100,30,key='age_'
                )
    if age:
        sss.age=''
        sss.age=age
        sss.filled_input+=1
    nationality = st.text_input('Where are you from?',key='nationality_')
    if nationality:
        sss.nationality=''
        sss.nationality=nationality
        sss.filled_input+=1
    city = st.text_input('Tell me which city are you living in.',key='city_')
    if city:
        sss.city=''
        sss.city=city
        sss.filled_input+=1
    problem = st.text_area("What's your biggest problem right now?🤔", key='problem_')
    if problem:
        sss.problem=''
        sss.problem=problem
        sss.filled_input+=1
    problem_explanation=st.text_area("Please describe your issue in more detail. The more details you can provide, the better😊", key='problem_explanation_')
    if problem_explanation:
        sss.problem_explanation=problem_explanation
        sss.filled_input+=1
    goal=st.text_area("Tell us what your end goal is!", key='goal_')
    if goal:
        sss.goal=''
        sss.goal=goal
        sss.filled_input+=1   
    col1,col2,col3=st.columns([1,8,1])
    with col2:
        st.title('')
        if st.button('Do you want to save it as is?', type='primary',use_container_width=True):
                if sss.filled_input==11:
                    st.success("""

        "Great! I saved everything just like this."        
        
        Welcome to Neri!

    """)
                    if 'user_info' not in sss:
                        sss.user_info=True 
                else: 
                    pass
    if 'user_info' in sss:
        col1,col2=st.columns([5,5])
        with col1:
            st.write(f"""
        **ID**: {sss.id}

        **Password**: {sss.pw}

        **Username**: {sss.username}

        **Age**: {sss.age}

        **Nationality**: {sss.nationality}

        **City**: {sss.city}
        """)
        with col2:
            st.write(f"""
            **Problem**: {sss.problem}

            **Problem description**: {sss.problem_explanation}

            **Goal**: {sss.goal}
        """)
        time.sleep(5)
        del sss.filled_input,sss.user_info
        st.switch_page('streamlit_app.py')
    else:
        pass