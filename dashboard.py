import streamlit as st
import pandas as pd

from program import preprocess, predict
from columns_dict import all_columns, categorical_options

# Custom CSS for spacing & borders
st.markdown("""
<style>
    .input-section {
        padding: 15px;
        margin-bottom: 20px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #fafafa;
    }
    .section-title {
        font-weight: 600;
        color: #2E86C1;
        margin-bottom: 10px;
    }
    .button-style {
        background-color: #2E86C1;
        color: white;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Prediction (Prototype)")

# Manual Input with expander
with st.expander("Add Single Entry (Manual Input)", expanded=True):
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    manual_input = {}
    chunk_size = 3
    for i in range(0, len(all_columns), chunk_size):
        cols = st.columns(chunk_size)
        for j, col in enumerate(all_columns[i:i + chunk_size]):
            if col in categorical_options:
                options_dict = categorical_options[col]
                choice = cols[j].selectbox(
                    col.replace("_", " ").capitalize(),
                    options=list(options_dict.keys())
                )
                manual_input[col] = options_dict[choice]
            else:
                if "Application_order" in col:
                    manual_input[col] = cols[j].number_input(
                        col.replace("_", " ").capitalize(), min_value=0, max_value=9, step=1, value=0
                    )
                elif "grade" in col.lower():
                    manual_input[col] = cols[j].number_input(
                        col.replace("_", " ").capitalize(), min_value=0.0, max_value=200.0, value=0.0, format="%.1f"
                    )
                elif "rate" in col.lower() or "gdp" in col.lower():
                    manual_input[col] = cols[j].number_input(
                        col.replace("_", " ").capitalize(), value=0.0, format="%.2f"
                    )
                else:
                    manual_input[col] = cols[j].number_input(
                        col.replace("_", " ").capitalize(), value=0, step=1
                    )
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("➕ Add Row", key="add_row"):
        new_row = pd.DataFrame([manual_input])
        if "manual_data" not in st.session_state:
            st.session_state.manual_data = new_row
        else:
            st.session_state.manual_data = pd.concat([st.session_state.manual_data, new_row], ignore_index=True)
        st.success("Row added!")

# Upload CSV with expander
with st.expander("Or Upload CSV"):
    uploaded_file = st.file_uploader("Upload a CSV file with the correct columns", type=["csv"])
    if uploaded_file:
        df_uploaded = pd.read_csv(uploaded_file)
        # Validate columns presence
        missing_cols = [col for col in all_columns if col not in df_uploaded.columns]
        if missing_cols:
            st.error(f"Missing columns in uploaded file: {missing_cols}")
            df_uploaded = pd.DataFrame()
        else:
            df_uploaded = df_uploaded[all_columns]
            st.success(f"Loaded {len(df_uploaded)} rows from CSV.")
    else:
        df_uploaded = pd.DataFrame()

# Combine manual + CSV data
if "manual_data" not in st.session_state:
    st.session_state.manual_data = pd.DataFrame(columns=all_columns)

combined_data = pd.concat([st.session_state.manual_data, df_uploaded], ignore_index=True)

st.subheader("🗂️ Combined Data")
st.dataframe(combined_data, use_container_width=True)

if st.button("🔮 Predict"):
    if combined_data.empty:
        st.warning("No data to predict.")
    else:
        hasil_prediksi = predict(preprocess(combined_data))
        result = combined_data.copy()
        result.insert(0, "Prediction", hasil_prediksi)
        # Optionally highlight predictions
        def highlight_pred(val):
            color = 'background-color: #b3ffb3' if val == 1 else 'background-color: #ffb3b3'
            return color
        st.subheader("📊 Prediction Results")
        st.dataframe(result.style.applymap(highlight_pred, subset=['Prediction']), use_container_width=True)
