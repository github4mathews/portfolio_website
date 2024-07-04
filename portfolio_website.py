import streamlit as st
import google.generativeai as gai
import pandas as pd

# gai.configure(api_key="AIzaSyBhO1YbXhf9A_nCSy8fTTB-4WeLbh3CyBc")

api_key = st.secrets["GOOGLE_API_KEY"]
gai.configure(api_key=api_key)
model = gai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.write("Hi :wave")
    st.subheader("I'm Mathews P Jacob")

    col11, col12 = st.columns(2)

    LinkedIn_url = 'https://www.linkedin.com/in/mathewspjacob/'
    Instagram_url = 'https://www.linkedin.com/in/mathewspjacob/'
    with col11:
        st.markdown(f'<a href="{LinkedIn_url}" style="background-color:GreenYellow;">LinkedIn</a>',
                unsafe_allow_html=True)
    with col12:
        st.markdown(f'<a href="{Instagram_url}" style="background-color:GreenYellow;">Instagram</a>',
                unsafe_allow_html=True)

    recipient_email = 'ms4mathews@outlook.com'
    subject = 'Hello from Streamlit!'
    body = 'This is the body of the email.'

    mailto_link = f'mailto:{recipient_email}?subject={subject}&body={body}'
    # st.markdown(f'Compose Email')

    st.markdown(f'<a href="{mailto_link}"><button style="background-color:LightSkyBlue;">Compose Email</button></a>',
                unsafe_allow_html=True)

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