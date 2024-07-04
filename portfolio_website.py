import streamlit as st
import google.generativeai as gai

api_key = st.secrets["AIzaSyBhO1YbXhf9A_nCSy8fTTB-4WeLbh3CyBc"]

gai.configure(api_key=api_key)
model = gai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave")
    st.title("I'm Mathews P Jacob")

with col2:
    st.image("./images/18.png")

st.write(" ")

persona = """ You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza) """

st.title("Mathew's AI Bot")
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user is asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.write(" ")

col1, col2 = st.columns(2)

with col1:
    st.subheader("My Youtube channel")
    st.write("- Largest IOT.Net + AI Channel")
    st.write("- Now 0 Subscribers")
    st.write("- Planning to do Free Tutorials")
    st.write("- 0 Views")

with col2:
    st.video("https://www.youtube.com/watch?v=1XT85-nNRyM&ab_channel=LittleChill")

st.write(" ")

st.title("My Setup")
st.image("./images/g/23.jpg")

st.write(" ")

st.title("My Skills")
st.slider("Embedded C/CPP", 0, 100, 80)
st.slider(".Net Core API", 0, 100, 90)
st.slider("WinForms", 0, 100, 90)
st.slider("MAUI", 0, 100, 80)
st.slider("Blazor", 0, 100, 80)
st.slider("PLC Programming", 0, 100, 60)
st.slider("MVTech Halcon CV", 0, 100, 80)

st.write(" ")

st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("./images/g/1.jpg")
    st.image("./images/g/2.png")
    st.image("./images/g/3.jpg")
with col2:
    st.image("./images/g/4.png")
    st.image("./images/g/5.jpg")
    st.image("./images/g/6.jpg")
with col3:
    st.image("./images/g/7.jpg")
    st.image("./images/g/8.jpg")
    st.image("./images/g/9.jpg")

st.write(" ")
st.subheader("Contact")
st.title("For any inquiries, email at:")
st.write("ms4mathews@outlook.com")