import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": \
                 "あなたはサラダと健康的な食生活の専門家です。サラダに関する詳細かつ情報豊富な回答を提供してください。"\
                 
                
                
                
                
                
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,  # 増加した最大トークン数
            temperature=0.5,
        )
        message = response.choices[0].message['content'].strip()
        return message
    except openai.error.InvalidRequestError as e:
        return f"Error: {e}"

# Streamlitアプリの設定
st.title('サラダバー勧誘ゲーム')
st.write('普段野菜を食べないあなたの同僚に、サラダバーの利用をすすめてください。')
st.write('相手は３０歳男性独身、健康診断で異常を指摘されたことはありません。')
st.write('そんな同僚に、今後の健康のことを考えて一緒にサラダバーを利用するよう誘ってください。')
st.write('会話のターン５回までに、サラダバーの利用を承諾させてください。')


# ユーザー入力
user_input = st.text_input('質問を入力してください：')

if user_input:
    # GPTにリクエストを送信
    prompt = f"サラダバーを同僚に勧めています：{user_input}"
    response = generate_response(prompt)
    
    # 返答を表示
    st.write('同僚の返答：')
    st.write(response)

    # 追加の内容がある場合、それを取得して表示
    while response and len(response.split()) >= 100:  # 追加内容があるかを確認
        prompt = f"{response} 続けてください。"  # 前回の応答に続けて質問
        response = generate_response(prompt)
        st.write(response)
