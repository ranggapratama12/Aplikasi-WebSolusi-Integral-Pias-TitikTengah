import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
Aplikasi ini menghitung estimasi nilai integral tentu dengan membagi area di bawah kurva menjadi pias-pias persegi panjang. 
Tinggi setiap pias ditentukan oleh nilai fungsi pada **titik tengah** setiap sub-interval.
""")

st.divider()

# ===============================
# INPUT SECTION
# ===============================
st.header("🧮 Input Parameter Integral")

# Input fungsi sebagai string
func_str = st.text_input(
    label="Masukkan fungsi f(x)",
    value="x**2",
    placeholder="Contoh: x**2, np.sin(x), np.exp(x)"
)

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Batas bawah (a)", value=0.0)
with col2:
    b = st.number_input("Batas atas (b)", value=1.0)

n = st.number_input(
    label="Jumlah pias (n)",
    min_value=1,
    step=1,
    value=4
)

# Tombol Hitung
if st.button("🔍 Hitung Integral"):
    try:
        # Menyiapkan fungsi matematika menggunakan eval
        # Menyertakan "np" agar user bisa menggunakan library numpy
        def f(x):
            return eval(func_str, {"np": np, "x": x, "x": x})

        # --- LOGIKA PERHITUNGAN METODE TITIK TENGAH ---
        # Rumus lebar pias: dx = (b - a) / n
        dx = (b - a) / n
        
        # Menentukan titik-titik tengah (midpoints)
        x_mid = np.linspace(a + dx/2, b - dx/2, n)
        y_mid = f(x_mid)
        
        # Hasil Integral: Jumlah dari (f(mid) * dx)
        integral_result = np.sum(y_mid) * dx

        # ===============================
        # OUTPUT SECTION
        # ===============================
        st.divider()
        st.header("📊 Hasil Perhitungan")
        
        st.success(f"**Nilai Estimasi Integral:** {integral_result:.6f}")

        # --- VISUALISASI ---
        # 
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot kurva fungsi utama
        x_curve = np.linspace(a, b, 200)
        y_curve = f(x_curve)
        ax.plot(x_curve, y_curve, 'red', label='f(x)', linewidth=2)

        # Plot batang pias (Midpoint Rectangles)
        x_left = np.linspace(a, b - dx, n)
        ax.bar(x_left, y_mid, width=dx, align='edge', alpha=0.3, 
               color='skyblue', edgecolor='blue', label='Pias (Metode Titik Tengah)')
        
        # Plot titik tengah pada kurva
        ax.scatter(x_mid, y_mid, color='darkblue', s=30, zorder=5, label='Titik Tengah')

        ax.set_title(f"Visualisasi Integral dengan n = {n}", fontsize=14)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)
        
        # Tampilkan grafik di Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
        st.info("Pastikan penulisan fungsi menggunakan format Python yang benar (misal: `x**2` untuk pangkat, atau `np.sin(x)`).")

st.divider()

# ===============================
# FOOTER
# ===============================
st.caption("""
© 2025 | Aplikasi Solusi Integral Numerik | Built with Streamlit, NumPy, and Matplotlib
""")
