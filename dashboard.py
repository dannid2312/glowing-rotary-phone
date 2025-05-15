import streamlit as st
import pandas as pd

# Judul halaman
st.title("Upload dan Tampilkan CSV")

# Upload file
uploaded_file = st.file_uploader("Silakan upload file CSV", type=["csv"])

# Jika file sudah diunggah
if uploaded_file is not None:
    try:
        # Baca file sebagai DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Tampilkan DataFrame
        st.subheader("Isi File CSV:")
        st.dataframe(df)

        # Info tambahan
        st.write(f"Jumlah baris: {df.shape[0]}")
        st.write(f"Jumlah kolom: {df.shape[1]}")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
else:
    st.info("Belum ada file yang diupload.")
