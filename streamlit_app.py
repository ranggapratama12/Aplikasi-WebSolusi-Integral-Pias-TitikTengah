import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# KONFIGURASI HALAMAN
# ===============================
st.set_page_config(
    page_title="Kalkulator Integral - Metode Titik Tengah",
    page_icon="📐",
    layout="centered"
)

# ===============================
# HEADER
# ===============================
st.title("📐 Kalkulator Integral Numerik")
st.subheader("Metode Pias Titik Tengah (Midpoint Rule)")

st.markdown("""
Aplikasi ini digunakan untuk menghitung **estimasi integral tentu**
menggunakan **Metode Titik Tengah (Midpoint Rule)**.
""")

st.divider()

# ===============================
# INPUT SECTION
# ===============================
st.header("🧮 Input Parameter Integral")

func_str = st.text_input(
    "Masukkan fungsi f(x)",
    value="x**2",
    help="Gunakan x sebagai variabel. Contoh: x**2, np.sin(x), np.exp(x)"
)

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Batas bawah (a)", value=0.0)
with col2:
    b = st.number_input("Batas atas (b)", value=1.0)

n = st.number_input(
    "Jumlah pias (n)",
    min_value=1,
    step=1,
    value=4
)

# ===============================
# PROSES PERHITUNGAN
# ===============================
if st.button("🔍 Hitung Integral"):
    try:
        if a >= b:
            st.error("Batas bawah (a) harus lebih kecil dari batas atas (b).")
        else:
            # Fungsi matematika
            def f(x):
                return eval(func_str, {"np": np, "x": x})

            # Lebar pias
            dx = (b - a) / n

            # Titik tengah
            x_mid = np.linspace(a + dx/2, b - dx/2, n)
            y_mid = f(x_mid)

            # Perhitungan integral
            integral = np.sum(y_mid) * dx

            # ===============================
            # OUTPUT
            # ===============================
            st.divider()
            st.header("📊 Hasil Perhitungan")

            st.success(f"**Nilai Estimasi Integral:** {integral:.6f}")

            st.markdown(f"""
            **Rumus Metode Titik Tengah:**  
            \\[
            \\int_a^b f(x) dx \\approx \\Delta x \\sum f(x_i^*)
            \\]
            dengan:
            - \\(\\Delta x = \\frac{{b-a}}{{n}} = {dx:.4f} \\
            - Jumlah pias = {n}
            """)

            # ===============================
            # VISUALISASI
            # ===============================
            st.subheader("📈 Visualisasi Grafik")

            fig, ax = plt.subplots(figsize=(10, 5))

            # Kurva fungsi
            x_curve = np.linspace(a, b, 300)
            y_curve = f(x_curve)
            ax.plot(x_curve, y_curve, color='red', linewidth=2, label='f(x)')

            # Pias midpoint
            x_left = np.linspace(a, b - dx, n)
            ax.bar(
                x_left,
                y_mid,
                width=dx,
                align='edge',
                alpha=0.35,
                edgecolor='blue',
                label='Pias Titik Tengah'
            )

            # Titik tengah
            ax.scatter(x_mid, y_mid, color='black', zorder=5)

            ax.set_title(f"Visualisasi Metode Titik Tengah (n = {n})")
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.legend()
            ax.grid(True, linestyle='--', alpha=0.6)

            st.pyplot(fig)

    except Exception as e:
        st.error("Terjadi kesalahan pada fungsi.")
        st.info("Contoh penulisan yang benar: x**2, np.sin(x), np.exp(x)")
        st.code(str(e))

st.divider()

# ===============================
# FOOTER
# ===============================
st.caption("© 2025 Rangga Pratama W | Kalkulator Integral Numerik - Metode Titik Tengah")
