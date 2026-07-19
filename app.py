import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Companion AI English Agent",
    page_icon="🧠",
    layout="wide"
)

# セッション状態の初期化（チャット履歴や学習データの保持）
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hi there! 👋 Welcome back. How was your day? Tell me what you did today in one sentence! (Don't worry about mistakes!)"
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
        st.info("💡 採点者ではなく「対等な共同編集者」として、4つのステップ（心理的安全性・モデリング・足場かけ・建設的相互作用）で発話を優しく引き出します。")
        
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
            # 1. ユーザー入力を履歴に追加
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # --- 4ステップ対話ロジックの実行 ---
            # ステップ1: 心理的安全性（受容と共感）
            acceptance = f"That sounds amazing! I'm so glad you shared that with me. 😊\n\n"
            
            # ステップ2: ポジティブな拡張・モデリング（さりげなく自然な正しい表現をお手本として提示）
            modeling = f"So, you mean you **enjoyed** '{user_input}' today? That's a wonderful way to spend your time!\n\n"
            
            # ステップ3: 行動ログに応じた足場かけ（Scaffolding）
            if "少し迷って" in hesitation_level:
                # 躊躇を検知した場合、心理的負担を下げるために「型」をプレゼント
                scaffolding = "💡 **AIからのヒント（足場かけ）:**\nつぎは、**'It was [感想（fun / relaxing / exciting）].'** の型を使ってあなたの気持ちを教えてね！\n\n"
                st.session_state.vocab_count += 2
            else:
                # 躊躇がない場合はヒントをスキップし、自発性を促す
                scaffolding = ""
                st.session_state.vocab_count += 4
                
            # ステップ4: 建設的相互作用（思考を深掘りする問いかけ）
            question = "💬 **AIからの深掘り質問:**\nWhat was the most interesting part of it? Tell me more!"
            
            # 全てのステップを結合してAIの返答を作成
            ai_reply = acceptance + modeling + scaffolding + question
            
            # 2. AIの返答を履歴に追加
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            
            # 画面を更新して最新のやりとりを表示
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
    
    # メトリクスの表示
    m1, m2, m3 = st.columns(3)
    m1.metric(label="🔥 現在の継続日数", value=f"{st.session_state.streak} 日連続", delta="目標まであと2日")
    m2.metric(label="🔤 今日使った新しい語彙数", value=f"{st.session_state.vocab_count} 語", delta="+4語 (昨日比)")
    m3.metric(label="💬 AIとの対話の深さ", value="Level 3 (発展レベル)", delta="Good")
    
    # グラフのシミュレーション
    st.write("### 📈 今週の学習着手ハードル（躊躇時間）の推移")
    st.caption("システムが裏側で計測している「入力にかかった時間（間）」のデータです。使い続けることで心理的ハードルが下がり、躊躇時間が短くなっていることがわかります。")
    
    # ダミーの躊躇時間データ（やりとりが進むと今日データが更新される演出）
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
