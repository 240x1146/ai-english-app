import streamlit as st
import time
import random

# -------------------------
# 設定
# -------------------------
st.set_page_config(page_title="AI English Learning", layout="wide")

st.title("🧠 AI英語学習支援アプリ（プロトタイプ）")

st.markdown("""
このアプリは以下の理論に基づいて設計されています：
- 個別最適化学習
- 建設的相互作用
- 行動分析（躊躇時間）
- 自己調整学習
""")

# -------------------------
# セッション初期化
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

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
# 疑似AI（教育設計ベース）
# -------------------------
def generate_fake_ai(user_input, level):
    
    follow_ups = {
        "beginner": [
            "Can you say that again in a simple way?",
            "Why do you like it?",
            "Can you add one more sentence?"
        ],
        "intermediate": [
            "Why do you think so?",
            "Can you explain more details?",
            "How would you say that differently?"
        ],
        "advanced": [
            "What are the deeper reasons behind that?",
            "How does that idea relate to your experience?",
            "Can you compare it with another example?"
        ]
    }

    # 簡易フィードバック
    words = user_input.split()
    
    if len(words) < 3:
        correction = "Try to make a longer sentence."
    elif not user_input.endswith("."):
        correction = "Add a period at the end."
    else:
        correction = "Good sentence! Try using more complex expressions."

    # 改善例（簡易）
    improved = user_input.capitalize()
    if not improved.endswith("."):
        improved += "."

    response = f"""
👍 Nice! I understand your idea.

✨ Better example:
{improved}

💡 Suggestion:
{correction}

❓ Question:
{random.choice(follow_ups[level])}
"""

    return response

# -------------------------
# UI（サイドバー）
# -------------------------
st.sidebar.title("📚 学習メニュー")
mode = st.sidebar.radio("モード選択", ["会話トレーニング", "ライティング分析"])

# -------------------------
# 入力
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
# チャット表示
# -------------------------
st.subheader("💬 会話履歴")

for chat in reversed(st.session_state.history):
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AI:** {chat['ai']}")
    st.markdown(f"⏱ Hesitation: {chat['hesitation']:.2f} sec")
    st.markdown(f"📈 Level: {chat['level']} / Score: {chat['score']}")
    st.markdown("---")

# -------------------------
# ダッシュボード
# -------------------------
st.subheader("📊 学習分析")

if len(st.session_state.history) > 0:
    scores = [c["score"] for c in st.session_state.history]
    hesitations = [c["hesitation"] for c in st.session_state.history]

    st.metric("会話回数", len(scores))
    st.metric("平均スコア", f"{sum(scores)/len(scores):.1f}")
    st.metric("平均躊躇時間", f"{sum(hesitations)/len(hesitations):.2f} sec")

    st.line_chart(scores)

    if sum(hesitations)/len(hesitations) > 5:
        st.warning("難易度が少し高い可能性があります → レベル調整中")
    else:
        st.success("良いペースで学習できています！")
else:
    st.write("まだデータがありません")

# -------------------------
# ナッジ機能
# -------------------------
if time.time() - st.session_state.start_time > 30:
    st.warning("⏰ 1分だけ英語やってみよう！")
