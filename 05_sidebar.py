# スライド11: サイドバー
# 起動: streamlit run 05_sidebar.py
import streamlit as st

name = st.sidebar.text_input("なまえ")
n = st.sidebar.slider("件数", 1, 10, 5)
st.write(name, n)
