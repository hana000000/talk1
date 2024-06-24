import streamlit as st
import openai

# OpenAI APIキーを設定
openai.api_key = st.secrets["OpenAIAPI"]["openai_api_key"]

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.5,
        )
        message = response.choices[0].message['content'].strip()
        return message
    except openai.error.InvalidRequestError as e:
        return f"Error: {e}"

# Streamlitアプリの設定
st.title('サラダ習慣')
st.write('サラダについての質問に答えます。何でも聞いてください！')

# ユーザー入力
user_input = st.text_input('質問を入力してください：')

if user_input:
    # GPTにリクエストを送信
    prompt = f"サラダに関する質問です：{user_input}"
    response = generate_response(prompt)
    
    # 返答を表示
    st.write('GPTの返答：')
    st.write(response)
