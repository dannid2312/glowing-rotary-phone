import streamlit as st
import pandas as pd

from program import preprocess, predict

st.title("Student Prediction (Prototype)")

# Definisikan semua kolom
categorical_columns = [
    "Marital_status", "Application_mode", "Course",
    "Daytime_evening_attendance", "Previous_qualification", 
    "Nacionality", "Mothers_qualification", "Fathers_qualification",
    "Mothers_occupation", "Fathers_occupation",  "Displaced",
    "Educational_special_needs", "Debtor", "Tuition_fees_up_to_date", "Gender",
    "Scholarship_holder", "Age_at_enrollment", "International"
]

numerical_columns = [
    "Application_order", "Previous_qualification_grade", "Admission_grade",
    "Curricular_units_1st_sem_credited", "Curricular_units_1st_sem_enrolled",
    "Curricular_units_1st_sem_evaluations", "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade", "Curricular_units_1st_sem_without_evaluations",
    "Curricular_units_2nd_sem_credited", "Curricular_units_2nd_sem_enrolled",
    "Curricular_units_2nd_sem_evaluations", "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade", "Curricular_units_2nd_sem_without_evaluations",
    "Unemployment_rate", "Inflation_rate", "GDP"
]

all_columns = categorical_columns + numerical_columns

# Inisialisasi DataFrame manual
if "manual_data" not in st.session_state:
    st.session_state.manual_data = pd.DataFrame(columns=all_columns)

# Input manual
st.subheader("Add Single Entry (Manual Input)")

