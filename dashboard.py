import streamlit as st
import pandas as pd

from program import preprocess, predict
from columns_dict import all_columns, categorical_options

st.title("Student Prediction (Prototype)")

# Inisialisasi DataFrame manual
if "manual_data" not in st.session_state:
    st.session_state.manual_data = pd.DataFrame(columns=all_columns)

# Input manual
st.subheader("Add Single Entry (Manual Input)")
       
# Saat input manual
manual_input = {}
chunk_size = 3

for i in range(0, len(all_columns), chunk_size):
    cols = st.columns(chunk_size)
    for j, col in enumerate(all_columns[i:i + chunk_size]):
        if col in categorical_options:
            options_dict = categorical_options[col]
            choice = cols[j].selectbox(
                col,
                options=list(options_dict.keys())
            )
            manual_input[col] = options_dict[choice]
        else:
            # numerik biasa
            if "Application_order" in col:
                manual_input[col] = cols[j].number_input(
                    col, min_value=0, max_value=9, step=1, value=0
                )
            elif "grade" in col.lower():
                manual_input[col] = cols[j].number_input(
                    col, min_value=0.0, max_value=200.0, value=0.0
                )
            elif "rate" in col.lower() or "gdp" in col.lower():
                manual_input[col] = cols[j].number_input(
                    col, value=0.0
                )
            else:
                manual_input[col] = cols[j].number_input(
                    col, value=0, step=1
                )

# Tambahkan baris ke DataFrame session_state
if st.button("Add Row"):
    new_row = pd.DataFrame([manual_input])
    st.session_state.manual_data = pd.concat([st.session_state.manual_data, new_row], ignore_index=True)
    st.success("Row added.")

# Upload CSV
st.subheader("Or Upload CSV")
uploaded_file = st.file_uploader("Upload a CSV file with the correct columns", type=["csv"])

if uploaded_file:
    df_uploaded = pd.read_csv(uploaded_file)[all_columns]
else:
    df_uploaded = pd.DataFrame()

# Gabungkan data manual dan CSV
combined_data = pd.concat([st.session_state.manual_data, df_uploaded], ignore_index=True)
result = combined_data.copy()

st.subheader("Combined Data")
st.dataframe(combined_data)

# Tombol prediksi
if st.button("Predict"):
    if combined_data.empty:
        st.warning("No data to predict.")
    else:
        st.write("🔮 This is where your model prediction will go.")
        hasil_prediksi = predict(preprocess(combined_data))
        result.insert(0, "Prediction", hasil_prediksi)
        st.dataframe(result)
