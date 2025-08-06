import streamlit as st

st.title("數字金字塔")

number = st.number_input("請輸入一個數字", min_value=1, max_value=9, step=1)
for i in range(1, number + 1):
    a = str(i) * i
    st.write(a)
