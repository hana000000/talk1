import streamlit as st
import openai

# OpenAI APIキーの設定
openai.api_key = st.secrets["OpenAIAPI"]["openai_api_key"]

st.title("GPT Integration Example")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        st.write(response.choices[0].text.strip())
    except openai.error.OpenAIError as e:
        st.error(f"An error occurred: {e}")
