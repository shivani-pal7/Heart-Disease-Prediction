
import streamlit as st
import pandas as pd
import joblib

model=joblib.load('Heart_Logistic_Regression.pkl')
scaler=joblib.load('Heart_scaler.pkl')
expected_columns=joblib.load('Heart_columns.pkl')




st.title('Heart Disease Prediction by Shivani❤️')

st.markdown('Please enter the following details to predict the likelihood of heart disease:')

age=st.slider('Age',18,100,40)
sex=st.selectbox('Sex',['Male','Female'])
chest_pain_type=st.selectbox('Chest Pain Type',['ATA','NAP','ASY','TA'])
resting_blood_pressure=st.slider('Resting Blood Pressure (mm Hg)',80,200,120)
colesterol=st.slider('Cholesterol (mg/dL)',100,600,200)
fasting_blood_sugar=st.selectbox('Fasting Blood Sugar > 120 mg/dL',['Yes','No'])
resting_ecg=st.selectbox('Resting ECG',['Normal','ST-T Abnormality','Left Ventricular Hypertrophy'])
max_HR=st.slider('Maximum Heart Rate Achieved',60,220,150)
exercise_induced_angina=st.selectbox('Exercise Induced Angina',['Yes','No'])
oldpeak=st.slider('Oldpeak (ST depression induced by exercise)',0.0,6.0,1.0)
st_splope=st.selectbox('ST Slope',['Up','Flat','Down'])


if st.button('Predict'):

    raw_input = {
    'Age': age,
    'Sex': sex,
    'Chest Pain Type': chest_pain_type,
    'RestingBP': resting_blood_pressure,
    'Cholesterol': colesterol,
    'FastingBS': fasting_blood_sugar,
    'RestingECG': resting_ecg,
    'MaxHR': max_HR,
    'ExerciseAngina': exercise_induced_angina,
    'Oldpeak': oldpeak,
    'ST_Slope': st_splope
}

    input_df = pd.DataFrame([raw_input])

    # One-Hot Encoding
    input_df = pd.get_dummies(input_df, drop_first=True)

    # Match training columns
    input_df = input_df.reindex(
        columns=expected_columns,
        fill_value=0
    )
    
    # Scaling
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error('🚨 High Risk of Heart Disease 🚨')
    else:
        st.success('✅ Low Risk of Heart Disease ✅')