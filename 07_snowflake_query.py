# スライド16: Snowflakeにつないで表を出す
# 起動: streamlit run 07_snowflake_query.py
# 前提: .streamlit/secrets.toml と PETS.PUBLIC.MYTABLE の準備（snowflake/setup.md 参照）
import streamlit as st

conn = st.connection("snowflake")
df = conn.query(
    """SELECT NAME, PET
    FROM PETS.PUBLIC.MYTABLE
    LIMIT 10""")
st.dataframe(df)
