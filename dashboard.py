import streamlit as st
import pandas as pd

from program import preprocess, predict

st.title("Student Prediction (Prototype)")

# Definisikan semua kolom
all_columns = [
    "Marital_status", "Application_mode", "Application_order", "Course",
    "Daytime_evening_attendance", "Previous_qualification", "Previous_qualification_grade",
    "Nacionality", "Mothers_qualification", "Fathers_qualification",
    "Mothers_occupation", "Fathers_occupation", "Admission_grade", "Displaced",
    "Educational_special_needs", "Debtor", "Tuition_fees_up_to_date", "Gender",
    "Scholarship_holder", "Age_at_enrollment", "International",
    "Curricular_units_1st_sem_credited", "Curricular_units_1st_sem_enrolled",
    "Curricular_units_1st_sem_evaluations", "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade", "Curricular_units_1st_sem_without_evaluations",
    "Curricular_units_2nd_sem_credited", "Curricular_units_2nd_sem_enrolled",
    "Curricular_units_2nd_sem_evaluations", "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade", "Curricular_units_2nd_sem_without_evaluations",
    "Unemployment_rate", "Inflation_rate", "GDP"
]

# Inisialisasi DataFrame manual
if "manual_data" not in st.session_state:
    st.session_state.manual_data = pd.DataFrame(columns=all_columns)

# Input manual
st.subheader("Add Single Entry (Manual Input)")

manual_input = {}
chunk_size = 6  # tampilkan 6 kolom per baris untuk kepraktisan

for i in range(0, len(all_columns), chunk_size):
    cols = st.columns(chunk_size)
    for j, col in enumerate(all_columns[i:i + chunk_size]):
        if "grade" in col.lower() or "rate" in col.lower() or "GDP" in col:
            manual_input[col] = cols[j].number_input(col, value=0.0)
        else:
            manual_input[col] = cols[j].number_input(col, value=0, step=1)

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
