import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model_sav', 'rb'))

#judul lweb
st.title('DATA MINING PREDIKSI DIABETES')

#membagi kolom



Pregnancies = st.text_input ('Input Nilai Pregnancies')

Glucose = st.text_input ('Input Nilai Glucose')

BloodPressure = st.text_input ('Input Nilai Blood Pressure')

SkinThickness = st.text_input ('Input Nilai Skin Thickness')

Insulin = st.text_input ('Input Nilai Insulin')

BMI = st.text_input ('Input Nilai BMI')

DiabetesPedigreeFunction = st.text_input ('Input Nilai Diabetes Pedigree Function')

Age = st.text_input ('Input Nilai Age')

#code untuk prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes') :
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1): 
        diab_diagnosis = 'Pasien terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
       
    st.success(diab_diagnosis)