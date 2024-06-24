import streamlit as st
import openai

# OpenAI APIキーの設定
openai.api_key = st.secrets["OpenAIAPI"]["openai_api_key"]

st.title("GPT Integration Example")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    st.write(response.choices[0].text)
