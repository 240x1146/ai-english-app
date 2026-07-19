import streamlit as st
import time
import random

st.set_page_config(page_title="AI English Learning", layout="wide")

st.title("🧠 AI英語学習支援アプリ（プロトタイプ）")

# セッション状態
if "history" not in st.session_state:
    st.session_state.history = []

if "start_time" not in st.session_state:
    st.session_state.start_time = None

# -------------------------
# 疑似AI応答
# -------------------------
def fake_ai_response(user_input):
    responses = [
        f"Interesting! Why do you think '{user_input}'?",
        f"Good point. Can you explain more?",
        f"I see. How would you say that differently?",
        f"Nice! Let's expand that idea."
    ]
    return random.choice(responses)

# -------------------------
# 添削（簡易）
# -------------------------
def simple_feedback(text):
    if len(text.split()) < 3:
        return "Try to make a longer sentence!"
    elif text.endswith(".") == False:
        return "Add a period at the end!"
    else:
        return "Good sentence! Maybe try using more complex words."

# -------------------------
# UI
# -------------------------
st.subheader("💬 英会話モード")

user_input = st.text_input("英語で入力してください")

if st.button("送信"):
    hesitation_time = None

    if st.session_state.start_time:
        hesitation_time = time.time() - st.session_state.start_time

    ai_reply = fake_ai_response(user_input)
    feedback = simple_feedback(user_input)

    st.session_state.history.append({
        "user": user_input,
        "ai": ai_reply,
        "feedback": feedback,
        "hesitation": hesitation_time
    })

    st.session_state.start_time = time.time()

# 初回入力タイミング
if st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# -------------------------
# 表示
# -------------------------
for chat in reversed(st.session_state.history):
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AI:** {chat['ai']}")
    st.markdown(f"📝 Feedback: {chat['feedback']}")
    if chat["hesitation"]:
        st.markdown(f"⏱ Hesitation: {chat['hesitation']:.2f} sec")
    st.markdown("---")

# -------------------------
# ダッシュボード
# -------------------------
st.subheader("📊 学習ダッシュボード")

total_messages = len(st.session_state.history)

if total_messages > 0:
    avg_hesitation = sum(
        [c["hesitation"] for c in st.session_state.history if c["hesitation"]]
    ) / total_messages

    st.metric("会話回数", total_messages)
    st.metric("平均躊躇時間", f"{avg_hesitation:.2f} sec")
else:
    st.write("まだデータがありません")
