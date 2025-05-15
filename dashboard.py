import streamlit as st
import pandas as pd

from program import preprocess, prediction

st.header("Student Prediction (Prototype)")

data = pd.DataFrame()

# Baris 1: beberapa variabel kategorikal kecil (asumsi)
col1, col2, col3, col4 = st.columns(4)
with col1:
    Marital_status = int(st.number_input('Marital_status', value=1))
    data["Marital_status"] = [Marital_status]
with col2:
    Application_mode = int(st.number_input('Application_mode', value=1))
    data["Application_mode"] = [Application_mode]
with col3:
    Application_order = int(st.number_input('Application_order', value=1))
    data["Application_order"] = [Application_order]
with col4:
    Course = int(st.number_input('Course', value=1))
    data["Course"] = [Course]

# Baris 2: Daytime_evening_attendance dan Previous qualification
col1, col2, col3, col4 = st.columns(4)
with col1:
    Daytime_evening_attendance = int(st.number_input('Daytime_evening_attendance', value=1))
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
with col2:
    Previous_qualification = int(st.number_input('Previous_qualification', value=1))
    data["Previous_qualification"] = [Previous_qualification]
with col3:
    Previous_qualification_grade = float(st.number_input('Previous_qualification_grade', value=12.0))
    data["Previous_qualification_grade"] = [Previous_qualification_grade]
with col4:
    Nacionality = int(st.number_input('Nacionality', value=1))
    data["Nacionality"] = [Nacionality]

# Baris 3: Kualifikasi dan pekerjaan orang tua
col1, col2, col3, col4 = st.columns(4)
with col1:
    Mothers_qualification = int(st.number_input('Mothers_qualification', value=1))
    data["Mothers_qualification"] = [Mothers_qualification]
with col2:
    Fathers_qualification = int(st.number_input('Fathers_qualification', value=1))
    data["Fathers_qualification"] = [Fathers_qualification]
with col3:
    Mothers_occupation = int(st.number_input('Mothers_occupation', value=1))
    data["Mothers_occupation"] = [Mothers_occupation]
with col4:
    Fathers_occupation = int(st.number_input('Fathers_occupation', value=1))
    data["Fathers_occupation"] = [Fathers_occupation]

# Baris 4: Admission_grade dan flag biner lainnya
col1, col2, col3, col4 = st.columns(4)
with col1:
    Admission_grade = float(st.number_input('Admission_grade', value=12.0))
    data["Admission_grade"] = [Admission_grade]
with col2:
    Displaced = int(st.number_input('Displaced', value=0))
    data["Displaced"] = [Displaced]
with col3:
    Educational_special_needs = int(st.number_input('Educational_special_needs', value=0))
    data["Educational_special_needs"] = [Educational_special_needs]
with col4:
    Debtor = int(st.number_input('Debtor', value=0))
    data["Debtor"] = [Debtor]

# Baris 5: Tuition_fees_up_to_date, Gender, Scholarship_holder, Age_at_enrollment
col1, col2, col3, col4 = st.columns(4)
with col1:
    Tuition_fees_up_to_date = int(st.number_input('Tuition_fees_up_to_date', value=1))
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
with col2:
    Gender = int(st.number_input('Gender', value=1))
    data["Gender"] = [Gender]
with col3:
    Scholarship_holder = int(st.number_input('Scholarship_holder', value=0))
    data["Scholarship_holder"] = [Scholarship_holder]
with col4:
    Age_at_enrollment = int(st.number_input('Age_at_enrollment', value=18))
    data["Age_at_enrollment"] = [Age_at_enrollment]

# Baris 6: International, Units curricular semester 1
col1, col2, col3, col4 = st.columns(4)
with col1:
    International = int(st.number_input('International', value=0))
    data["International"] = [International]
with col2:
    Curricular_units_1st_sem_credited = int(st.number_input('Curricular_units_1st_sem_credited', value=1))
    data["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]
with col3:
    Curricular_units_1st_sem_enrolled = int(st.number_input('Curricular_units_1st_sem_enrolled', value=1))
    data["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]
with col4:
    Curricular_units_1st_sem_evaluations = int(st.number_input('Curricular_units_1st_sem_evaluations', value=1))
    data["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]

# Baris 7: More units curricular semester 1
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_1st_sem_approved = int(st.number_input('Curricular_units_1st_sem_approved', value=1))
    data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]
with col2:
    Curricular_units_1st_sem_grade = float(st.number_input('Curricular_units_1st_sem_grade', value=14.0))
    data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]
with col3:
    Curricular_units_1st_sem_without_evaluations = int(st.number_input('Curricular_units_1st_sem_without_evaluations', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = [Curricular_units_1st_sem_without_evaluations]

# Baris 8: Curricular units 2nd semester
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_2nd_sem_credited = int(st.number_input('Curricular_units_2nd_sem_credited', value=1))
    data["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]
with col2:
    Curricular_units_2nd_sem_enrolled = int(st.number_input('Curricular_units_2nd_sem_enrolled', value=1))
    data["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]
with col3:
    Curricular_units_2nd_sem_evaluations = int(st.number_input('Curricular_units_2nd_sem_evaluations', value=1))
    data["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]
with col4:
    Curricular_units_2nd_sem_approved = int(st.number_input('Curricular_units_2nd_sem_approved', value=1))
    data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]

# Baris 9: More curricular units 2nd semester
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_2nd_sem_grade = float(st.number_input('Curricular_units_2nd_sem_grade', value=14.0))
    data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]
with col2:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input('Curricular_units_2nd_sem_without_evaluations', value=0))
    data["Curricular_units_2nd_sem_without_evaluations"] = [Curricular_units_2nd_sem_without_evaluations]
with col3:
    Unemployment_rate = float(st.number_input('Unemployment_rate', value=6.0))
    data["Unemployment_rate"] = [Unemployment_rate]
with col4:
    Inflation_rate = float(st.number_input('Inflation_rate', value=2.5))
    data["Inflation_rate"] = [Inflation_rate]

# Baris 10: GDP
col1, col2 = st.columns(2)
with col1:
    GDP = float(st.number_input('GDP', value=20000))
    data["GDP"] = [GDP]

# Tampilkan data mentah
with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

# Tombol predict (fungsi prediksi dan preprocessing harus disediakan)
if st.button('Predict'):
    # Contoh pemanggilan fungsi, sesuaikan dengan fungsi preprocess dan prediksi yang kamu punya
    new_data = data_preprocessing(data=data)  
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Prediction Result: {}".format(prediction(new_data)))
