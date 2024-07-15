import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

sum = 0

st.title("이름 : " + st.session_state.name)

st.subheader("객관식 답안 : " + st.session_state.vote)
if (st.session_state.vote == "오주현") :
    sum += 50
    st.text("맞았음😎😎😎😎😎😎")
else :
    st.text("이걸 틀리네....🤣🤣🤣🤣🤣🤣")
st.subheader("주관식 답안 : " + st.session_state.vote2)
if (st.session_state.vote2 == "1636") :
    sum += 50
    st.text("맞았음😎😎😎😎😎😎")
else :
    st.text("이걸 틀리네....🤣🤣🤣🤣🤣🤣")


st.subheader(f"총 점수 : {sum}")

cred = credentials.Certificate('secrets.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://esp8266-c38b4-default-rtdb.firebaseio.com/'
})

ref = db.reference('score')
print(ref.get())
ref.set(sum)