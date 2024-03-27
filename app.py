import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics

# Sidebar
st.sidebar.title("DA PROJECT")
app_mode = st.sidebar.selectbox("Select Page", ["HOME", "ABOUT", "CROP PREDICTION"], index=0)  # Set default index to 2

# Display Image
img = Image.open("crop.png")
st.image(img)

# Load Dataset
df = pd.read_csv('Crop_recommendation.csv')
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Split the data into training and testing sets
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=42)
RF = RandomForestClassifier(n_estimators=20, random_state=5)
RF.fit(Xtrain, Ytrain)

# Dump the trained Random Forest classifier with Pickle
RF_pkl_filename = 'RF.pkl'
with open(RF_pkl_filename, 'wb') as file:
    pickle.dump(RF, file)

# Main Page
if app_mode == "HOME":
    st.markdown("<h1 style='text-align: center;'>CROP RECOMMENDATION</h1>", unsafe_allow_html=True)
    st.subheader("Welcome to our Crop Recommendation Web App!")
    st.write("This app helps farmers predict the most suitable crop to grow based on various environmental factors. Our innovative platform uses advanced data analytics techniques to recommend the best crops for your land based on various factors such as soil nutrients, temperature, humidity, pH levels, and rainfall. With our user-friendly interface, you can easily input your crop details and receive tailored recommendations in just a few clicks. Explore our website to learn more about how our Crop Recommendation Web App works and how it can benefit you!")
    
    st.subheader("How it Works:")
    st.write("1. Navigate to the 'CROP PREDICTION' page from the sidebar.")
    st.write("2. Enter details about your soil and environmental conditions.")
    st.write("3. Click on the 'Predict' button to get the recommended crop.")

elif app_mode == "ABOUT":
    st.markdown("<h1 style='text-align: center;'>CROP RECOMMENDATION</h1>", unsafe_allow_html=True)
    st.write("This Crop Recommendation App is developed as a part of a Data Analytics project. Our Crop Recommendation Web App is designed to assist farmers in making informed decisions about crop selection, ultimately leading to improved agricultural productivity and sustainability.")
    st.write("Utilizing the power of data analytics, our platform analyzes various factors including soil nutrients (Nitrogen, Phosphorus, Potassium), environmental conditions (temperature, humidity, rainfall), and soil pH levels to generate personalized crop recommendations. By considering these crucial parameters, we aim to optimize crop selection for specific land conditions, thereby enhancing yield and profitability for farmers.")

    st.subheader("Key Features:")
    st.write("- Predicts the most suitable crop based on soil and environmental conditions.")
    st.write("- Uses a Random Forest classifier trained on a dataset of crop parameters.")
    st.write("- Provides easy-to-use interface for farmers to make informed decisions.")

elif app_mode == "CROP PREDICTION":
    st.markdown("<h1 style='text-align: center;'>CROP PREDICTION</h1>", unsafe_allow_html=True)

    # Load the trained Random Forest model
    RF_Model_pkl = pickle.load(open('RF.pkl', 'rb'))

    # Function to make predictions
    def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
        prediction = RF_Model_pkl.predict([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        return prediction

    # Streamlit code for the web app interface
    st.sidebar.title("DA PROJECT")
    st.sidebar.header("Enter Crop Details")
    nitrogen = st.sidebar.number_input("Nitrogen", min_value=0.0, max_value=140.0, value=0.0, step=0.1)
    phosphorus = st.sidebar.number_input("Phosphorus", min_value=0.0, max_value=145.0, value=0.0, step=0.1)
    potassium = st.sidebar.number_input("Potassium", min_value=0.0, max_value=205.0, value=0.0, step=0.1)
    temperature = st.sidebar.number_input("Temperature (°C)", min_value=0.0, max_value=51.0, value=0.0, step=0.1)
    humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    ph = st.sidebar.number_input("pH Level", min_value=0.0, max_value=14.0, value=0.0, step=0.1)
    rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)

    if st.sidebar.button("Predict"):
        inputs = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        if not inputs.any() or np.isnan(inputs).any() or (inputs == 0).all():
            st.error("Please fill in all input fields with valid values before predicting.")
        else:
            prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
            st.success(f"The recommended crop is: {prediction[0]}")
