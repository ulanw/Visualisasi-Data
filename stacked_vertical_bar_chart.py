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

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Stacked Vertical Bar Chart")

# Data
stores = ['Store A', 'Store B', 'Store C']
male_population = [150, 200, 180]
female_population = [120, 230, 170]

# Grafik
fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male_population, label='Male', color='blue')
ax.bar(x, female_population, bottom=male_population, label='Female', color='pink')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)

st.subheader("Membuat Stacked Vertical Bar Chart dengan Matplotlib")

# Data Transaksi Penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a_sales = [200, 250, 300]
product_b_sales = [150, 300, 250]

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a_sales, label='Product A', color='blue')
ax.bar(x, product_b_sales, bottom=product_a_sales, label='Product B', color='green')

ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_title('Sales Transactions by Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)

st.subheader("Kustomisasi Stacked Vertical Bar Chart")

for i in range(len(x)):
    plt.text(x[i], product_a_sales[i] / 2, str(product_a_sales[i]), ha='center', color='white')
    plt.text(x[i], product_a_sales[i] + product_b_sales[i] / 2, str(product_b_sales[i]), ha='center', color='black')

st.pyplot(fig)

st.subheader("Multiple Stacked Vertical Bar Chart")

# Data tambahan
q1_male = [150, 180, 160]
q1_female = [240, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

fig, ax = plt.subplots()
bar_width = 0.4
x = np.arange(len(stores))

ax.bar(x - bar_width / 2, q1_male, label='Q1 Male', color='lightblue', width=bar_width)
ax.bar(x - bar_width / 2, q1_female, bottom=q1_male, label='Q1 Female', color='pink', width=bar_width)
ax.bar(x + bar_width / 2, q2_male, label='Q2 Male', color='blue', width=bar_width)
ax.bar(x + bar_width / 2, q2_female, bottom=q2_male, label='Q2 Female', color='red', width=bar_width)

ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)