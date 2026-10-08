# 🚦 Smart Traffic Congestion Predictor

> An AI-powered Traffic Congestion Prediction System that uses Weather and Time-based Features to predict congestion levels using Machine Learning.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

Urban traffic congestion is a major challenge in modern cities, causing delays, fuel wastage, and increased pollution.

This project leverages Machine Learning to predict traffic congestion levels based on:

- Weather Conditions
- Time of Day
- Day of Week
- Seasonal Trends
- Rush Hour Indicators

The system helps in understanding traffic patterns and can be extended for smart city traffic management solutions.

---

## 🎯 Problem Statement

Traffic congestion significantly impacts:

- Travel Time
- Fuel Consumption
- Air Pollution
- Road Safety

The objective of this project is to build a predictive model capable of estimating congestion levels using historical traffic and weather data.

---

## 📊 Dataset

### Dataset Used
Metro Interstate Traffic Volume Dataset

The dataset contains:

- Traffic Volume
- Temperature
- Rainfall
- Snowfall
- Cloud Coverage
- Weather Conditions
- Date & Time Information

---

## 🔍 Exploratory Data Analysis

The following analyses were performed:

### Data Cleaning
- Missing Value Handling
- Duplicate Removal
- Feature Engineering

### Feature Engineering
Created new features:

- Hour
- Month
- Day of Week
- Rush Hour Indicator
- Weekend Indicator

### Visualization
- Traffic Distribution
- Hour-wise Traffic Analysis
- Weather Impact Analysis
- Correlation Analysis
- Feature Importance Analysis

---

## 🤖 Machine Learning Model

### Model Used

✅ Random Forest Classifier

Reasons for selection:

- Handles Non-Linear Relationships
- Robust Against Overfitting
- High Prediction Accuracy
- Works Well with Mixed Features

---

## 📈 Feature Importance

Top features influencing congestion prediction:

| Feature | Importance |
|----------|------------|
| Hour | 0.593 |
| Temperature | 0.149 |
| Month | 0.051 |
| Rush Hour | 0.046 |
| Weekend | 0.040 |
| Cloud Coverage | 0.035 |

Key Insight:

> Traffic congestion is primarily influenced by the time of day, making hourly traffic patterns the strongest predictor.

---

## 🏗️ Project Structure

```bash
Smart-Traffic-Congestion-Predictor/
│
├── app/
│   └── predict.py
│
├── data/
│   └── Metro_Interstate_Traffic_Volume.csv
│
├── models/
│   ├── traffic_rf_model.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   └── traffic_analysis.ipynb
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/rajshete1110-rgb/Smart-Traffic-Congestion-Predictor.git
```

### Navigate to Project

```bash
cd Smart-Traffic-Congestion-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Prediction

```bash
python app/predict.py
```

---

## 🧪 Sample Prediction

### Input

```python
{
 'temp': 280,
 'rain_1h': 0,
 'snow_1h': 0,
 'clouds_all': 90,
 'hour': 17,
 'month': 12,
 'is_weekend': 0,
 'rush_hour': 1
}
```

### Output

```text
Predicted Congestion Level: High
```

---

## 📌 Future Improvements

- Real-Time Traffic Prediction
- Live Weather API Integration
- Streamlit Dashboard
- Traffic Heatmaps
- Deep Learning Models
- Smart Traffic Signal Integration
- Deployment on Cloud

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Joblib
- Jupyter Notebook
- Git & GitHub

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Machine Learning Model Building
- Model Evaluation
- Feature Importance Analysis
- Git & GitHub Version Control

---

## 👨‍💻 Author

### Raj Shete

B.E. Computer Engineering Student  
Aspiring AI/ML Engineer

GitHub:
https://github.com/rajshete1110-rgb

LinkedIn:
https://www.linkedin.com/in/rajshete/

---

⭐ If you found this project useful, consider giving it a star.
