import streamlit as st
import time
import random

st.set_page_config(page_title="AI英語学習", layout="centered")

# セッション管理
if "history" not in st.session_state:
    st.session_state.history = []

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "level" not in st.session_state:
    st.session_state.level = "A1"

# --- タイトル ---
st.title("📱 AI英語学習エージェント（デモ版）")

# --- ナッジ ---
st.subheader("今日のクイック英会話（30秒）")
st.info("👉 Do you like studying English? Why?")

# --- 疑似AI応答関数 ---
def fake_ai_response(user_input, level):
    responses_easy = [
        "Nice! Why do you think so?",
        "Great! Tell me more.",
        "I see! Can you explain a bit more?"
    ]

    responses_medium = [
        "That's interesting. Can you give an example?",
        "Good point! Why do you feel that way?",
        "I like your idea. Could you expand on that?"
    ]

    corrections = [
        "Tip: You can say 'I like it because...' 😊",
        "Tip: Try using 'because' to explain your reason!",
        "Tip: Add more details to make your sentence stronger!"
    ]

    if level == "A1":
        response = random.choice(responses_easy)
    else:
        response = random.choice(responses_medium)

    tip = random.choice(corrections)

    return response + "\n\n💡 " + tip

# --- 入力 ---
user_input = st.text_input("✍️ 英語で答えてください")

if user_input:
    hesitation = time.time() - st.session_state.start_time

    # 疑似AI
    ai_text = fake_ai_response(user_input, st.session_state.level)

    # レベル調整
    if hesitation < 3:
        st.session_state.level = "A2"
    elif hesitation > 8:
        st.session_state.level = "A1"

    # 保存
    st.session_state.history.append({
        "user": user_input,
        "ai": ai_text,
        "hesitation": round(hesitation, 2)
    })

    st.session_state.start_time = time.time()

# --- 会話表示 ---
st.subheader("💬 会話履歴")

for h in st.session_state.history:
    st.markdown(f"**👤 You:** {h['user']}")
    st.markdown(f"**🤖 AI:** {h['ai']}")
    st.caption(f"⏱ 躊躇時間: {h['hesitation']}秒")

# --- ダッシュボード ---
st.subheader("📊 学習ダッシュボード")

st.write(f"発話数: {len(st.session_state.history)}")
st.write(f"現在レベル: {st.session_state.level}")

if st.session_state.history:
    avg = sum([h["hesitation"] for h in st.session_state.history]) / len(st.session_state.history)
    st.write(f"平均躊躇時間: {round(avg,2)}秒")

    if avg < 4:
        st.success("💡 スムーズに英語が出ています！")
    else:
        st.warning("💡 少し考えながら進めています")
