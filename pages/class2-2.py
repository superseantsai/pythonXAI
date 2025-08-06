import streamlit as st  # 匯入streamlit模組並重新命名為st

# st.number_input ()可以讓使用者輸入數字，設定step=1可以讓適用者只能輸入整數
# min_value=0 可以設定最小值為0，max_value=100可以設定最大值為100
number = st.number_input("請輸入半徑", step=1, min_value=0, max_value=100)
# st.markdown()可以在網頁使用Markdown語法顯示文字
st.markdown(f"您輸入的數字是: {number}")
