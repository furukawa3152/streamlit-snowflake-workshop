# Snowflake セットアップ（後半レッスン用）

`07_snowflake_query.py` と `08_snowflake_filter.py` は、
公式 Streamlit チュートリアルで作るサンプル表 `PETS.PUBLIC.MYTABLE` を読みます。
**この表は自動では作られません。** 自分の Snowflake アカウントで事前に用意してください。

## 公式チュートリアル

- [Connect Streamlit to Snowflake](https://docs.streamlit.io/develop/tutorials/databases/snowflake)

## 無料トライアル

- Snowflake の 30 日間トライアルを、メールアドレスで作成できます。
- 申込ページでは無料クレジットの案内があります。クレジットカードの登録は不要です（追加も不要です）。
- 参考: [Trial accounts](https://docs.snowflake.com/en/user-guide/admin-trial-account)

## サンプル表の作成（公式チュートリアルより）

Snowflake の Worksheets で、次の SQL を実行します
（出典: [Connect Streamlit to Snowflake](https://docs.streamlit.io/develop/tutorials/databases/snowflake)）。

```sql
CREATE DATABASE PETS;

CREATE TABLE MYTABLE (NAME varchar(80), PET varchar(80));

INSERT INTO MYTABLE
VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');

SELECT * FROM MYTABLE;
```

スキーマを指定していないため、通常は `PETS.PUBLIC.MYTABLE` になります。

期待するサンプル行:

| NAME   | PET  |
|--------|------|
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

## 接続情報（secrets.toml）

1. `.streamlit/secrets.toml.example` をコピーして `.streamlit/secrets.toml` を作ります。
2. `YOUR_...` を自分の環境の値に置き換えます（キーペア認証の公式例）。
3. `secrets.toml` は **コミットしない** でください（`.gitignore` 済み）。

アカウント識別子はハイフン区切り（`組織-アカウント`）です。
詳細は上記の公式チュートリアルを参照してください。
