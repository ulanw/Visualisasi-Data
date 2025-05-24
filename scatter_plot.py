import streamlit as st
import matplotlib.pyplot as plt
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

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Judul aplikasi
st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')

# Scatter plot menggunakan Matplotlib
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='blue')
ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
# Tampilkan di Streamlit
st.pyplot(fig)


# Kustomisasi scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.grid(True)
# Tampilkan di Streamlit
st.pyplot(fig)


# Data tambahan untuk kategori hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# Multiple scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan')
ax.set_title('Penjualan Es Krim Berdasarkan Hari')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.legend()
# Tampilkan di Streamlit
st.pyplot(fig)
