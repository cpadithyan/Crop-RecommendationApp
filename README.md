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

The system architecture comprises two main components: the web server and the ML container. The web server communicates with a SQL database to store and retrieve data, ensuring scalability and deployability for handling many requests.

### Datasets

The dataset consists of 2200 rows and 8 columns representing various environmental and soil parameters, including nitrogen, phosphorus, potassium (NPK) levels, temperature, humidity, pH, precipitation, and the target crop label. By analyzing the relationships between these input features and the corresponding crop types, we develop a predictive model for recommending suitable crops for specific soil and environmental conditions.

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

### Website Deployment

The web application, developed using Streamlit, incorporates a machine learning backend for crop recommendation based on user-input parameters. The application is designed for deployment on cloud service platforms, ensuring widespread accessibility and scalability.

## Future Scope

Future improvements include using additional data sources such as satellite images, drone data, and ground sensors to enhance prediction accuracy. Developing specialized ML models for different agricultural regions and ensuring easy accessibility for all users are key areas for further development.

## Conclusion

Our Crop Recommendation System demonstrates the potential of machine learning in transforming agriculture. By providing farmers with accurate crop yield predictions and insightful advice, we aim to promote sustainable and efficient farming practices. Integrating ML into crop recommendation systems can lead to better resource utilization, reduced environmental impact, and improved living conditions for farmers. This project represents a significant step towards a sustainable and successful agricultural future driven by data-driven insights.

### Web App Link : https://crop-recommn.streamlit.app/
  
