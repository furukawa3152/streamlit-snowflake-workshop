# Streamlit勉強会 基本からSnowflake連携まで
古川 格 / HAGAKURE PROGRAMMING塾 の 90 分ハンズオン用 **お手本リポジトリ** です。  
スライドで示したコードと同じものを、番号付きファイルでそのまま動かせます。

対象: Python 環境（venv / pip）の準備ができる方。  
前半（01〜06）は Snowflake なしで動きます。後半（07〜08）だけ接続設定が必要です。

---

## 事前準備

1. Python の仮想環境を用意して有効化する（すでにできる前提です）。
2. 必要なライブラリを入れます。

**デフォルト（スライドと同じコマンド）:**

```bash
pip install streamlit snowflake-snowpark-python pandas
```

`requirements.txt` から入れる場合:

```bash
pip install -r requirements.txt
```

> メモ: 公式チュートリアルの現在の書き方は `streamlit[snowflake]>=1.66.0` です。  
> スライドでは教えるコードをカバーできるシンプルなコマンドを使っています。どちらでもこのリポジトリのコードは動かせます。

3. （後半のみ）Snowflake の無料トライアル（メールで作成・30 日間・カード登録不要）と、サンプル表の準備。詳しくは [`snowflake/setup.md`](snowflake/setup.md) へ。

---

## 動かし方

リポジトリのルートで、次のように起動します。

```bash
streamlit run 01_hello.py
```

ブラウザが開いたら成功です。ほかのファイルも同じです。

| ファイル | 内容（対応スライド） |
|----------|----------------------|
| `01_hello.py` | はじめての Streamlit（スライド 6） |
| `02_display.py` | title / write / markdown（スライド 7） |
| `03_widgets.py` | text_input / slider / selectbox / button（スライド 8） |
| `04_tables_charts.py` | DataFrame + 表 + 棒グラフ（スライド 10） |
| `05_sidebar.py` | サイドバー（スライド 11） |
| `06_filter_local.py` | 演習1: ローカル表の絞り込み（スライド 12） |
| `07_snowflake_query.py` | Snowflake 接続とクエリ（スライド 16） |
| `08_snowflake_filter.py` | params で安全に絞り込み（スライド 17 / 18） |

例:

```bash
streamlit run 02_display.py
streamlit run 06_filter_local.py
streamlit run 08_snowflake_filter.py
```

---

## 操作するたび、上から下へ（スライド 9）

ウィジェットを操作すると、スクリプト全体が最初から再実行されます。これはバグではなく、Streamlit の基本のしくみです。

再実行をまたいで値を残したいときは `st.session_state` を使いますが、この勉強会では深追いしません。まずは「上から下へ」の流れを体感しましょう。

---

## Snowflake 連携（07〜08）

1. `.streamlit/secrets.toml.example` をコピーして `.streamlit/secrets.toml` を作り、`YOUR_...` を置き換えます。
2. 公式チュートリアルどおりに `PETS.PUBLIC.MYTABLE` を作成します（自動では入りません）。
3. `streamlit run 07_snowflake_query.py` で接続と表示を確認します。
4. `08_snowflake_filter.py` では `params=[pet]` で値を渡します。**SQL 文字列にウィジェットの値を埋め込まない**でください。

手順の詳細・公式 SQL・トライアル案内は [`snowflake/setup.md`](snowflake/setup.md) にまとめています。

接続情報や秘密鍵は共有・コミットしないでください。`secrets.toml` は `.gitignore` に入れています。

---

## ファイル構成

```text
.
├── 01_hello.py
├── 02_display.py
├── 03_widgets.py
├── 04_tables_charts.py
├── 05_sidebar.py
├── 06_filter_local.py
├── 07_snowflake_query.py
├── 08_snowflake_filter.py
├── .streamlit/
│   └── secrets.toml.example
├── snowflake/
│   └── setup.md
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ライセンス

MIT License — Copyright (c) 2026 古川 格 / HAGAKURE PROGRAMMING塾
