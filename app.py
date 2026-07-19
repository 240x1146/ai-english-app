import streamlit as st
import streamlit.components.v1 as components

# ページ設定（ブラウザのタブ名やレイアウトの設定）
st.set_page_config(
    page_title="伴走型AI英語学習支援プロジェクト",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit自体の背景や余白を綺麗に整えるカスタムスタイル
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 画面に表示するWEBサイトのHTML/CSSデータ
html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* カラーパレットの定義 */
        :root {
            --primary-color: #2563eb;
            --secondary-color: #10b981;
            --accent-color: #f59e0b;
            --bg-color: #f8fafc;
            --text-color: #1e293b;
            --card-bg: #ffffff;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.7;
            padding: 10px;
        }

        /* メインの2カラムレイアウト */
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 3fr 1fr;
            gap: 20px;
        }

        @media (max-width: 900px) {
            .main-container {
                grid-template-columns: 1fr;
            }
        }

        /* 各セクションのカードデザイン */
        section {
            background-color: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }

        /* ヒーローヘッダー */
        .hero-banner {
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
            padding: 40px;
            border-radius: 12px;
            margin-bottom: 25px;
            border-left: 6px solid var(--primary-color);
        }

        .hero-banner h1 {
            color: #1e3a8a;
            font-size: 2rem;
            margin-bottom: 10px;
        }

        .hero-banner p {
            color: #475569;
            font-size: 1.1rem;
        }

        h2 {
            font-size: 1.4rem;
            color: #0f172a;
            margin-bottom: 20px;
            border-left: 5px solid var(--primary-color);
            padding-left: 12px;
        }

        h3 {
            font-size: 1.15rem;
            color: #1e293b;
            margin: 25px 0 10px 0;
        }

        p {
            margin-bottom: 12px;
            color: #475569;
        }

        ul, ol {
            margin-bottom: 15px;
            padding-left: 20px;
            color: #475569;
        }

        li {
            margin-bottom: 8px;
        }

        /* 特徴の3カラムグリッド */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .feature-card {
            background-color: #f8fafc;
            padding: 20px;
            border-radius: 8px;
            border-top: 4px solid var(--primary-color);
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }

        .feature-card:nth-child(2) { border-top-color: var(--accent-color); }
        .feature-card:nth-child(3) { border-top-color: var(--secondary-color); }

        .feature-card h4 {
            font-size: 1.05rem;
            color: #0f172a;
            margin-bottom: 10px;
        }

        /* ワークフローの矢印デザイン */
        .workflow-list {
            list-style: none;
            padding-left: 0;
        }

        .workflow-item {
            position: relative;
            padding-left: 25px;
            margin-bottom: 15px;
        }

        .workflow-item::before {
            content: "↓";
            position: absolute;
            left: 5px;
            top: -15px;
            color: var(--primary-color);
            font-weight: bold;
            font-size: 1.2rem;
        }

        .workflow-item:first-child::before {
            content: "●";
            top: 2px;
            font-size: 0.9rem;
        }

        .workflow-title {
            font-weight: bold;
            color: #0f172a;
        }

        blockquote {
            background-color: #f0fdf4;
            border-left: 4px solid var(--secondary-color);
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }

        aside {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .sidebar-widget {
            background-color: var(--card-bg);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }

        .sidebar-widget h4 {
            font-size: 1rem;
            margin-bottom: 12px;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 6px;
        }

        .links-list {
            list-style: none;
            padding-left: 0;
        }

        .links-list li {
            font-size: 0.9rem;
            margin-bottom: 10px;
        }

        .links-list a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 500;
        }

        .links-list a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <div class="hero-banner">
        <h1>AIを活用した個別最適化・伴走型英語学習支援</h1>
        <p>行動ログ分析に基づき、認知心理的ハードルを徹底的に下げて自発的学習をナッジするエージェントシステム</p>
    </div>

    <div class="main-container">
        <main>
            <!-- 背景・問題の説明 -->
            <section id="problem">
                <h2>1. 問題の説明と背景</h2>
                <h3>現状の課題と重要な理由</h3>
                <p>近年、AI技術の発展により英語学習支援ツールが増加していますが、日本の教育環境では「読む力」に偏りがちで、実践的なライティングや個別最適化された環境が不足しています。英語力はキャリアや留学において必須である一方、一律の授業スタイルではモチベーション低下を招きやすいのが実情です。</p>
                
                <h3>データに基づく客観的エビデンス</h3>
                <p>文部科学省が高校3年生7万人を対象に実施した英語能力調査では、<strong>CEFR A1レベル（中学生レベル）に留まる生徒が86.5%</strong>という深刻な結果が出ています。多くの学生が「自分の書いた英語が正しいか判断できない」という不安を抱えており、24時間いつでも即時フィードバックが得られる環境の構築が急務です。</p>
                
                <h3>対象ユーザー・ステークホルダー</h3>
                <ul>
                    <li>英語を学ぶ高校生・大学生 / 英検受験者</li>
                    <li>個別最適化指導を導入したい指導者・教育機関</li>
                    <li>AI学習支援サービスを提供する企業</li>
                </ul>
            </section>

            <!-- ソリューション設計 -->
            <section id="solution">
                <h2>2. ソリューション設計</h2>
                <p>本提案は、単に英語を教える教材ではなく、学習者の行動データを分析して「心理的・認知的な負担」を最小化し、自己調整学習を優しく促す（ナッジする）<strong>伴走型AIエージェント・システム</strong>です。</p>

                <div class="features-grid">
                    <div class="feature-card">
                        <h4>① 状況適応型・AI対話モジュール</h4>
                        <p>学習者のレベルや気分、関心に合わせ、AIのトピックや語彙力を動的に変更。「建設的相互作用」を生む対話シナリオを展開します。</p>
                    </div>
                    <div class="feature-card">
                        <h4>② 行動ログ分析・ナッジエンジン</h4>
                        <p>スマホの通知確認タイミングや、タイピングの「躊躇時間」を検知。最も負担の少ない時間帯に、1分で終わるクイック対話を提案します。</p>
                    </div>
                    <div class="feature-card">
                        <h4>③ 自己調整学習支援ダッシュボード</h4>
                        <p>継続日数や「対話の深さ（語彙多様性）」を可視化。学習者が自ら目標をモニタリングし、自己監視・評価を行うサイクルを支援します。</p>
                    </div>
                </div>

                <h3>エンドユーザーのUXワークフロー</h3>
                <ol class="workflow-list">
                    <li class="workflow-item"><span class="workflow-title">行動データの蓄積:</span> スマートデバイスから受動的にライフログを蓄積</li>
                    <li class="workflow-item"><span class="workflow-title">ナッジの発生:</span> 最適なタイミングで「5秒で答えて！」等の超低負担な通知を送出</li>
                    <li class="workflow-item"><span class="workflow-title">学習・対話の開始:</span> ワンタップでシームレスにAIとの建設的な対話を開始</li>
                    <li class="workflow-item"><span class="workflow-title">リアルタイム適応:</span> ユーザーの入力の「間（躊躇度）」に応じて、AIが次の質問の難易度やヒントを自動調整</li>
                    <li class="workflow-item"><span class="workflow-title">ダッシュボード反映:</span> 進捗を可視化し、次の自発的学習意欲を向上</li>
                </ol>
            </section>

            <!-- 理論と設計決定 -->
            <section id="decisions">
                <h2>3. 理論的枠組みと設計決定</h2>
                <p><strong>【採用した理論】</strong> 建設的相互作用、自己調整学習、社会的学習理論</p>
                
                <blockquote>
                    <strong>★ 設計の根幹：採点者ではなく「対等な編集者・パートナー」</strong><br>
                    過度な文法エラーの指摘は、学習者の内発的動機づけを低下させます。本システムは、ミスを厳しく採点するのではなく、「こう表現すると、さらに意図がクリアに伝わるよ！」という前向きな提案を行い、心理的安全性を確保します。
                </blockquote>

                <ul>
                    <li><strong>スマホ/PCの採用:</strong> 専用機器の購入負担や起動の手間をゼロにし、隙間時間の活用を最大化するため。</li>
                    <li><strong>キーボード入力のステップ化:</strong> 心理的負担を下げるため、最初は「タップ選択による型作り」から始め、段階的に「タイピングによる肉付け」へと移行させます。</li>
                </ul>
            </section>

            <!-- 評価計画 -->
            <section id="evaluation">
                <h2>4. 評価計画とデータ分析計画</h2>
                <p><strong>評価目的:</strong> システムを通じた英語学習成果と、習慣化への有効性の検証</p>
                <p>アプリの起動時間やタイピングの躊躇時間などの行動データを分析し、「英語を書くことへの抵抗感の減少」や「継続率」を測定します。これらの行動変化をパフォーマンス指標とし、最終的な英語の成績向上やスコアアップに繋がっているかを総合評価します。</p>
            </section>
        </main>

        <!-- サイドバー情報 -->
        <aside>
            <div class="sidebar-widget">
                <h4>システム構成 / 技術</h4>
                <ul>
                    <li>Hardware: スマートフォン / PC</li>
                    <li>Framework: Python / Streamlit</li>
                    <li>Core Engine: LLM API</li>
                    <li>Log System: JS打鍵ログ収集</li>
                </ul>
            </div>

            <div class="sidebar-widget">
                <h4>参考文献・エビデンス</h4>
                <ul class="links-list">
                    <li>・<a href="https://www.nippon.com/ja/japan-data/h02199/" target="_blank">文科省 英語能力調査データ</a></li>
                    <li>・<a href="https://www.benesse-i-career.co.jp/news/20240404_1release.pdf" target="_blank">ベネッセ リリース資料</a></li>
                    <li>・<a href="https://toyo.repo.nii.ac.jp/record/9027/files/kankogaku16_001-018.pdf" target="_blank">東洋大学 学術リポジトリ</a></li>
                    <li>・<a href="https://onlinelibrary.wiley.com/doi/full/10.1155/2021/8812542" target="_blank">Wiley Online Library</a></li>
                    <li>・<a href="https://www.jstage.jst.go.jp/article/tjsai/31/3/31_A-F93_1/_article/-char/ja/" target="_blank">J-STAGE (人工知能学会)</a></li>
                    <li>・<a href="https://dl.acm.org/doi/10.1145/3769526.3769663" target="_blank">ACM Digital Library</a></li>
                </ul>
            </div>
        </aside>
    </div>

</body>
</html>
"""

# Streamlitのセキュアな埋め込み機能を使用してWEB画面を表示
components.html(html_content, height=1600, scrolling=True)
