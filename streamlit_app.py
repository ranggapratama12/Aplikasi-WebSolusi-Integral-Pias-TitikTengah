import streamlit as st

# ===============================
# KONFIGURASI HALAMAN
# ===============================
st.set_page_config(
    page_title="Solusi Integral - Titik Tengah",
    page_icon="📐",
    layout="centered"
)

# ===============================
# HEADER
# ===============================
st.title("📐 Aplikasi Website Solusi Integral")
st.subheader("Metode Pias Titik Tengah (Midpoint Rule)")

st.markdown("""
Aplikasi ini dirancang untuk membantu menghitung **solusi integral numerik** menggunakan **kaidah titik tengah** secara interaktif berbasis web.

🚧 **Status proyek: Dalam pengembangan**
""")

st.divider()

# ===============================
# INPUT SECTION
# ===============================
st.header("🧮 Input Parameter Integral")

st.text_input(
    label="Masukkan fungsi f(x)",
    placeholder="Contoh: x**2, sin(x), exp(x)",
    disabled=False
)

col1, col2 = st.columns(2)

with col1:
    st.number_input("Batas bawah (a)", value=0.0)

with col2:
    st.number_input("Batas atas (b)", value=1.0)

st.number_input(
    label="Jumlah pias (n)",
    min_value=1,
    step=1,
    value=4
)

# Tombol dinonaktifkan untuk tahap pengembangan (Sesuai permintaan)
st.button("🔍 Hitung Integral", disabled=True)

st.info("⚠️ Fitur perhitungan sedang dikosongkan untuk tahap pengembangan selanjutnya.")

st.divider()

# ===============================
# OUTPUT SECTION (DUMMY/PLACEHOLDER)
# ===============================
st.header("📊 Hasil Perhitungan")

st.markdown("""
**Nilai Integral (Metode Titik Tengah):** `— hasil belum tersedia —`
""")

st.markdown("""
**Visualisasi Grafik:** Grafik fungsi dan pias titik tengah akan ditampilkan di sini setelah logika perhitungan diaktifkan.
""")

st.warning("🚧 Grafik belum tersedia (on progress)")

st.divider()

# ===============================
# FOOTER
# ===============================
st.caption("""
© 2025  
Aplikasi Website Solusi Integral  
Metode Pias Titik Tengah | Streamlit
""")
