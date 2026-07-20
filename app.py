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
        st.info("💡 受容・文法アドバイス・足場かけ・深掘り質問の4ステップで、学習者を否定せずに英語力を伸ばします。")
        
        # チャット履歴の描画
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        st.write("---")
        st.caption("【デモ用設定：以下の状態を選んで送信テストをしてみてください】")
        
        c1, c2 = st.columns(2)
        with c1:
            hesitation_level = st.radio(
                "タイピング時の状態（躊躇ログ）:",
                ["すぐに思いついて入力できた（ストレス低）", "少し迷って時間がかかった（ストレス中）"],
                index=0
            )
        with c2:
            grammar_status = st.radio(
                "入力文の文法状態（デモ用）:",
                ["文法ミスなし（正しい英文）", "少し文法ミスあり（例: 時制や前置詞のミス）"],
                index=0
            )

        # チャット入力欄
        if user_input := st.chat_input("ここに英文を入力してね... (例: I went shopping / I go to shop yesterday)"):
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # --- 4ステップ対話ロジック（文法アドバイス機能つき） ---
            
            # 1. 心理的安全性（共感）
            en_1 = "That sounds wonderful! Thank you for sharing that with me. 😊\n"
            ja_1 = "（とても素敵ですね！教えてくれてありがとうございます。😊）\n\n"
            
            # 2. 文法のアドバイス・モデリング（ミスの有無で分岐）
            if "ミスあり" in grammar_status:
                en_2 = f"💡 **One-Point Advice:**\nYour idea came through clearly! If you want to make it even more natural, you can say: **'I went to the store'** instead of '{user_input}'.\n"
                ja_2 = f"✏️ **ワンポイントアドバイス:**\n言いたいことはバッチリ伝わっています！より自然にするなら、過去のことなので動詞を過去形（went）に変えて **'I went to...'** と言うとバッチリです！\n\n"
            else:
                en_2 = f"✨ **Great Grammar!**\nYour sentence **'{user_input}'** is super natural and perfectly written!\n"
                ja_2 = f"✨ **素晴らしい英語です！**\n**'{user_input}'** はとても自然で完璧な文法ですよ！\n\n"
            
            # 3. 足場かけ（躊躇度に応じたヒント）
            if "少し迷って" in hesitation_level:
                en_3 = "💡 **Next Step Hint:**\nTry using this pattern next: **'It was [fun / busy / good].'**\n"
                ja_3 = "💡 **次のヒント:**\n迷ったときは、**'It was [感想（funなど）].'** の型を使って気持ちを教えてね！\n\n"
                st.session_state.vocab_count += 2
            else:
                en_3 = ""
                ja_3 = ""
                st.session_state.vocab_count += 4
                
            # 4. 建設的相互作用（深掘り質問）
            en_4 = "💬 **AI Question:**\nWhat was the best part of your experience? Tell me more!"
            ja_4 = "💬 **日本語訳:**\n一番良かったところはどこですか？もっと詳しく教えてください！"
            
            # 英語と日本語のブロックを結合
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
