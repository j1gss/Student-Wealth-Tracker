import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="UniWallet", layout="wide")
st.title("Student Budget Manager")

if 'sem' not in st.session_state:
    st.session_state.sem = []
with st.sidebar:
    st.header("Monthly Parameters")
    money = st.number_input("Monthly Allowance (₹)", min_value=0.0, value=15000.0)
    stash_pct = st.slider("Emergency Stash %", 5, 25, 10)
    stash_val = (money * stash_pct) / 100
    st.subheader("Hard Commitments")
    rentnsubs = st.number_input("Rent/Bills (₹)", min_value=0.0, value=4000.0)
    food_setup = st.radio("Food Arrangement", ["Fixed (Hostel Mess/Home)", "Variable (Canteen/Self-Cook)"])
    if food_setup == "Fixed (Hostel Mess/Home)":
        foodmb = st.number_input("Mess (₹)", value=4500.0)
        foodbuff = 1500.0
    else:
        foodmb = 0.0
        foodbuff = 8000.0
    outflow = rentnsubs + foodmb + stash_val
    liquid = money - outflow
st.subheader("Daily Spend Logger")
with st.expander("Record New Transaction", expanded=True):
    col_x, col_y, col_z = st.columns([2, 1, 1])
    with col_x:
        item = st.text_input("What did you buy?", placeholder="e.g. Metro, Maggi, Library fine")
    with col_y:
        cost = st.number_input("Amount (₹)", min_value=1.0)
    with col_z:
        tag = st.selectbox("Category", ["Survival/Essentials", "Books/Uni Fees", "Bakwaas/Leisure"])
    if st.button("Add to Ledger"):
        ts = datetime.datetime.now().strftime("%d %b, %H:%M")
        st.session_state.sem.append({
            "Time": ts,
            "Item": item,
            "Amt": cost,
            "Tag": tag
        })
if st.session_state.sem:
    spends = pd.DataFrame(st.session_state.sem)
    spent = spends.Amt.sum()
    st.divider()
    m1, m2, m3 = st.columns(3)
    m1.metric("Fixed Costs", f"₹{outflow}")
    m2.metric("Remaining Liquidity", f"₹{round(liquid - spent, 2)}")
    m3.metric("Emergency Reserve", f"₹{stash_val}")
    days_left = 31 - datetime.datetime.now().day
    if days_left > 0:
        safe_daily_limit = (liquid - spent) / days_left
        st.info(f"**Advice:** To survive till month-end, keep daily extra spends under **₹{round(safe_daily_limit, 2)}**.")
    st.write("### Recent Logs")
    st.dataframe(spends, use_container_width=True)