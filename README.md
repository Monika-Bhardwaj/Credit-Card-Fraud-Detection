# 💳 Credit Card Fraud Detection Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/Monika-Bhardwaj/Credit-Card-Fraud-Detection?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Monika-Bhardwaj/Credit-Card-Fraud-Detection?style=for-the-badge)

📊 A real-time interactive dashboard to **analyze and visualize credit card transactions** and detect fraudulent activity.

🔗 **Live App:** [Click here to try it out](https://credit-card-fraud-detection-fzzahlxj77u9vajkwwdvez.streamlit.app/)  

---

## 🚀 Features

✅ **Interactive Dashboard** built with [Streamlit](https://streamlit.io)  

✅ **Filter transactions** by:
- ⏱️ Time Range  
- 🔍 Transaction Type (All / Legitimate / Fraudulent)  

✅ **Key Metrics**
- 📌 Total Transactions  
- ⚠️ Fraudulent Transactions  
- 📈 Fraud Rate (%)  

✅ **Visualizations**
- 📉 Transactions Over Time (with fraud overlay)  
- 💰 Transaction Amount Distribution (Legit vs Fraud)  

✅ **Data Export**
- 📥 Download filtered transactions as CSV  

✅ **Expandable Data Table**
- 🔎 Explore full filtered dataset inside the app  

---

## 📸 Dashboard Preview
 
![Dashboard Preview](c:\Users\ASUS\AppData\Local\Packages\MicrosoftWindows.Client.Core_cw5n1h2txyewy\TempState\ScreenClip\{D75004E7-F319-48A7-AE85-A10E97E0BCE6}.png)

---

## 📂 Project Structure

credit_card_fraud_dashboard/
├── data/ # Dataset (loaded from public URL in deployment)
├── dashboard/
│ └── dashboard.py # Streamlit dashboard app
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## ⚙️ Installation (Run Locally)

Clone the repository:
git clone https://github.com/Monika-Bhardwaj/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run dashboard/dashboard.py

---

🌐 Deployment

This project is deployed on Streamlit Cloud.
To deploy your own version:

Push your code to a GitHub repository.

Go to [Streamlit Cloud](https://streamlit.io/cloud).

Connect your GitHub repo and select dashboard/dashboard.py as the entry file.

Done ✅

---

📊 Dataset

The dataset comes from Kaggle - [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

For deployment, the app loads the CSV directly from a public TensorFlow storage link:
https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv

---

🔮 Future Enhancements

Add ML model integration to predict fraud probability in real-time

More interactive charts using Plotly

Export results to Excel

A report-style notebook for analysis

---

👩‍💻 Author

Monika Bhardwaj
🎯 Aspiring Data Analyst | Passionate about AI/ML & Data Visualization

🔗 [LinkedIn](https://www.linkedin.com/in/monika-bhardwaj-50b752286/) | [GitHub](https://github.com/Monika-Bhardwaj)