import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI英語学習支援", layout="wide")

# タイトル
st.title("伴走型AI英語学習支援プロジェクト")

# もし先ほどのHTMLをStreamlit上でそのまま表示させたい場合
# （⚠️以下の「ここにHTMLコードを貼り付ける」部分に、先ほどのコードを丸ごと入れてください）
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>伴走型AI英語学習支援プロジェクト</title>
    <style>
        /* ここにCSSスタイル */
    </style>
</head>
<body>
    <!-- ここにメインコンテンツ -->
    <h1>AIを活用した個別最適化・伴走型英語学習支援</h1>
</body>
</html>
"""

# HTMLをStreamlit内に埋め込んで表示
components.html(html_code, height=1500, scrolling=True)
