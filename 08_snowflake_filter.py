# スライド17 / 18: params で安全に絞り込む
# 起動: streamlit run 08_snowflake_filter.py
# 注意: ウィジェットの値を SQL 文字列に埋め込まない（params で渡す）
import streamlit as st

conn = st.connection(
    "snowflake", paramstyle="qmark")
pet = st.selectbox("ペット", ["dog", "cat", "bird"])
sql = """SELECT NAME, PET
FROM PETS.PUBLIC.MYTABLE
WHERE PET = ?
LIMIT 10"""
df = conn.query(sql, params=[pet])
st.dataframe(df)
