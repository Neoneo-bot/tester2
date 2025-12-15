import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.markdown("""
    <style>
    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    .main-header {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        animation: slideIn 1s ease-out;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(45deg, #11998e, #38ef7d);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

