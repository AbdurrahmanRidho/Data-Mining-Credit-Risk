import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load model yang telah dilatih
gradient_boosting_model = joblib.load('gradient_boosting_model.pkl')

# Fungsi untuk memprediksi
def predict(features):
    # Prediksi menggunakan model yang telah diload
    prediction = gradient_boosting_model.predict(features)
    return prediction

# Judul aplikasi
st.title('Aplikasi Prediksi')

# Deskripsi aplikasi
st.write('Masukkan fitur untuk melakukan prediksi.')

# encoder
# Import library yang diperlukan
from sklearn.preprocessing import LabelEncoder

# Data awal
income_type_data = [
    'Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student'
]

# Inisialisasi LabelEncoder
label_encoder_income_type = LabelEncoder()

# Fit transform untuk mengubah data menjadi label encoding
encoded_income_type = label_encoder_income_type.fit_transform(income_type_data)

# Tampilkan hasil label encoding
print(dict(zip(income_type_data, encoded_income_type)))

# Data awal
education_type_data = [
    'Secondary / secondary special', 'Higher education', 'Incomplete higher',
    'Lower secondary', 'Academic degree'
]

# Inisialisasi LabelEncoder
label_encoder_education_type = LabelEncoder()

# Fit transform untuk mengubah data menjadi label encoding
encoded_education_type = label_encoder_education_type.fit_transform(education_type_data)

# Data awal
family_status_data = [
    'Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow'
]

# Inisialisasi LabelEncoder
label_encoder_family_status = LabelEncoder()

# Fit transform untuk mengubah data menjadi label encoding
encoded_family_status = label_encoder_family_status.fit_transform(family_status_data)

# Data awal
housing_type_data = [
    'House / apartment', 'With parents', 'Municipal apartment',
    'Rented apartment', 'Office apartment', 'Co-op apartment'
]

# Inisialisasi LabelEncoder
label_encoder_housing_type = LabelEncoder()

# Fit transform untuk mengubah data menjadi label encoding
encoded_housing_type = label_encoder_housing_type.fit_transform(housing_type_data)


# Data awal
occupation_type_data = [
    'Other', 'Laborers', 'Sales staff', 'Core staff', 'Managers', 'Drivers',
    'High skill tech staff', 'Accountants', 'Medicine staff', 'Cooking staff',
    'Security staff', 'Cleaning staff', 'Private service staff', 'Low-skill Laborers',
    'Secretaries', 'Waiters/barmen staff', 'HR staff', 'IT staff', 'Realty agents'
]

# Inisialisasi LabelEncoder
label_encoder_occupation_type = LabelEncoder()

# Fit transform untuk mengubah data menjadi label encoding
encoded_occupation_type = label_encoder_occupation_type.fit_transform(occupation_type_data)

# Form input dari pengguna
gender = st.selectbox('Gender', ['Female', 'Male'])
own_car = st.selectbox('Own Car', ['Yes', 'No'])
own_property = st.selectbox('Own Property', ['Yes', 'No'])
work_phone = st.selectbox('Work Phone', ['Yes', 'No'])
phone = st.selectbox('Phone', ['Yes', 'No'])
email = st.selectbox('Email', ['Yes', 'No'])
unemployed = st.selectbox('Unemployed', ['Yes', 'No'])
num_children = st.number_input('Number of Children', min_value=0, max_value=10, value=0, step=1)
num_family = st.number_input('Number of Family Members', min_value=1, max_value=10, value=1, step=1)
account_length = st.number_input('Account Length (months)', min_value=0, max_value=600, value=0, step=1)
total_income = st.number_input('Total Income', min_value=0.0, max_value=1e6, value=0.0, step=1000.0)
age = st.number_input('Age', min_value=18, max_value=100, value=18, step=1)
years_employed = st.number_input('Years Employed', min_value=0, max_value=50, value=0, step=1)
income_type = st.selectbox('Income Type', ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student'])
education_type = st.selectbox('Education Type', ['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree'])
family_status = st.selectbox('Family Status', ['Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow'])
housing_type = st.selectbox('Housing Type', ['House / apartment', 'With parents', 'Municipal apartment', 'Rented apartment', 'Office apartment', 'Co-op apartment'])
occupation_type = st.selectbox('Occupation Type', ['Other', 'Laborers', 'Sales staff', 'Core staff', 'Managers', 'Drivers', 'High skill tech staff', 'Accountants', 'Medicine staff', 'Cooking staff', 'Security staff', 'Cleaning staff', 'Private service staff', 'Low-skill Laborers', 'Secretaries', 'Waiters/barmen staff', 'HR staff', 'IT staff', 'Realty agents'])

# Konversi input ke dalam format yang dapat diproses oleh model
gender = 0 if gender == 'Female' else 1
own_car = 1 if own_car == 'Yes' else 0
own_property = 1 if own_property == 'Yes' else 0
work_phone = 1 if work_phone == 'Yes' else 0
phone = 1 if phone == 'Yes' else 0
email = 1 if email == 'Yes' else 0
unemployed = 1 if unemployed == 'Yes' else 0
income_type = label_encoder_income_type.transform([income_type])[0]
education_type = label_encoder_education_type.transform([education_type])[0]
family_status = label_encoder_family_status.transform([family_status])[0]
housing_type = label_encoder_housing_type.transform([housing_type])[0]
occupation_type = label_encoder_occupation_type.transform([occupation_type])[0]

# Memanggil fungsi prediksi dengan input dari pengguna
features = [[gender, own_car, own_property, work_phone, phone, email, unemployed, num_children, num_family, account_length, total_income, age, years_employed, income_type, education_type, family_status, housing_type, occupation_type]]
prediction = predict(features)

# Tombol untuk melakukan prediksi
if st.button('Predict'):
    # Memanggil fungsi prediksi dengan input dari pengguna
    features = [[gender, own_car, own_property, work_phone, phone, email, unemployed, num_children, num_family, account_length, total_income, age, years_employed, income_type, education_type, family_status, housing_type, occupation_type]]
    prediction = predict(features)

    # Menampilkan hasil prediksi
    st.subheader('Hasil Prediksi')
    if prediction[0] == 0:
        st.write('Low Risk')
    else:
        st.write('High Risk')