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

st.title("Penjualan Smartphone Berdasarkan Merek")
st.subheader("Horizontal Bar Chart Sederhana")

# Data penjualan Smartphone
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales = [350, 420, 300, 280]

# membuat horizontal bar chart
fig, ax = plt.subplots()
y = np.arange(len(brands))
ax.barh(y, sales, color='pink')
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in units)')
ax.set_title('Smartphone Sales by Brand')

# tampilan di streamlit
st.pyplot(fig)

st.markdown("---")

#warna berbeda untuk setiap batang
colors = ['blue', 'green', 'orange', 'red']

fig, ax = plt.subplots()
ax.barh(y, sales, color=colors)

# menambahkan nilai pada batang
for i, v in enumerate(sales):
    ax.text(v + 10, i, str(v), color='black', va='center') #posisi teks

ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in units)')
ax.set_title('Customized Smartphone Sales by Brand')

# tampilkan si streamlit
st.pyplot(fig)

st.markdown("---")

st.subheader('Multiple Horizontal Bar Chart')

# data penjualan
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
q1_sales = [350, 400, 300, 250]
q2_sales = [370, 420, 310, 280]

bar_width = 0.4 # lebar batang
y = np.arange(len(brands))

fig, ax = plt.subplots()

# membuat multiple horizontal bar chart
ax.barh(y - bar_width / 2, q1_sales, height=bar_width, label='Q1 Sales', color='skyblue')
ax.barh(y + bar_width / 2, q2_sales, height=bar_width, label=' Q2 Sales', color='salmon')

# penyesuain tampilan
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in units)')
ax.set_title('Smarthphone Sales by Brand (multiple periods)')
ax.legend()

# tampilkan di streamlit
st.pyplot(fig)