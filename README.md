# 🍷 Wine Quality Prediction

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Model](https://img.shields.io/badge/Model-Random_Forest-green)
![Task](https://img.shields.io/badge/Task-Multiclass_Classification-red)
![Interface](https://img.shields.io/badge/Interface-CLI-purple)

A machine learning project that predicts the quality of **Red Wine** and **White Wine** using two independently trained models. The project is designed as a **Command Line Interface (CLI)** application, allowing users to select the wine type and receive quality predictions directly from the terminal.

## 🚀 Features

* 🔴 Dedicated model for **Red Wine Quality Prediction**
* ⚪ Dedicated model for **White Wine Quality Prediction**
* 💻 Simple and interactive **CLI interface**
* 🧹 Data preprocessing pipeline
* 📊 Model evaluation using multiple metrics
* ⚖️ Designed to work with imbalanced real-world datasets
* 📁 Modular project structure for easier maintenance and expansion

## 🛠️ Tech Stack

* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **SciPy**
* **Scikit-Learn**
* **XGBoost**
* **OS**
* **SYS**

## 📂 Project Structure

```text
Wine-Quality-Prediction/
│
├── dataset/
│
├── src/
│   
├── notebook/
│
└── README.md
```

## 📈 Model Evaluation

The models were evaluated using:

* **F1 Score**
* **Precision**
* **Recall**

These metrics were chosen over accuracy because the wine quality datasets contain **imbalanced classes**, making accuracy alone an unreliable measure of performance.

## ⚠️ Challenges Faced

* Significant class imbalance in both datasets.
* Some rare quality classes contained very few samples, making them difficult for the model to learn and predict.
* Hyperparameter tuning was experimented with, but the baseline models provided better and more stable results.

## ▶️ Running the Project

Clone the repository and run:

```bash
python main.py
```

## 📚 Dataset

This project uses the **Wine Quality Dataset** from the **UCI Machine Learning Repository**, containing physicochemical properties of Portuguese red and white wines.