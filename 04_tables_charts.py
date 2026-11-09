# スライド10: 表とグラフ
# 起動: streamlit run 04_tables_charts.py
import streamlit as st
import pandas as pd

df = pd.DataFrame({"売上": [10, 20, 15]})
st.dataframe(df)
st.bar_chart(df)
