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
Tinggi pias diambil dari nilai fungsi pada **titik tengah** setiap sub-interval.
""")

st.divider()

# ===============================
# INPUT SECTION
# ===============================
st.header("🧮 Input Parameter Integral")

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
        # Menyiapkan fungsi matematika
        def f(x):
            return eval(func_str, {"np": np, "x": x})

        # --- LOGIKA PERHITUNGAN ---
        dx = (b - a) / n
        x_mid = np.linspace(a + dx/2, b - dx/2, n)
        y_mid = f(x_mid)
        integral_result = np.sum(y_mid) * dx

        # ===============================
        # OUTPUT SECTION
        # ===============================
        st.divider()
        st.header("📊 Hasil Perhitungan")
        
        st.success(f"**Nilai Estimasi Integral:** {integral_result:.6f}")

        # --- VISUALISASI ---
        # Pastikan baris di bawah ini sejajar dengan 'st.success' di atas
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Plot kurva f(x)
        x_curve = np.linspace(a, b, 200)
        y_curve = f(x_curve)
        ax.plot(x_curve, y_curve, 'red', label='f(x)', linewidth=2)

        # Plot pias (bar chart)
        x_left = np.linspace(a, b - dx, n)
        ax.bar(x_left, y_mid, width=dx, align='edge', alpha=0.3, 
               color='skyblue', edgecolor='blue', label='Pias Titik Tengah')
        
        # Penanda titik tengah
        ax.scatter(x_mid, y_mid, color='darkblue', s=30, zorder=5)

        ax.set_title(f"Visualisasi Midpoint Rule (n={n})")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)
        
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

st.divider()

# ===============================
# FOOTER
# ===============================
st.caption("© 2025 Rangga Pratama W | Website | Aplikasi Solusi Integral Numerik | Powered by Streamlit")
