import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.markdown("""
    <style>
    /* Animasi Judul */
    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
