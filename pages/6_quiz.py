import streamlit as st

st.title("이름 : " + st.session_state.name)

def vote(item):
    if 'name' not in st.session_state:
        st.session_state.vote = item
    else :
        st.session_state.vote = item

if "vote" not in st.session_state:
    st.write("부산소마고에서 가장 잘생긴 사람은?")
    if st.button("박제현 선생님"):
        vote("박제현 선생님")
    if st.button("최병준 선생님"):
        vote("최병준 선생님")
    if st.button("박건우 선생님"):
        vote("박건우 선생님")
    if st.button("정종건 선생님"):
        vote("정종건 선생님")
    if st.button("오주현"):
        vote("오주현")

text = st.text_input('병자호란이 일어난 년도는?')
if st.button('저장') :
    if 'vote2' not in st.session_state:
        st.session_state.vote2 = text
    else :
        st.session_state.vote2 = text