import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# nama anggota kelompok
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #d63384;
        font-size: 36px;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        margin-bottom: 30px;
    }

    .box {
        background-color: #ffe6f0;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(214, 51, 132, 0.2);
        width: 70%;
        margin: 0 auto;
    }

    .anggota {
        font-size: 20px;
        padding: 5px 0;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown('<div class="title">🌸 Daftar Nama Anggota Kelompok 🌸</div>', unsafe_allow_html=True)

# Daftar nama dalam box
st.markdown("""
    <div class="box">
        <div class="anggota">1. Wulan Ramadani (0110223259) </div>
        <div class="anggota">2. Siti Fadila Siregar (0110223245) </div>
        <div class="anggota">3. Zahra Praharani (0110223182)</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Contoh data penjualan
brands = ['Brand A', 'Brand B', 'Brand C']
sales_2022 = [350, 450, 300]
sales_2023 = [400, 500, 320]

def create_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    ax.barh(y, sales_2022, label='2022', color='skyblue')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='orange')
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Smartphone Sales by Brand')
    ax.legend()
    return fig

# Render chart di Streamlit
st.title("Smartphone Sales Visualization")
st.pyplot(create_stacked_bar_chart())

def create_custom_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    ax.barh(y, sales_2022, label='2022', color='blue', edgecolor='black', hatch='//')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='green', edgecolor='black', hatch='\\\\')
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Customized Smartphone Sales by Brand')
    ax.legend()

    # Tambahkan anotasi
    for i in range(len(brands)):
        ax.text(sales_2022[i] / 2, i, f"{sales_2022[i]}", va='center', color='white')
        ax.text(sales_2022[i] + sales_2023[i] / 2, i, f"{sales_2023[i]}", va='center', color='black')

    return fig

st.pyplot(create_custom_stacked_bar_chart())