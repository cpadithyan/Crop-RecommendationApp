# Crop Recommendation System

## Abstract

Agriculture plays a crucial role in the economies of many developing countries. Farmers face numerous challenges in meeting the expectations of a changing global community. Factors such as soil erosion, fertilizer shortages, and climate change severely affect crop productivity. Additionally, traditional agricultural methods often rely on instinct and trial-and-error rather than data-driven decision-making, leading to suboptimal results. Our Crop Recommendation System uses machine learning algorithms to address this issue by providing farmers with the knowledge and skills necessary to choose crops suitable for their local climate and soil nutrient levels. We evaluate various algorithms, including Decision Tree, Gaussian Naive Bayes, Support Vector Machine (SVM), and Random Forest, to determine the best crop prediction models. Our experiments show that the Random Forest algorithm is the most accurate. Our goal is to transform crop planning techniques using machine learning, enabling farmers to maximize yields while reducing resource waste.

## Introduction

Machine learning has become a powerful tool for solving challenging problems in various fields, including agriculture. Crop recommendation is one such problem where selecting the right crops is essential for increasing agricultural profitability and production. Our project aims to create a website for crop recommendations in the agricultural industry, using machine learning techniques to help farmers make informed crop selection decisions. By collecting and analyzing data from various sources such as soil databases, climate records, and crop performance data, we develop and assess machine learning models that can forecast the best crops for specific conditions. We compare and evaluate several machine learning techniques, including Decision Tree, Gaussian Naive Bayes, Support Vector Machine (SVM), and Random Forest. The website is designed to be deployed on cloud platforms, enhancing scalability and accessibility, allowing farmers to access guidance services anywhere.

## Motivation

Climate change has significantly impacted agriculture in recent years. Farmers worldwide face challenges due to extreme weather, unpredictable rainfall, and climate change. Inappropriate crop selection often results from limited availability of improved agricultural techniques, leading to lower yields and economic losses. Utilizing technology wisely can address these issues. By combining machine learning algorithms with user-friendly online interfaces, we can provide farmers with access to advanced crop selection tools. These technologies have the potential to optimize agricultural operations and enable data-driven decisions regarding crop selection, improving agricultural productivity and reducing the effects of climate change.

## Literature Review

The use of machine learning (ML) in agriculture has revolutionized how farmers predict crop yields and make decisions. Researchers have extensively studied various ML algorithms for their effectiveness in this field. Among these algorithms, Random Forest consistently predicts crop yields with high accuracy due to its ability to handle large datasets with numerous input variables. Machine learning is also essential for developing recommendation systems for farmers, utilizing historical data and present conditions to provide valuable crop selection advice. Extensive datasets that include a range of crop growth-influencing variables, such as soil type, weather, and farming techniques, are crucial for the continuous improvement of ML models.

## Project Goals and Objectives

Our main aim is to use machine learning to transform crop recommendation and deployment in agriculture. By providing farmers with precise guidance tailored to their specific climate and soil conditions, we aim to improve crop yields and enable data-driven decision-making, enhancing overall agricultural productivity. We explore various machine learning algorithms, including Decision Tree, Gaussian Naive Bayes, Support Vector Machine (SVM), and Random Forest, evaluating them based on accuracy, precision, and recall. We focus on creating scalable and accessible web applications to handle many users and requests. Promoting sustainable agricultural methods and sharing knowledge with relevant parties are also key objectives to enhance environmental sustainability, economic development, and food security.

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
  
