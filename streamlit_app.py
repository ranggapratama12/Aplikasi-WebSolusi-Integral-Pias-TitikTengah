import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ===============================
# JUDUL APLIKASI
# ===============================
st.title("📐 Aplikasi Website Solusi Integral")
st.subheader("Metode Pias Titik Tengah (Midpoint Rule)")

st.write("""
Aplikasi ini digunakan untuk menghitung **solusi integral numerik**
menggunakan **kaidah titik tengah**.
""")

# ===============================
# INPUT USER
# ===============================
st.sidebar.header("Input Parameter")

fungsi_input = st.sidebar.text_input(
    "Masukkan fungsi f(x)",
    value="x**2"
)

a = st.sidebar.number_input("Batas bawah (a)", value=0.0)
b = st.sidebar.number_input("Batas atas (b)", value=1.0)
n = st.sidebar.number_input("Jumlah pias (n)", min_value=1, value=4, step=1)

# ===============================
# PROSES PERHITUNGAN
# ===============================
x = sp.symbols('x')

try:
    fungsi = sp.sympify(fungsi_input)
    f = sp.lambdify(x, fungsi, "numpy")

    h = (b - a) / n
    titik_tengah = a + h * (np.arange(n) + 0.5)
    hasil = h * np.sum(f(titik_tengah))

    st.success("Perhitungan berhasil!")

    st.write("### 📊 Hasil Perhitungan")
    st.write(f"**Nilai Integral (Metode Titik Tengah):** `{hasil}`")

    # ===============================
    # GRAFIK
    # ===============================
    x_plot = np.linspace(a, b, 400)
    y_plot = f(x_plot)

    fig, ax = plt.subplots()
    ax.plot(x_plot, y_plot, label="f(x)")
    ax.bar(titik_tengah, f(titik_tengah), width=h, alpha=0.3, edgecolor="black")
    ax.set_title("Grafik Pias Titik Tengah")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()

    st.pyplot(fig)

except Exception as e:
    st.error("Terjadi kesalahan pada fungsi yang dimasukkan")
    st.write(e)
