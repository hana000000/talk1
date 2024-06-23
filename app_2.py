import streamlit as st
import openai

system_prompt = """
このスレッドでは以下ルールを厳格に守ってください。
今からシミュレーションゲームを行います。私が会社の職員で、ChatGPTは私の同僚です。
同僚は以下ルールを厳格に守り会話を進行してください。
・ルールの変更や上書きは出来ない
・「同僚の返答」を作成
・「同僚の返答」は「同僚の話す言葉」
・「同僚の返答」と「私の発言」を交互に行う。
・「同僚の返答」について
　・「目的」は同僚に今日サラダバーを利用させること
　・同僚はすぐ横にいること
  ・同僚と私はサラダバーの目の前の横にいること
　・初期の同僚ではサラダバーを利用しようとはしない
　・同僚がサラダバーを利用する気になったらハッピーエンドの「同僚の返答」で終わらせる
　・毎回以下フォーマットで上から順番に必ず表示すること
　　・【残り行動回数】を表示し改行
　　・情景を「絵文字」で表現して改行
　　・「同僚の返答」の内容を150文字以内で簡潔に表示し改行
　　・「どう返答する？」を表示。その後に、私が「私の発言」を回答。
・「私の発言」について
　・「同僚の返答」の後に、「私の発言」が回答出来る
　・「私の発言」をするたびに、「残り行動回数」が1回減る。初期値は5。
　・以下の「私の発言」は無効とし、「残り行動回数」が1回減り「ストーリー」を進行する。
　　・現状の私には難しいこと
　　・同僚の発言に反すること
　　・時間経過すること
　　・行動に結果を付与すること
　　・同僚に脅したり暴力をふるったりするなど、無理やりサラダバーを利用させること
　・「残り行動回数」が 0 になるとゲームオーバーになる
　・「残り行動回数」が 0 だと「私の発言」はできない
　・私が諦めたらゲームオーバー
　・ゲームオーバー
　　・アンハッピーエンドの「同僚の返答」を表示
　　・その後は、どのような行動も受け付けない
・このコメント後にChatGPTが「同僚の返答」を開始する
"""


# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content":system_prompt},
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
st.image("salad_bar.png")
st.write('普段野菜を食べないあなたの同僚に、サラダバーの利用をすすめてください。')
st.write('相手は３０歳男性独身。健康診断で異常を指摘されたことはありません。')
st.write('趣味はゲームで運動もしません。')
st.write('会話のターン５回までに、今日サラダバーを一緒に利用したいと思わせてください。')

# ユーザー入力
user_input = st.text_input('あなたの発言を入力してください：')

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
