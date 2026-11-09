# スライド12: 演習1 / ローカルデータの絞り込み
# 起動: streamlit run 06_filter_local.py
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "商品": ["りんご", "みかん", "ぶどう", "りんご"],
    "個数": [3, 5, 2, 8],
})
choice = st.selectbox(
    "商品", ["すべて", "りんご", "みかん", "ぶどう"])
if choice != "すべて":
    df = df[df["商品"] == choice]
st.dataframe(df)
