import streamlit as st
import openai

# OpenAI APIキーの設定
openai.api_key = st.secrets["OpenAIAPI"]["openai_api_key"]

st.title("GPT Integration Example")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(response.choices[0].message['content'].strip())
    except openai.error.OpenAIError as e:
        st.error(f"An error occurred: {e}")
