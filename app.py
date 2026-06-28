import streamlit as st
import time
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI英語学習アプリ")

if "history" not in st.session_state:
    st.session_state.history = []

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

user_input = st.text_input("英語で答えてください")

if user_input:
    hesitation = time.time() - st.session_state.start_time

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly English tutor."},
            {"role": "user", "content": user_input}
        ]
    )

    ai_text = response.choices[0].message.content

    st.session_state.history.append((user_input, ai_text, round(hesitation,2)))

    st.session_state.start_time = time.time()

for u, a, h in st.session_state.history:
    st.write("👤", u)
    st.write("🤖", a)
    st.caption(f"躊躇時間: {h}秒")
