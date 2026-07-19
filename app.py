import streamlit as st
import time
import random

# -------------------------
# 初期設定
# -------------------------
st.set_page_config(page_title="伴走型AI英語学習", layout="wide")

st.title("🧠 伴走型AI英語学習エージェント")

st.markdown("""
### コンセプト
このアプリは以下に基づく学習支援システムです：

- 建設的相互作用（対話で深く学ぶ）
- 自己調整学習（進捗の可視化）
- 社会的学習理論（AIをパートナー化）
- 行動分析（躊躇時間）
- ナッジ（行動を促す）
""")

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
    st.session_state.goal = random.choice([
        "1分だけ英語を書く",
        "Whyで答える",
        "5単語以上使う"
    ])

# -------------------------
# サイドバー（自己調整）
# -------------------------
st.sidebar.title("📊 学習コントロール")

target = st.sidebar.selectbox("今日の目標設定", ["Easy", "Normal", "Hard"])

st.sidebar.markdown(f"🎯 推奨目標: {st.session_state.goal}")

# -------------------------
# レベル推定（個別最適化）
# -------------------------
def estimate_level(text, hesitation):
    words = len(text.split())

    if hesitation > 6 or words < 4:
        return "beginner"
    elif words < 10:
        return "intermediate"
    else:
        return "advanced"

# -------------------------
# スコア（自己調整）
# -------------------------
def calc_score(text):
    words = len(text.split())
    unique = len(set(text.split()))
    return min(100, words * 5 + unique * 3)

# -------------------------
# 行動分析（弱点）
# -------------------------
def analyze_behavior(history):
    if len(history) < 3:
        return "データ蓄積中..."

    hesitation_avg = sum(h["hesitation"] for h in history) / len(history)

    if hesitation_avg > 5:
        return "👉 入力に迷いが見られます（難易度を下げます）"
    else:
        return "👉 スムーズに入力できています"

# -------------------------
# AI（伴走型・建設的相互作用）
# -------------------------
def partner_ai(text, level, hesitation):

    coach = ["いい感じ！", "その調子！", "ナイス！"]

    questions = {
        "beginner": [
            "Why do you like it?",
            "Can you add one word?"
        ],
        "intermediate": [
            "Why do you think that?",
            "Can you explain more?"
        ],
        "advanced": [
            "What is the deeper meaning?",
            "Can you compare your idea?"
        ]
    }

    # 躊躇検知 → ナッジ的ヒント
    if hesitation > 6:
        hint = "💡 ヒント: 簡単な単語でOK！"
    else:
        hint = ""

    # 改善例
    improved = text.capitalize()
    if not improved.endswith("."):
        improved += "."

    return f"""
💬 AIパートナー: {random.choice(coach)}

👍 あなたの考えは伝わっています！

✨ 改善例:
{improved}

{hint}

❓ 深掘り:
{random.choice(questions[level])}
"""

# -------------------------
# ナッジ（行動促進）
# -------------------------
if time.time() - st.session_state.start_time > 20:
    st.warning("⏰ 今がチャンス！1文だけ書いてみよう！")

# -------------------------
# 入力
# -------------------------
st.info("例：I like music")

user_input = st.text_input("英語で入力してください")

if st.button("送信") and user_input:

    hesitation = time.time() - st.session_state.start_time
    level = estimate_level(user_input, hesitation)
    score = calc_score(user_input)

    ai_reply = partner_ai(user_input, level, hesitation)

    st.session_state.history.append({
        "user": user_input,
        "ai": ai_reply,
        "hesitation": hesitation,
        "score": score,
        "level": level
    })

    st.session_state.start_time = time.time()
    st.session_state.streak += 1

# -------------------------
# 会話表示（建設的相互作用）
# -------------------------
st.subheader("💬 対話履歴")

for h in reversed(st.session_state.history):
    st.markdown(f"**You:** {h['user']}")
    st.markdown(f"**AI:** {h['ai']}")
    st.markdown(f"⏱ {h['hesitation']:.2f}s / ⭐ {h['score']} / 📈 {h['level']}")
    st.markdown("---")

# -------------------------
# ダッシュボード（自己調整）
# -------------------------
st.subheader("📊 学習ダッシュボード")

if len(st.session_state.history) > 0:
    scores = [h["score"] for h in st.session_state.history]
    hes = [h["hesitation"] for h in st.session_state.history]

    st.metric("継続回数", st.session_state.streak)
    st.metric("平均スコア", f"{sum(scores)/len(scores):.1f}")
    st.metric("平均躊躇", f"{sum(hes)/len(hes):.2f}s")

    st.line_chart(scores)

    st.info(analyze_behavior(st.session_state.history))

    # 成長可視化
    if len(scores) > 1:
        if scores[-1] > scores[0]:
            st.success("📈 成長しています！")
        else:
            st.warning("📊 継続で改善できます！")

else:
    st.write("データがまだありません")
