import streamlit as st
import openai

# OpenAI APIキーを設定
openai.api_key = st.secrets["OpenAIAPI"]["openai_api_key"]

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
st.title('しりとりマスター')
st.write('日本語で楽しいしりとりゲームをしましょう！')

# ユーザー入力
user_input = st.text_input('あなたの言葉を入力してください：')

if user_input:
    # GPTにリクエストを送信
    prompt = f"しりとりゲームをしましょう。あなたの言葉は '{user_input}' です。次の言葉を教えてください。"
    response = generate_response(prompt)
    
    # 返答を表示
    st.write('GPTの返答：')
    st.write(response)
