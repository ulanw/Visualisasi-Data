# Pola dan Trend dengan Bar Chart
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

# Data jumlah mahasiswa per jurusan selama 5 tahun
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 100, 100, 100, 100],
    'Sistem Informasi': [120, 125, 135, 115, 140],
    'Teknik Informatika': [105, 110, 100, 110, 100],
    'Data Science': [75, 80, 85, 100, 110]
}

# Membuat dataframe untuk visualisasi
df = pd.DataFrame(data)

# Streamlit App
st.title("Visualisasi Tren Jumlah Mahasiswa Menilih Jurusan Komputer (5 Tahun Terakhir)")

# Menambahkan filter tahun
filter_tahun = st.multiselect("Pilih Tahun:", df["Tahun"], default=df["Tahun"])

# Menambahkan filter jurusan
jurusan_list = ["Ilmu Komputer", "Sistem Informasi", "Teknik Informatika", "Data Science"]
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)

# Filter data berdasarkan input pengguna
filtered_data = df[df["Tahun"].isin(filter_tahun)][["Tahun"] + filter_jurusan]

# Menampilkan data tabel
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# Membuat Bar Chart dengan filter
st.subheader("Bar Chart Jumlah Mahasiswa (Berdasarkan Filter)")
fig, ax = plt.subplots(figsize=(12, 6))

# Menampilkan Bar Chart berdasarkan data yang difilter
x = range(len(filtered_data["Tahun"]))

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * 0.2 for p in x], filtered_data[jur], width=0.2, label=jur)

# Menambahkan sumbu dan judul
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + 0.2 * len(filter_jurusan) / 2 - 0.1 for p in x])
ax.set_xticklabels(filtered_data["Tahun"])
ax.legend()

# Menampilkan plot di Streamlit
st.pyplot(fig)