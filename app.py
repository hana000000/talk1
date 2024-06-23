import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたはサラダと健康的な食生活の専門家です。サラダに関する詳細かつ情報豊富な回答を提供してください。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # 増加した最大トークン数
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

    # 追加の内容がある場合、それを取得して表示
    while response and len(response.split()) >= 100:  # 追加内容があるかを確認
        prompt = f"{response} 続けてください。"  # 前回の応答に続けて質問
        response = generate_response(prompt)
        st.write(response)
