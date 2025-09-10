# 💳 Credit Card Fraud Detection   

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

> 📊 An **interactive dashboard** to explore and analyze credit card transactions, detect fraud patterns, and visualize trends.  
> Built with **Streamlit**, **Pandas**, and **Matplotlib**.  

---

## 📂 Project Structure
credit_card_fraud_detection/
├── data/
│ └── creditcard.csv # Dataset (not included, download from Kaggle)
├── dashboard/
│ └── dashboard.py # Main Streamlit app
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 🚀 Features  

✅ **Filtering & Exploration**  
- Filter by **time range**  
- Select **transaction type**: All, Legitimate, Fraudulent  

✅ **Metrics at a Glance**  
- 🟦 Total Transactions  
- 🟥 Fraud Transactions  
- 🟨 Fraud Rate (%)  

✅ **Visualizations**  
- 📈 Transactions Over Time (line chart)  
- 💰 Transaction Amount Distribution (histogram)  

✅ **Data Interaction**  
- Preview random **sample transactions**  
- Expand to view **full filtered dataset**  

✅ **Export Options**  
- Download filtered transactions as **CSV**  

---

## 🧠 Machine Learning Demo (Extension)  

> As an optional extension, we train a **Logistic Regression model** to classify transactions as fraud or legitimate.  

### Model Highlights  
- **Train/Test Split** (80/20)  
- **Logistic Regression Classifier**  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score  
- **Confusion Matrix Heatmap**  

This demo shows how machine learning can be integrated into fraud detection.  

---

## ⚙️ Installation  

Clone the repository:  
```bash
git clone https://github.com/yourusername/credit_card_fraud_dashboard.git
cd credit_card_fraud_dashboard

Install dependencies:
pip install -r requirements.txt

▶️ Usage

Run the dashboard locally:
streamlit run dashboard/dashboard.py

Then open the link shown in the terminal (default: http://localhost:8501) in your browser.

📦 Requirements
Listed in requirements.txt:

streamlit
pandas
matplotlib
seaborn
scikit-learn   # (for ML demo)

📊 Dataset
This project uses the Credit Card Fraud Detection dataset available on Kaggle:
👉 Credit Card Fraud Detection Dataset

📖 Future Enhancements
✨ Bar chart of frauds per time bin
✨ Filters by transaction amount
✨ Export to Excel (.xlsx) instead of CSV
✨ Interactive plots with Plotly
✨ Full report-style Colab Notebook

🙌 Acknowledgments
Dataset: Kaggle - Credit Card Fraud Detection

Streamlit → for building interactive dashboards

Matplotlib & Seaborn → for visualizations

Scikit-learn → for ML demo




