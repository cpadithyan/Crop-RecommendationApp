# Crop Recommendation System

## Introduction

### Project Overview

The Crop Recommendation System is a machine learning-based web application designed to help farmers select the most suitable crops based on local soil and climate conditions. The application leverages several machine learning algorithms to provide accurate crop recommendations, improving agricultural productivity and sustainability.

## Key Features

 - Accurate crop recommendations using machine learning
 - User-friendly web interface for easy access
 - Scalable and deployable on cloud platforms
 - Supports multiple machine learning algorithms

## Model Development

### Algorithms Used

- **Decision Tree**: Provides insights into the decision-making process by dividing data into smaller groups based on feature values, creating a tree-like structure.
- **Gaussian Naive Bayes**: Based on Bayes' theorem, assumes features are independent given the class label, often delivering good results with high-dimensional data.
- **Support Vector Machine (SVM)**: Finds the hyperplane in the feature space that best partitions the classes, useful for non-linear data separation.
- **Random Forest**: A cluster learning method combining multiple decision trees for robust classification, handling high-dimensional data effectively.

## Methodology

### System Architecture

The system architecture comprises two main components: the web server and the ML container. The web server communicates with a database to store and retrieve data, ensuring scalability and deployability for handling many requests.

| System Architecture |
|---------------------|
| ![image](https://github.com/ravikant-diwakar/Crop-Recommendation/assets/110620635/2fbb5654-19fb-438c-9cf5-4c6328f44fa7) |


### Datasets

The dataset consists of 2200 rows and 8 columns representing various environmental and soil parameters, including nitrogen, phosphorus, potassium (NPK) levels, temperature, humidity, pH, precipitation, and the target crop label. By analyzing the relationships between these input features and the corresponding crop types, we develop a predictive model for recommending suitable crops for specific soil and environmental conditions.


| Random data from the dataset for crop recommendation |
|------------------------------------------------------|
| ![image](https://github.com/ravikant-diwakar/Crop-Recommendation/assets/110620635/228e1251-7033-461f-9b4d-8fca493482d9) |


### Crop Recommendation

We trained our dataset using four standard machine learning algorithms: Random Forest, Gaussian Naive Bayes, Support Vector Machine (SVM), and Decision Tree. These algorithms perform well on labeled datasets for classification problems, with Random Forest emerging as the most accurate model for crop prediction.

### Analysis Tools and Technologies

- **Python**: Versatile programming language for machine learning.
- **NumPy**: Provides support for large, multi-dimensional arrays and matrices.
- **Pandas**: Powerful library for data manipulation and analysis.
- **Streamlit**: Framework for building interactive web applications.
- **HTML, CSS, JavaScript**: Standard web technologies for designing and styling the web application.

## Results

### Model Performance

Random Forest outperformed other algorithms, achieving an accuracy of 99.55%. A graphical representation of the accuracy comparison among the algorithms is provided.

| Accuracy Comparison |
|---------------------|
| ![image](https://github.com/ravikant-diwakar/Crop-Recommendation/assets/110620635/d1f0c9f0-35cd-4898-9749-e689f9a8d3ec) |


### Website Deployment

The web application, developed using Streamlit, incorporates a machine learning backend for crop recommendation based on user-input parameters. The application is designed for deployment on cloud service platforms, ensuring widespread accessibility and scalability.

| Landing page of the website |
|-----------------------------|
| ![image](https://github.com/ravikant-diwakar/Crop-Recommendation/assets/110620635/b2fc8288-6800-4eeb-8ca7-76c40b6424ba) |

| Result of crop recommendation |
|-----------------------------|
| ![image](https://github.com/ravikant-diwakar/Crop-Recommendation/assets/110620635/1f5cb278-9898-4cf8-98d2-2d8dc96336e7) |

---
