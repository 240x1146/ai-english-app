import streamlit as st
import time
import random

# -------------------------
# 初期設定
# -------------------------
st.set_page_config(page_title="AI English Learning", layout="wide")

st.title("🧠 AI英語学習支援アプリ（完成版プロトタイプ）")

st.markdown("""
## このアプリの特徴
- 学習行動を分析（躊躇時間）
- 個別にレベル調整
- AI風対話で思考を深める
- 学習の成長を可視化
""")

# -------------------------
# セッション初期化
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "daily_goal" not in st.session_state:
    st.session_state.daily_goal = random.choice([
        "3文以上書こう",
        "Whyで答えてみよう",
        "5単語以上使おう"
    ])

# -------------------------
# サイドバー
# -------------------------
st.sidebar.title("📚 学習メニュー")
mode = st.sidebar.radio("モード選択", ["会話トレーニング", "ライティング分析"])
st.sidebar.markdown(f"🎯 今日の目標: {st.session_state.daily_goal}")

# -------------------------
# レベル推定
# -------------------------
def estimate_level(text, hesitation):
    word_count = len(text.split())
    if hesitation > 6 or word_count < 4:
        return "beginner"
    elif word_count < 10:
        return "intermediate"
    else:
        return "advanced"

# -------------------------
# スコア計算
# -------------------------
def calculate_score(text):
    words = len(text.split())
    unique_words = len(set(text.split()))
    return min(100, words * 5 + unique_words * 3)

# -------------------------
# 弱点分析
# -------------------------
def analyze_weakness(history):
    if len(history) == 0:
        return "まだ分析データがありません"

    short_sentences = sum(1 for h in history if len(h["user"].split()) < 5)

    if short_sentences > len(history) / 2:
        return "👉 文章が短い傾向があります"
    else:
        return "👉 表現は安定しています"

# -------------------------
# 疑似AI（コーチ型）
# -------------------------
def generate_fake_ai(user_input, level):

    coaching = ["Great job!", "Nice try!", "Keep going!"]

    follow_ups = {
        "beginner": [
            "Why do you like it?",
            "Can you add one more sentence?"
        ],
        "intermediate": [
            "Why do you think so?",
            "Can you explain more?"
        ],
        "advanced": [
            "What are the deeper reasons?",
            "Can you compare this idea?"
        ]
    }

    words = user_input.split()

    if len(words) < 3:
        correction = "Try to make a longer sentence."
    elif not user_input.endswith("."):
        correction = "Add a period at the end."
    else:
        correction = "Good! Try more complex expressions."

    improved = user_input.capitalize()
    if not improved.endswith("."):
        improved += "."

    return f"""
💬 Coach: {random.choice(coaching)}

👍 Good point!

✨ Improved:
{improved}

💡 Feedback:
{correction}

❓ Question:
{random.choice(follow_ups[level])}
"""

# -------------------------
# 入力UI
# -------------------------
st.info("例：I like music")

user_input = st.text_input("英語で入力してください")

if st.button("送信") and user_input:

    hesitation_time = time.time() - st.session_state.start_time
    level = estimate_level(user_input, hesitation_time)
    score = calculate_score(user_input)

    ai_reply = generate_fake_ai(user_input, level)

    st.session_state.history.append({
        "user": user_input,
        "ai": ai_reply,
        "hesitation": hesitation_time,
        "level": level,
        "score": score
    })

    st.session_state.start_time = time.time()

# -------------------------
# 会話モード
# -------------------------
if mode == "会話トレーニング":

    st.subheader("💬 会話履歴")

    for chat in reversed(st.session_state.history):
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**AI:** {chat['ai']}")
        st.markdown(f"⏱ {chat['hesitation']:.2f} sec / 📈 {chat['level']} / ⭐ {chat['score']}")
        st.markdown("---")

# -------------------------
# ライティング分析モード
# -------------------------
if mode == "ライティング分析":

    st.subheader("✍ ライティング分析")

    if user_input:
        st.write("スコア:", calculate_score(user_input))

    st.warning(analyze_weakness(st.session_state.history))

# -------------------------
# ダッシュボード
# -------------------------
st.subheader("📊 学習ダッシュボード")

if len(st.session_state.history) > 0:
    scores = [c["score"] for c in st.session_state.history]
    hesitations = [c["hesitation"] for c in st.session_state.history]

    st.metric("会話回数", len(scores))
    st.metric("平均スコア", f"{sum(scores)/len(scores):.1f}")
    st.metric("平均躊躇時間", f"{sum(hesitations)/len(hesitations):.2f} sec")

    st.line_chart(scores)

    if len(scores) > 1:
        if scores[-1] > scores[0]:
            st.success("📈 成長しています！")
        else:
            st.info("📊 継続して改善しましょう！")
else:
    st.write("まだデータがありません")

# -------------------------
# ナッジ機能
# -------------------------
if time.time() - st.session_state.start_time > 20:
    st.warning("⏰ 今がチャンス！1文だけ書いてみよう！")
