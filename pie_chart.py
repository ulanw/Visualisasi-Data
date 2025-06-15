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

# Data partisipasi siswa
kegiatan = ['Olahraga', 'Seni', 'Musik', 'Debat']
persentase = [35, 25, 20, 20]

# Fungsi untuk membuat pie chart
def plot_pie_chart(labels, data):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Persentase Partisipasi Siswa dalam Kegiatan Ekstrakurikuler')
    st.pyplot(fig)

# Streamlit interface
st.title("Visualisasi Data Kegiatan Ekstrakurikuler")
st.subheader("Pie Chart Sederhana")
plot_pie_chart(kegiatan, persentase)

# Fungsi untuk pie chart dengan kustomisasi
def plot_customized_pie(labels, data):
    colors = ['gold', 'lightblue', 'lightgreen', 'coral']
    explode = [0.1, 0, 0, 0]  # Menonjolkan "Olahraga"

    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)
    ax.set_title('Kustomisasi Pie Chart')
    st.pyplot(fig)

# Streamlit interface untuk kustomisasi
st.subheader("Kustomisasi Pie Chart")
plot_customized_pie(kegiatan, persentase)

# Fungsi untuk multiple pie chart
def plot_multiple_pie():
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Data kelompok 1
    kegiatan_1 = ['Olahraga', 'Seni']
    persentase_1 = [40, 60]

    # Data kelompok 2
    kegiatan_2 = ['Musik', 'Debat']
    persentase_2 = [50, 50]

    # Pie chart untuk kelompok 1
    axs[0].pie(persentase_1, labels=kegiatan_1, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue'])
    axs[0].set_title('Grup 1')

    # Pie chart untuk kelompok 2
    axs[1].pie(persentase_2, labels=kegiatan_2, autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'coral'])
    axs[1].set_title('Grup 2')

    st.pyplot(fig)

# Streamlit interface untuk multiple pie chart
st.subheader("Multiple Pie Chart")
plot_multiple_pie()
