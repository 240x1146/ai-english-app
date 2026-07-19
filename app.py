import streamlit as st
import time
import random

# -------------------------
# 初期設定
# -------------------------
st.set_page_config(page_title="AI Learning Platform", layout="wide")

# -------------------------
# セッション管理
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "goal" not in st.session_state:
    st.session_state.goal = "Write 3 sentences"

# -------------------------
# ページ切替
# -------------------------
page = st.sidebar.radio("Menu", ["🏠 Home", "💬 Training", "📊 Dashboard", "⚙ Settings"])

# -------------------------
# 共通関数
# -------------------------
def estimate_level(text, hesitation):
    wc = len(text.split())
    if hesitation > 6 or wc < 4:
        return "Beginner"
    elif wc < 10:
        return "Intermediate"
    return "Advanced"

def score(text):
    wc = len(text.split())
    uniq = len(set(text.split()))
    return min(100, wc * 5 + uniq * 3)

def analyze(history):
    if len(history) < 3:
        return "Collecting data..."
    avg_h = sum(h["hes"] for h in history)/len(history)
    return "Too difficult → Adjusting" if avg_h > 5 else "Good pace"

def coach_reply(text, level, hes):
    hints = ["Keep going!", "Nice!", "Good job!"]
    q = {
        "Beginner": ["Why?", "Add one word"],
        "Intermediate": ["Explain more", "Give example"],
        "Advanced": ["Compare ideas", "Deep reason?"]
    }
    hint = "Use simple words!" if hes > 6 else ""
    improved = text.capitalize() + ("" if text.endswith(".") else ".")
    return f"""
💬 Coach: {random.choice(hints)}

✨ Improved:
{improved}

💡 {hint}

❓ {random.choice(q[level])}
"""

# -------------------------
# HOME
# -------------------------
if page == "🏠 Home":
    st.title("🧠 AI English Learning Platform")
    st.markdown("""
### Features
- Personalized learning
- Behavior analysis
- AI coaching
- Progress visualization
""")

# -------------------------
# TRAINING
# -------------------------
if page == "💬 Training":
    st.header("💬 Training")

    user_input = st.text_input("Enter English")

    if st.button("Send") and user_input:
        hes = time.time() - st.session_state.start_time
        lvl = estimate_level(user_input, hes)
        sc = score(user_input)

        reply = coach_reply(user_input, lvl, hes)

        st.session_state.history.append({
            "user": user_input,
            "ai": reply,
            "hes": hes,
            "score": sc,
            "lvl": lvl
        })

        st.session_state.start_time = time.time()
        st.session_state.streak += 1

    for h in reversed(st.session_state.history):
        st.write("You:", h["user"])
        st.write("AI:", h["ai"])
        st.write(h["lvl"], h["score"])

# -------------------------
# DASHBOARD
# -------------------------
if page == "📊 Dashboard":
    st.header("📊 Dashboard")

    if len(st.session_state.history) > 0:
        scores = [h["score"] for h in st.session_state.history]
        hes = [h["hes"] for h in st.session_state.history]

        st.metric("Sessions", len(scores))
        st.metric("Avg Score", sum(scores)/len(scores))
        st.metric("Avg Hesitation", sum(hes)/len(hes))

        st.line_chart(scores)

        st.info(analyze(st.session_state.history))

# -------------------------
# SETTINGS
# -------------------------
if page == "⚙ Settings":
    st.header("⚙ Settings")

    st.session_state.goal = st.selectbox("Goal", [
        "Write 3 sentences",
        "Use Why",
        "Use 10 words"
    ])

    st.write("Current Goal:", st.session_state.goal)
