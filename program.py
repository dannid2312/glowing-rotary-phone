import pandas as pd
import numpy as np
import joblib
import os

def preprocess(df, model_path='model'):
    # Kolom untuk PCA
    pca_academic_columns = [
        'Course', 'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
        'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations'
    ]

    pca_parents_columns = [
        'Mothers_qualification', 'Fathers_qualification',
        'Mothers_occupation', 'Fathers_occupation'
    ]

    # Load semua scaler
    scalers = {}
    for file in os.listdir(model_path):
        if file.startswith("scaler_") and file.endswith(".joblib"):
            col = file.replace("scaler_", "").replace(".joblib", "")
            scalers[col] = joblib.load(os.path.join(model_path, file))

    # Apply semua scaler
    for col, scaler in scalers.items():
        if col in df.columns:
            X = np.asarray(df[col]).reshape(-1, 1)
            df[col] = scaler.transform(X)

    # Load PCA
    pca_academic = joblib.load(os.path.join(model_path, 'pca_academic.joblib'))
    pca_parents = joblib.load(os.path.join(model_path, 'pca_parents.joblib'))

    # PCA transform
    df_pca_academic = pd.DataFrame(
        pca_academic.transform(df[pca_academic_columns]),
        columns=[f'pca_academic_{i+1}' for i in range(pca_academic.n_components_)],
        index=df.index
    )

    df_pca_parents = pd.DataFrame(
        pca_parents.transform(df[pca_parents_columns]),
        columns=[f'pca_parents_{i+1}' for i in range(pca_parents.n_components_)],
        index=df.index
    )

    # Drop kolom asli PCA
    df.drop(columns=pca_academic_columns + pca_parents_columns, inplace=True)

    # Gabungkan hasil PCA
    df = pd.concat([df, df_pca_academic, df_pca_parents], axis=1)

    try: df.drop(columns=['Status'], inplace=True)
    except: pass

    return df

def predict(data):
    model = joblib.load("model/gboost_model.joblib")
    result = model.predict(data)
    result = ['Dropout' if result[i] == 1 else 'Graduate' for i in range(len(result))]
    return result

if __name__ == '__main__':
    df = pd.read_csv("enrolled_students.csv")
    df = preprocess(df)
    print(df)

    print(predict(df))
