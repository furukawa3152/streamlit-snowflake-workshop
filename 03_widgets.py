# スライド8: ウィジェット
# 起動: streamlit run 03_widgets.py
import streamlit as st

name = st.text_input("なまえ")
age = st.slider("年齢", 0, 100, 30)
fruit = st.selectbox("好きなフルーツ", ["りんご", "みかん", "ぶどう"])
if st.button("送信"):
    st.write(name, age, fruit)
