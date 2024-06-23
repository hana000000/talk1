import streamlit as st
import openai

# OpenAI APIキーを設定
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

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
