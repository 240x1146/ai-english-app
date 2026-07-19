<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>伴走型AI英語学習支援プロジェクト</title>
    <style>
        /* 全体のスタイル定義（モダンでクリアなデザイン） */
        :root {
            --primary-color: #2563eb;    /* 信頼感のあるブルー */
            --secondary-color: #10b981;  /* 成長・習慣化を表すグリーン */
            --accent-color: #f59e0b;     /* ナッジ・通知用のオレンジ */
            --bg-color: #f8fafc;         /* 薄いグレーの背景 */
            --text-color: #1e293b;       /* 読みやすい濃いグレー */
            --card-bg: #ffffff;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', Meiryo, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.7;
        }

        /* ヘッダー・ナビゲーション */
        header {
            background-color: var(--card-bg);
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .nav-container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-weight: bold;
            font-size: 1.3rem;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .logo-sub {
            font-size: 0.8rem;
            color: #64748b;
            background: #e2e8f0;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
        }

        /* ヒーローセクション（ファーストビュー） */
        .hero {
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
            padding: 4rem 2rem;
            text-align: center;
        }

        .hero-container {
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 2.2rem;
            color: #1e3a8a;
            margin-bottom: 1rem;
            letter-spacing: -0.025em;
        }

        .hero p {
            font-size: 1.1rem;
            color: #475569;
            margin-bottom: 2rem;
        }

        .btn {
            display: inline-block;
            background-color: var(--primary-color);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.2s;
        }

        .btn:hover {
            background-color: #1d4ed8;
        }

        /* メインコンテンツの外枠 */
        .main-container {
            max-width: 1100px;
            margin: 2rem auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: 3fr 1fr;
            gap: 2rem;
        }

        @media (max-width: 768px) {
            .main-container {
                grid-template-columns: 1fr;
            }
        }

        /* セクション共通スタイル */
        section {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }

        h2 {
            font-size: 1.5rem;
            color: #0f172a;
            margin-bottom: 1.5rem;
            border-left: 5px solid var(--primary-color);
            padding-left: 0.75rem;
        }

        h3 {
            font-size: 1.15rem;
            color: #1e293b;
            margin: 1.5rem 0 0.5rem 0;
        }

        p {
            margin-bottom: 1rem;
            color: #475569;
        }

        /* リストの調整 */
        ul, ol {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
            color: #475569;
        }

        li {
            margin-bottom: 0.5rem;
        }

        /* 3つの主要コア機能（グリッド配置） */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .feature-card {
            background-color: #f8fafc;
            padding: 1.5rem;
            border-radius: 8px;
            border-top: 4px solid var(--primary-color);
        }

        .feature-card:nth-child(2) { border-top-color: var(--accent-color); }
        .feature-card:nth-child(3) { border-top-color: var(--secondary-color); }

        .feature-card h4 {
            font-size: 1.05rem;
            color: #0f172a;
            margin-bottom: 0.5rem;
        }

        /* ワークフロー（タイムライン風） */
        .workflow-list {
            list-style: none;
            padding-left: 0;
            position: relative;
        }

        .workflow-item {
            position: relative;
            padding-left: 2rem;
            margin-bottom: 1.5rem;
        }

        .workflow-item::before {
            content: "↓";
            position: absolute;
            left: 0.3rem;
            top: -1.2rem;
            color: var(--primary-color);
            font-weight: bold;
        }

        .workflow-item:first-child::before {
            content: "●";
            top: 0;
        }

        .workflow-title {
            font-weight: bold;
            color: #0f172a;
        }

        /* 強調用の引用ブロック */
        blockquote {
            background-color: #f0fdf4;
            border-left: 4px solid var(--secondary-color);
            padding: 1rem;
            margin: 1.5rem 0;
            border-radius: 0 8px 8px 0;
            font-style: italic;
        }

        /* サイドバー（リンクやメタ情報） */
        aside {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .sidebar-widget {
            background-color: var(--card-bg);
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }

        .sidebar-widget h4 {
            font-size: 1rem;
            margin-bottom: 0.75rem;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
        }

        .links-list {
            list-style: none;
            padding-left: 0;
        }

        .links-list li {
            font-size: 0.9rem;
            word-break: break-all;
        }

        .links-list a {
            color: var(--primary-color);
            text-decoration: none;
        }

        .links-list a:hover {
            text-decoration: underline;
        }

        /* フッター */
        footer {
            background-color: #0f172a;
            color: #94a3b8;
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <!-- ヘッダー -->
    <header>
        <div class="nav-container">
            <div class="logo">
                AI English Support <span class="logo-sub">伴走型エージェント</span>
            </div>
            <div>
                <a href="https://ai-english-app-ktfargdkm6smzvatez9hfb.streamlit.app/" target="_blank" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">アプリを開く</a>
            </div>
        </div>
    </header>

    <!-- ヒーローセクション -->
    <div class="hero">
        <div class="hero-container">
            <h1>AIを活用した個別最適化・伴走型英語学習支援</h1>
            <p>単に「教える」のではなく、学習者の行動ログを分析し、自然な対話を通じて自発的な習慣化をナッジする次世代システム。</p>
            <a href="#solution" class="btn">ソリューションの詳細を見る</a>
        </div>
    </div>

    <!-- メインコンテンツ -->
    <div class="main-container">
        <main>
            <!-- 背景と問題の説明 -->
            <section id="problem">
                <h2>問題の説明と背景</h2>
                <h3>現状の課題と重要な理由</h3>
                <p>近年、AIチャットボットや自動添削ツールは普及しつつあるものの、日本の英語教育は依然として「読む」ことに偏りがちです。大学での学習や国際コミュニケーションにおいて「書く・話す」実践力は不可欠ですが、従来の授業だけでは一人ひとりの苦手分野に合わせた個別指導が難しく、モチベーション低下を招く要因となっています。</p>
                
                <h3>データに基づく証拠</h3>
                <p>文部科学省の調査（平成26年度・高校3年生7万人対象）では、<strong>CEFR A1レベル（中学生レベル）にとどまる生徒が86.5%</strong>にのぼり、「書く力」に深刻な課題があることが浮き彫りになりました。多くの学習者が「自分の書いた英文が正しいか客観的に判断できない」という不安を抱えており、24時間いつでも適切なフィードバックを受けられる環境が強く求められています。</p>
                
                <h3>対象ステークホルダー</h3>
                <ul>
                    <li>英語を学ぶ高校生・大学生 / 英検受験者</li>
                    <li>個別最適化された指導を模索する教師・教育機関</li>
                    <li>最先端の学習支援サービスを展開する企業</li>
                </ul>
            </section>

            <!-- ソリューション設計 -->
            <section id="solution">
                <h2>ソリューション設計</h2>
                <p>本プロジェクトは、学習者の「学習負担（認知心理的ハードル）」を徹底的に軽減し、システム側から行動を優しく促す仕掛け（ナッジ）を組み込むことで、内発的動機づけを高める<strong>「伴走型AIエージェント・システム」</strong>です。</p>

                <div class="features-grid">
                    <div class="feature-card">
                        <h4>① 状況適応型・AI会話対話モジュール</h4>
                        <p>学習者のレベルや気分、興味に合わせ、AIの話し方や語彙を動的に変化。お互いに問いを立て直す「建設的相互作用」を生み出します。</p>
                    </div>
                    <div class="feature-card">
                        <h4>② 行動ログ分析・ナッジエンジン</h4>
                        <p>スマホの通知確認タイミングやタイピングの「躊躇時間」を分析。最も学習に着手しやすい時間に、負担の少ない1分英会話などを提案します。</p>
                    </div>
                    <div class="feature-card">
                        <h4>③ 自己調整学習支援ダッシュボード</h4>
                        <p>点数だけでなく「継続日数」や「対話の深さ（語彙の多様性）」を可視化。学習者自身が自発的に目標を修正できるよう支援します。</p>
                    </div>
                </div>

                <h3>システムワークフロー</h3>
                <ol class="workflow-list" style="margin-top: 1rem;">
                    <li class="workflow-item"><span class="workflow-title">日常の行動データの蓄積:</span> スマートデバイス等から受動的にデータを収集</li>
                    <li class="workflow-item"><span class="workflow-title">ナッジの発生:</span> 最適なタイミングで、心理的負担の少ない学習（例: 5秒で答えて！）を提案</li>
                    <li class="workflow-item"><span class="workflow-title">学習の開始:</span> ワンタップで起動。AIとの建設的な対話、または自動添削フィードバック</li>
                    <li class="workflow-item"><span class="workflow-title">リアルタイム行動分析:</span> 入力の躊躇度（間）、正答率、学習時間を測定</li>
                    <li class="workflow-item"><span class="workflow-title">個別最適化＆反映:</span> 次回の難易度を自動調整し、ダッシュボードへ進捗を可視化</li>
                </ol>
            </section>

            <!-- 設計上の決定事項と理論 -->
            <section id="framework">
                <h2>理論的枠組みと設計上の決定事項</h2>
                <p>本ソリューションは、<strong>「建設的相互作用」「自己調整学習」「社会的学習理論」</strong>をベースに構築されています。</p>
                
                <blockquote>
                    <strong>【採点者ではなく、対等な編集者として】</strong><br>
                    文法ミスを厳しく指摘される環境は、学習意欲を低下させ、発話への恐怖心を生んでしまいます。本システムでは、ミスを叱るのではなく「こう書くと、もっとネイティブに意図が伝わるよ！」という前向きな提案を重視し、裏側で行度ログ分析を行うことで、ストレスフリーな個別最適化を実現します。
                </blockquote>

                <ul>
                    <li><strong>デバイス選定:</strong> 専用機器ではなく日常的に使用する「スマートフォン/PC」を採用し、起動の物理的ハードルをゼロに。</li>
                    <li><strong>キーボード入力の段階化:</strong> 最初は「タップ選択で文の骨組みを作る」ことから始め、徐々に「タイピングで肉付けする」ステップアップ構造で挫折を防ぎます。</li>
                </ul>
            </section>

            <!-- 評価計画 -->
            <section id="evaluation">
                <h2>評価計画とデータ分析</h2>
                <p><strong>目的:</strong> ユーザーの英語学習成果および習慣化の度合いを評価するため</p>
                <p>収集した行動データ（アプリ起動時間、タイピング速度、躊躇時間など）を分析し、学習の継続率や、躊躇時間の減少（＝心理的ハードルの低下）、最終的な外部スコアや成績の向上を基準として、システムの有益性を総合的に判断します。</p>
            </section>
        </main>

        <!-- サイドバー -->
        <aside>
            <div class="sidebar-widget">
                <h4>使用技術・ツール</h4>
                <ul>
                    <li><strong>Hardware:</strong> スマートフォン / PC</li>
                    <li><strong>Framework:</strong> Python / Streamlit</li>
                    <li><strong>Core API:</strong> 大規模言語モデル（LLM）API</li>
                    <li><strong>Log System:</strong> JavaScriptによる打鍵行動ログ収集</li>
                </ul>
            </div>

            <div class="sidebar-widget">
                <h4>プロジェクトリンク</h4>
                <ul class="links-list">
                    <li>🚀 <strong>Streamlit アプリ:</strong><br><a href="https://ai-english-app-ktfargdkm6smzvatez9hfb.streamlit.app/" target="_blank">アプリを開く</a></li>
                </ul>
            </div>

            <div class="sidebar-widget">
                <h4>参考文献・リソース</h4>
                <ul class="links-list">
                    <li>・<a href="https://www.nippon.com/ja/japan-data/h02199/" target="_blank">nippon.com（英語能力調査データ）</a></li>
                    <li>・<a href="https://www.benesse-i-career.co.jp/news/20240404_1release.pdf" target="_blank">ベネッセ・アイ・キャリア 資料</a></li>
                    <li>・<a href="https://toyo.repo.nii.ac.jp/record/9027/files/kankogaku16_001-018.pdf" target="_blank">東洋大学リポジトリ</a></li>
                    <li>・<a href="https://onlinelibrary.wiley.com/doi/full/10.1155/2021/8812542" target="_blank">Wiley Online Library</a></li>
                    <li>・<a href="https://www.jstage.jst.go.jp/article/tjsai/31/3/31_A-F93_1/_article/-char/ja/" target="_blank">J-STAGE（人工知能学会）</a></li>
                    <li>・<a href="https://dl.acm.org/doi/10.1145/3769526.3769663" target="_blank">ACM Digital Library</a></li>
                </ul>
            </div>
        </aside>
    </div>

    <!-- フッター -->
    <footer>
        <p>&copy; 2026 AI英語学習支援支援プロジェクト (伴走型AIエージェント・システム)</p>
    </footer>

</body>
</html>
