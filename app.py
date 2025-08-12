import streamlit as st
import numpy as np
import pandas as pd
import time

# Page configuration
st.set_page_config(
    page_title="Hillroute Capital Dashboard",
    page_icon="📈",
    layout="wide"
)
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79, #2e7bb6);
        color: white;
        border-radius: 5px;
        text-align: center;
        margin: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>📈 Hillroute Capital Dashboard</h1></div>', unsafe_allow_html=True)

page_1 = st.Page(
    "pages/portfolio_dashboard/portfolio_dashboard.py", 
    title="Portfolio Dashboard", 
    icon="📊"
)
page_2 = st.Page(
    "pages/strategy_backtest/strategy_backtest.py", 
    title="Strategy Backtest", 
    icon="🔍"
)
page_3 = st.Page(
    "pages/strategy_live/strategy_live.py", 
    title="Strategy Live", 
    icon="⚡"
)

pg = st.navigation([page_1, page_2, page_3])

pg.run()