# Mapping pilihan untuk semua kolom kategorikal yang ingin dropdown
categorical_options = {
    "Marital_status": {
        "Single": 1,
        "Married": 2,
        "Widower": 3,
        "Divorced": 4,
        "Facto union": 5,
        "Legally separated": 6
    },
    "Application_mode": {
        "1st phase - general contingent": 1,
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5,
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10,
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16,
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18,
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
        "Over 23 years old": 39,
        "Transfer": 42,
        "Change of course": 43,
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51,
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57
    },
    "Course": {
        "Biofuel Production Technologies": 33,
        "Animation and Multimedia Design": 171,
        "Social Service (evening attendance)": 8014,
        "Agronomy": 9003,
        "Communication Design": 9070,
        "Veterinary Nursing": 9085,
        "Informatics Engineering": 9119,
        "Equinculture": 9130,
        "Management": 9147,
        "Social Service": 9238,
        "Tourism": 9254,
        "Nursing": 9500,
        "Oral Hygiene": 9556,
        "Advertising and Marketing Management": 9670,
        "Journalism and Communication": 9773,
        "Basic Education": 9853,
        "Management (evening attendance)": 9991
    },
    "Daytime_evening_attendance": {
        "Evening": 0,
        "Daytime": 1,
    },
    "Previous_qualification": {
        "Secondary education": 1,
        "Higher education - bachelor's degree": 2,
        "Higher education - degree": 3,
        "Higher education - master's": 4,
        "Higher education - doctorate": 5,
        "Frequency of higher education": 6,
        "12th year of schooling - not completed": 9,
        "11th year of schooling - not completed": 10,
        "Other - 11th year of schooling": 12,
        "10th year of schooling": 14,
        "10th year of schooling - not completed": 15,
        "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
        "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Professional higher technical course": 42,
        "Higher education - master (2nd cycle)": 43
    },
    "Nacionality": {
        "Portuguese": 1,
        "German": 2,
        "Spanish": 6,
        "Italian": 11,
        "Dutch": 13,
        "English": 14,
        "Lithuanian": 17,
        "Angolan": 21,
        "Cape Verdean": 22,
        "Guinean": 24,
        "Mozambican": 25,
        "Santomean": 26,
        "Turkish": 32,
        "Brazilian": 41,
        "Romanian": 62,
        "Moldova (Republic of)": 100,
        "Mexican": 101,
        "Ukrainian": 103,
        "Russian": 105,
        "Cuban": 108,
        "Colombian": 109
    },
    "Mothers_qualification": {
        "Secondary Education - 12th Year of Schooling or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year of Schooling - Not Completed": 9,
        "11th Year of Schooling - Not Completed": 10,
        "7th Year (Old)": 11,
        "Other - 11th Year of Schooling": 12,
        "10th Year of Schooling": 14,
        "General commerce course": 18,
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
        "Technical-professional course": 22,
        "7th year of schooling": 26,
        "2nd cycle of the general high school course": 27,
        "9th Year of Schooling - Not Completed": 29,
        "8th year of schooling": 30,
        "Unknown": 34,
        "Can't read or write": 35,
        "Can read without having a 4th year of schooling": 36,
        "Basic education 1st cycle (4th/5th year) or equiv.": 37,
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Specialized higher studies course": 41,
        "Professional higher technical course": 42,
        "Higher Education - Master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    },
    "Fathers_qualification": {
        "Secondary Education - 12th Year of Schooling or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year of Schooling - Not Completed": 9,
        "11th Year of Schooling - Not Completed": 10,
        "7th Year (Old)": 11,
        "Other - 11th Year of Schooling": 12,
        "2nd year complementary high school course": 13,
        "10th Year of Schooling": 14,
        "General commerce course": 18,
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
        "Complementary High School Course": 20,
        "Technical-professional course": 22,
        "Complementary High School Course - not concluded": 25,
        "7th year of schooling": 26,
        "2nd cycle of the general high school course": 27,
        "9th Year of Schooling - Not Completed": 29,
        "8th year of schooling": 30,
        "General Course of Administration and Commerce": 31,
        "Supplementary Accounting and Administration": 33,
        "Unknown": 34,
        "Can't read or write": 35,
        "Can read without having a 4th year of schooling": 36,
        "Basic education 1st cycle (4th/5th year) or equiv.": 37,
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Specialized higher studies course": 41,
        "Professional higher technical course": 42,
        "Higher Education - Master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    },
    "Mothers_occupation": {
        "Student": 0,
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
        "Specialists in Intellectual and Scientific Activities": 2,
        "Intermediate Level Technicians and Professions": 3,
        "Administrative staff": 4,
        "Personal Services, Security and Safety Workers and Sellers": 5,
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
        "Skilled Workers in Industry, Construction and Craftsmen": 7,
        "Installation and Machine Operators and Assembly Workers": 8,
        "Unskilled Workers": 9,
        "Armed Forces Professions": 10,
        "Other Situation": 90,
        "(blank)": 99,
        "Health professionals": 122,
        "Teachers": 123,
        "Specialists in information and communication technologies (ICT)": 125,
        "Intermediate level science and engineering technicians and professions": 131,
        "Technicians and professionals, of intermediate level of health": 132,
        "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
        "Office workers, secretaries in general and data processing operators": 141,
        "Data, accounting, statistical, financial services and registry-related operators": 143,
        "Other administrative support staff": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers and the like": 153,
        "Skilled construction workers and the like, except electricians": 171,
        "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
        "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
        "Cleaning workers": 191,
        "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
        "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
        "Meal preparation assistants": 194
    },
    "Fathers_occupation": {
        "Student": 0,
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
        "Specialists in Intellectual and Scientific Activities": 2,
        "Intermediate Level Technicians and Professions": 3,
        "Administrative staff": 4,
        "Personal Services, Security and Safety Workers and Sellers": 5,
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
        "Skilled Workers in Industry, Construction and Craftsmen": 7,
        "Installation and Machine Operators and Assembly Workers": 8,
        "Unskilled Workers": 9,
        "Armed Forces Professions": 10,
        "Other Situation": 90,
        "(blank)": 99,
        "Armed Forces Officers": 101,
        "Armed Forces Sergeants": 102,
        "Other Armed Forces personnel": 103,
        "Directors of administrative and commercial services": 112,
        "Hotel, catering, trade and other services directors": 114,
        "Specialists in the physical sciences, mathematics, engineering and related techniques": 121,
        "Health professionals": 122,
        "Teachers": 123,
        "Specialists in finance, accounting, administrative organization, public and commercial relations": 124,
        "Intermediate level science and engineering technicians and professions": 131,
        "Technicians and professionals, of intermediate level of health": 132,
        "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
        "Information and communication technology technicians": 135,
        "Office workers, secretaries in general and data processing operators": 141,
        "Data, accounting, statistical, financial services and registry-related operators": 143,
        "Other administrative support staff": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers and the like": 153,
        "Protection and security services personnel": 154,
        "Market-oriented farmers and skilled agricultural and animal production workers": 161,
       
# Saat input manual
manual_input = {}
chunk_size = 4

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
