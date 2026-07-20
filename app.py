import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Companion AI English Agent",
    page_icon="🧠",
    layout="wide"
)

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hi there! 👋 Welcome back. How was your day? Tell me what you did today in one sentence! (Don't worry about mistakes!)\n\n"
                       "--- \n"
                       "（こんにちは！👋 おかえりなさい。今日はどんな1日でしたか？今日したことを1つの文で教えてね！間違いは気にしなくて大丈夫だよ！）"
        }
    ]
if "streak" not in st.session_state:
    st.session_state.streak = 5
if "vocab_count" not in st.session_state:
    st.session_state.vocab_count = 12

# タイトル表示
st.title("伴走型AI英語学習エージェント (Demo)")
st.caption("行動分析 ✕ 自己調整学習 ✕ 建設的相互作用 に基づく学習支援ツール")

# タブの構築
tab1, tab2 = st.tabs(["💬 AI対話・ナッジ（メイン機能）", "📊 自己調整学習ダッシュボード"])

# ==========================================
# タブ1: AI対話モジュール & ナッジエンジン
# ==========================================
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Situation-Adaptive AI Conversation")
        st.info("💡 4つのステップ（心理的安全性・モデリング・足場かけ・建設的相互作用）に沿って、英語と日本語を同時に出力します。")
        
        # チャット履歴の描画
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        st.write("---")
        st.caption("【デモ用設定：あなたのタイピング時の心理状態を選んで送信してください】")
        hesitation_level = st.radio(
            "文字を入力する際、どのくらい迷いましたか？（行動ログ・躊躇時間のシミュレート）",
            ["すぐに思いついて入力できた（ストレス低・躊躇なし）", "単語や文法に少し迷って時間がかかった（ストレス中・躊躇あり）"],
            index=0
        )

        # チャット入力欄
        if user_input := st.chat_input("ここに英文を入力してね... (例: I went shopping / I watched a movie)"):
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # --- 4ステップ対話ロジック（日英ハイブリッド版） ---
            
            # ステップ1: 心理的安全性（受容と共感）
            en_1 = f"That sounds amazing! I'm so glad you shared that with me. 😊\n"
            ja_1 = f"（それは素敵ですね！教えてくれてとても嬉しいです。😊）\n\n"
            
            # ステップ2: ポジティブな拡張・モデリング（正しい表現のお手本提示）
            en_2 = f"So, you mean you **enjoyed** '{user_input}' today? That's a wonderful way to spend your time!\n"
            ja_2 = f"（つまり、今日は「{user_input}」を**楽しんだ**のですね？とても素晴らしい時間の過ごし方です！）\n\n"
            
            # ステップ3: 行動ログに応じた足場かけ（Scaffolding）
            if "少し迷って" in hesitation_level:
                en_3 = "💡 **AI Hints:**\nNext, try to use this pattern to tell me your feelings: **'It was [感想（fun / relaxing / exciting）].'**\n"
                ja_3 = "💡 **日本語解説:**\n入力に少し迷ったみたいだね。次は、**'It was [感想].'**（楽しかった、リラックスした、ワクワクしたなど）の型を使って気持ちを教えてね！\n\n"
                st.session_state.vocab_count += 2
            else:
                en_3 = ""
                ja_3 = ""
                st.session_state.vocab_count += 4
                
            # ステップ4: 建設的相互作用（思考を深掘りする問いかけ）
            en_4 = "💬 **AI Question:**\nWhat was the most interesting part of it? Tell me more!"
            ja_4 = "💬 **日本語訳:**\nそれのどこが一番おもしろかった？もっと詳しく教えて！"
            
            # 英語セクションと日本語セクションを綺麗に分けて結合
            ai_reply = (
                "### 🇬🇧 AI Response\n"
                f"{en_1}{en_2}{en_3}{en_4}\n\n"
                "--- \n"
                "### 🇯🇵 日本語の翻訳とサポート\n"
                f"{ja_1}{ja_2}{ja_3}{ja_4}"
            )
            
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            st.rerun()

    with col2:
        st.subheader("🔔 ナッジエンジン（行動ログ）")
        st.write("ユーザーのスマホ起動時間や隙間時間を狙い、心理的ハードルの低い「1分クイック通知」を送る仕組みです。")
        
        st.success("🤖 **AIからのナッジ通知（例）**\n\n「通学電車に乗りましたね！お疲れ様です。5秒で答えられる質問が届いています。ワンタップで始めよう！」")
        if st.button("通知をタップしてクイック会話を起動"):
            st.toast("ワンタップで会話モジュールが起動しました！")

# ==========================================
# タブ2: 自己調整学習支援ダッシュボード
# ==========================================
with tab2:
    st.subheader("Self-Regulated Learning Dashboard")
    st.write("点数で裁くのではなく、**継続やプロセス**を可視化して学習者の内発的動機づけを高めます。")
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="🔥 現在の継続日数", value=f"{st.session_state.streak} 日連続", delta="目標まであと2日")
    m2.metric(label="🔤 今日使った新しい語彙数", value=f"{st.session_state.vocab_count} 語", delta="+4語 (昨日比)")
    m3.metric(label="💬 AIとの対話の深さ", value="Level 3 (発展レベル)", delta="Good")
    
    st.write("### 📈 今週の学習着手ハードル（躊躇時間）の推移")
    st.caption("システムが裏側で計測している「入力にかかった時間（間）」のデータです。使い続けることで心理的ハードルが下がり、躊躇時間が短くなっていることがわかります。")
    
    chart_data = {
        "月曜日": 18,
        "火曜日": 15,
        "水曜日": 12,
        "木曜日": 14,
        "金曜日": 9,
        "土曜日": 7,
        "今日": 5 if len(st.session_state.messages) > 1 else 11
    }
    st.line_chart(chart_data)
    
    st.info("🎯 **自己調整へのナッジ:** 「今週は文字入力までの迷う時間が平均8秒も短くなりました！あなたの脳が英語の『型』に慣れてきた証拠です。明日は少し長めの文章にチャレンジしてみませんか？」")
