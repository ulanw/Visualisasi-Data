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

# Data Penjualan Bulanan
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
shoes = [500, 600, 700, 800, 650, 700, 850, 900, 750, 800, 950, 1000]
sandals = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850]
socks = [200, 250, 300, 350, 300, 400, 450, 500, 600, 700, 750, 800]

# Fungsi untuk Membuat Area Chart
def plot_area_chart(selected_products):
    plt.figure(figsize=(10, 6))
    
    # Menampilkan produk yang dipilih
    if 'Sepatu' in selected_products:
        plt.fill_between(months, shoes, color="blue", alpha=0.5, label="Sepatu")
    if 'Sandal' in selected_products:
        plt.fill_between(months, sandals, color="green", alpha=0.5, label="Sandal")
    if 'Kaos Kaki' in selected_products:
        plt.fill_between(months, socks, color="orange", alpha=0.5, label="Kaos Kaki")
    
    plt.title("Area Chart: Penjualan Bulanan")
    plt.xlabel("Bulan")
    plt.ylabel("Unit Terjual")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    st.pyplot(plt)

# Aplikasi Streamlit
def main():
    st.title("📊 Visualisasi Penjualan Bulanan")
    st.sidebar.title("⚙️ Pengaturan Grafik")

    # Filter Produk
    st.sidebar.markdown("### ✅ Pilih Produk")
    products = ['Sepatu', 'Sandal', 'Kaos Kaki']
    selected_products = st.sidebar.multiselect(
        "Produk yang akan ditampilkan:",
        products,
        default=products
    )

    # Tampilkan Grafik
    st.markdown("### 📈 Area Chart Penjualan")
    plot_area_chart(selected_products)

# Jalankan Program
if __name__ == "__main__":
    main()