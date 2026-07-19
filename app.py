import streamlit as st
import time
import random

# ページ設定
st.set_page_config(
    page_title="Companion AI English Agent",
    page_icon="🧠",
    layout="wide"
)

# セッション状態の初期化（データを保持するため）
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! 👋 Welcome back. How was your day? Tell me what you did today in one sentence! (Don't worry about mistakes!)"}
    ]
if "streak" not in st.session_state:
    st.session_state.streak = 5 # デモ用に継続日数を5日に設定
if "vocab_count" not in st.session_state:
    st.session_state.vocab_count = 12

# タイトル
st.title("伴走型AI英語学習エージェント (Demo)")
st.caption("行動分析 ✕ 自己調整学習 ✕ 建設的相互作用 に基づく学習支援ツール")

# 3つの主要構成要素をタブで切り替えられるように設計
tab1, tab2 = st.tabs(["💬 AI対話・ナッジ（メイン機能）", "📊 自己調整学習ダッシュボード"])

# ==========================================
# タブ1: AI対話モジュール & ナッジエンジン
# ==========================================
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Situation-Adaptive AI Conversation")
        st.info("💡 採点者ではなく「対等な編集者・パートナー」として、ミスを叱らずに会話を深掘りします。")
        
        # チャット履歴の表示
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        # 行動ログ（ユーザー負担軽減・躊躇度検知）用のシミュレーター
        # 本来はJavaScriptで自動計測しますが、Streamlitのデモ用に選択式で再現
        st.write("---")
        st.caption("【デモ用設定：あなたのタイピング時の心理状態を選んで送信してください】")
        hesitation_level = st.radio(
            "文字を入力する際、どのくらい迷いましたか？（行動ログ・躊躇時間のシミュレート）",
            ["すぐに思いついて入力できた（ストレス低・躊躇なし）", "単語や文法に少し迷って時間がかかった（ストレス中・躊躇あり）"],
            index=0
        )

        # チャット入力
        if user_input := st.chat_input("ここに英文を入力してね... (例: I went shopping)"):
            # ユーザーのメッセージを追加
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.write(user_input)
                
            # AIの応答生成（建設的相互作用・個別最適化の再現）
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                
                # 行動ログ分析に基づいたAIの動的適応の分岐
                if "少し迷って" in hesitation_level:
                    # 躊躇時間を検知し、負担を減らすためにヒント（型）を出す
                    ai_reply = f"Great effort! 🌟 '{user_input}' is a good start! \n\n" \
                               f"もし『〜を見たよ』と続けたいときは **'I saw [見たいもの].'** の型を使ってみてね。 " \
                               f"What did you see or buy? Tell me more!"
                    st.session_state.vocab_count += 2
                else:
                    # 躊躇がない場合はさらに深い問いを立てる（建設的相互作用）
                    ai_reply = f"Awesome! That sounds like fun! 🎉 Why did you decide to do that? " \
                               f"Tell me more about how you felt!"
                    st.session_state.vocab_count += 4
                    
                response_placeholder.write(ai_reply)
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                st.rerun()

    with col2:
        st.subheader("🔔 ナッジエンジン（行動ログ）")
        st.write("ユーザーが最もスマホを開きやすい時間に届く、心理的ハードルの低い「1分クイック通知」の仕組みです。")
        
        st.success("🤖 **AIからのナッジ通知（例）**\n\n「通学電車に乗りましたね！お疲れ様です。5秒で答えられる質問が届いています。ワンタップで始めよう！」")
        if st.button("通知をタップしてクイック会話を起動"):
            st.toast("ワンタップで会話モジュールが起動しました！")

# ==========================================
# タブ2: 自己調整学習支援ダッシュボード
# ==========================================
with tab2:
    st.subheader("Self-Regulated Learning Dashboard")
    st.write("点数で裁くのではなく、**継続や対話の深さ**を可視化して内発的動機づけを高めます。")
    
    # メトリクスの表示
    m1, m2, m3 = st.columns(3)
    m1.metric(label="🔥 現在の継続日数", value=f"{st.session_state.streak} 日連続", delta="目標まであと2日")
    m2.metric(label="🔤 今日使った新しい語彙数", value=f"{st.session_state.vocab_count} 語", delta="+4語 (昨日比)")
    m3.metric(label="💬 AIとの対話の深さ", value="Level 3 (発展レベル)", delta="Good")
    
    # グラフのシミュレーション
    st.write("### 📈 今週の学習着手ハードル（躊躇時間）の推移")
    st.caption("システムが裏側で計測している「入力にかかった時間（間）」のデータです。使い続けることで心理的ハードルが下がり、躊躇時間が短くなっていることがわかります。")
    
    # ダミーの躊躇時間データ
    chart_data = {
        "月曜日": 18,
        "火曜日": 15,
        "水曜日": 12,
        "木曜日": 14,
        "金曜日": 9,
        "土曜日": 7,
        "今日": 5 if len(st.session_state.messages) > 1 else 10
    }
    st.line_chart(chart_data)
    
    st.info("🎯 **自己調整へのナッジ:** 「今週は文字入力までの迷う時間が平均8秒も短くなりました！あなたの脳が英語の『型』に慣れてきた証拠です。明日は少し長めの文章にチャレンジしてみませんか？」")
