## 📞 Telecom Churn Prediction

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange)](https://scikit-learn.org)
[![Random Forest](https://img.shields.io/badge/Random%20Forest-1.3.2-green)](https://scikit-learn.org/stable/modules/ensemble.html#forest)
[![Decision Tree](https://img.shields.io/badge/Decision%20Tree-1.3.2-brightgreen)](https://scikit-learn.org/stable/modules/tree.html)
[![Support Vector Classifier](https://img.shields.io/badge/SVC-1.3.2-blueviolet)](https://scikit-learn.org/stable/modules/svm.html)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7.6-red)](https://xgboost.readthedocs.io/)
[![CatBoost](https://img.shields.io/badge/CatBoost-1.2-purple)](https://catboost.ai/)


## 📋 Project Overview
This project focuses on predicting customer churn in the telecom industry using historical customer data and machine learning models. The goal is to detect early signs of churn based on customer demographics, service usage, and account information.

The system combines **data analysis**, **machine learning**, and **web deployment (Flask)** to deliver an interactive and user-friendly churn prediction tool.

## 🎯 Project Goals

- 🧹 Perform data preprocessing and exploratory data analysis (EDA) to understand patterns and correlations related to churn.

- 🧠 Engineer key features to improve the accuracy of predictive models.

- 🤖 Train and evaluate multiple classification algorithms including:

> Random Forest Classifier

> Decision Tree Classifier

> Support Vector Classifier (SVC)

> XGBoost Classifier

> CatBoost Classifier

- ⚖️ Compare model performances and select the best-performing one. 

- 🚀 Deploy the final model using Flask to provide real-time churn predictions via a simple web interface.

## 🧪 Model Performance

After extensive training and evaluation across multiple classifiers, CatBoost Classifier achieved the highest accuracy :


| Model | Accuracy |
|---------|----------------------|
| **Random Forest** | 87 |
| **Decision Tree** | 89 |
| **SVC** | 92 |
| **XGBoost** | 96.27 |
| **CatBoost** | 96.69 |

## 🛠️ Tech Stack
- 🐍 Python 3.8+
- 📦 XGBoost, RandomForest, Decision Tree, Support vector classifier, and CatBoost for model training.
- 📊 Pandas, NumPy for data manipulation
- 📈 Matplotlib, Seaborn for EDA and visualization
- ⚙️ Scikit-learn for preprocessing, metrics, and pipelines
- 🌐 Flask (for web app deployment)
- 💾 Pickle (for model persistence)
- 💻 Jupyter Notebook for development and reporting

## 🧑‍💻 Author
**Mortadha Ferchichi**

- 📧 ferchichii.mortadha@gmail.com
- 🌐 https://github.com/morta123456


