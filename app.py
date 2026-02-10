import streamlit as st
import random

# タイトルを表示
st.title("おみくじアプリ ⛩️")

# 説明文を表示
st.write("ボタンを押して、今日の運勢を占いましょう！")

# ボタンが押されたときの処理
if st.button("おみくじを引く"):
    # おみくじの結果リスト
    results = ["大吉", "中吉", "小吉"]
    # ランダムに結果を選ぶ
    result = random.choice(results)
    
    # 結果を大きく表示 (Markdownを使用)
    st.markdown(f"## 結果は... **{result}** です！")
