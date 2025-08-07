import streamlit as st
import time

# 初始化購物車和重新整理狀態
if "cart" not in st.session_state:
    st.session_state.cart = []

if "refreshing" not in st.session_state:
    st.session_state.refreshing = False

# 標題
st.title("點餐機")

# 處理重新整理的邏輯（顯示文字後延遲3秒再重新整理）
if st.session_state.refreshing:
    st.warning("準備重新整理中... 請稍候")
    time.sleep(3)
    st.session_state.refreshing = False  # 重設狀態
    st.rerun()  # 重新整理畫面

# 重新整理按鈕（會觸發「準備重新整理」）
if st.button("重新整理"):
    st.session_state.refreshing = True
    st.rerun()  # 立刻進入 refreshing 狀態（讓畫面變成「準備重新整理」）

# 餐點輸入區
col1, col2 = st.columns([2, 1])
with col1:
    food = st.text_input("輸入餐點", placeholder="例如：雞排、珍奶")
with col2:
    if st.button("加入") and food.strip() != "":
        st.session_state.cart.append(food.strip())
        st.success(f"已加入：{food.strip()}")
        st.rerun()

# 購物車標題永遠顯示
st.title("購物車")

# 顯示購物車內容（如果有）
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{i+1}. {item}")
        with col2:
            if st.button("刪除", key=f"del_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
                break
