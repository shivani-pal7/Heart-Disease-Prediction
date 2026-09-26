# ❤️ Heart Disease Prediction

A Machine Learning web application that predicts the **likelihood of heart disease** based on user-provided health-related parameters.

The project uses **Logistic Regression** for classification and **Streamlit** to create an interactive web interface.

## 📌 Project Overview

This project takes several input parameters such as age, blood pressure, cholesterol, chest pain type, maximum heart rate, and other related features.

The trained Logistic Regression model processes these inputs and provides a prediction:

* ✅ Low Risk of Heart Disease
* 🚨 High Risk of Heart Disease

> **Note:** This project is created for educational and demonstration purposes. The prediction is a machine-learning model output and should not be considered a medical diagnosis.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Logistic Regression
* StandardScaler
* Joblib
* Streamlit

## 📊 Input Features

The application uses the following features:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise Induced Angina
* Oldpeak
* ST Slope

## 🤖 Machine Learning Model

Different classification algorithms were evaluated during the project:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Naive Bayes
* Decision Tree
* Support Vector Machine (SVM)

**Logistic Regression** was selected for the deployed application.

### Data Preprocessing

The project includes:

1. One-Hot Encoding for categorical features
2. Standard Scaling for numerical features
3. Train-test split
4. Logistic Regression model training

## 🌐 Streamlit Application

The trained model is integrated with Streamlit to provide an interactive interface where users can enter feature values and receive a model prediction.

## 📁 Project Structure

```text
Heart-Disease-Prediction/
│
├── app.py
├── Heart_Logistic_Regression.pkl
├── Heart_scaler.pkl
├── Heart_columns.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/shivani-pal7/Heart-Disease-Prediction.git
```

### 2. Open the project folder

```bash
cd Heart-Disease-Prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 💡 Key Learning

Through this project, I practiced:

* Data preprocessing
* One-hot encoding
* Feature scaling
* Classification algorithms
* Model evaluation
* Model saving using Joblib
* Building a Streamlit application
* Deploying a machine learning project

## 👩‍💻 Author

**Shivani Pal**

GitHub: [shivani-pal7](https://github.com/shivani-pal7)


