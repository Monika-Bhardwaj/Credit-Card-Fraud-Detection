import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Credit Card Fraud Detection Dashboard", layout="wide")

# Load data with caching
@st.cache_data
def load_data():
    data_path = "data/creditcard.csv"
    df = pd.read_csv(data_path)
    df['TimeBin'] = (df['Time'] // 10000) * 10000  # bin by 10k seconds
    return df

df = load_data()

st.title("📊 Credit Card Fraud Detection Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filter Transactions")

# Time filter
min_time = int(df['Time'].min())
max_time = int(df['Time'].max())
time_range = st.sidebar.slider("Time Range (in seconds)", min_time, max_time, (min_time, max_time))

# Transaction type
trans_type = st.sidebar.radio("Transaction Type", ['All', 'Legitimate', 'Fraudulent'])

# Apply filters
filtered_df = df[(df['Time'] >= time_range[0]) & (df['Time'] <= time_range[1])]

if trans_type == 'Legitimate':
    filtered_df = filtered_df[filtered_df['Class'] == 0]
elif trans_type == 'Fraudulent':
    filtered_df = filtered_df[filtered_df['Class'] == 1]

# Metrics
total_trans = len(filtered_df)
fraud_trans = filtered_df['Class'].sum()
fraud_rate = (fraud_trans / total_trans * 100) if total_trans > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", total_trans)
col2.metric("Fraud Transactions", fraud_trans)
col3.metric("Fraud Rate (%)", f"{fraud_rate:.2f}%")

# Data Sample
st.subheader("📋 Transactions Data Sample")
st.dataframe(filtered_df.sample(min(10, total_trans)) if total_trans > 0 else pd.DataFrame())

# 📉 Plot: Transactions Over Time
st.subheader("📈 Transactions Over Time")

trans_over_time = filtered_df.groupby("TimeBin").size().reset_index(name="Total")
fraud_over_time = filtered_df[filtered_df['Class'] == 1].groupby("TimeBin").size().reset_index(name="Fraud")

fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(trans_over_time["TimeBin"], trans_over_time["Total"], label="Total Transactions", color="blue")
if not fraud_over_time.empty:
    ax1.plot(fraud_over_time["TimeBin"], fraud_over_time["Fraud"], label="Fraud Transactions", color="red")
ax1.set_xlabel("Time (binned in 10k seconds)")
ax1.set_ylabel("Number of Transactions")
ax1.set_title("Transactions Over Time")
ax1.grid(True)
ax1.legend()
st.pyplot(fig1)

# 📊 Plot: Amount Distribution
st.subheader("💰 Transaction Amount Distribution")

fig2, ax2 = plt.subplots(figsize=(10, 4))
filtered_df[filtered_df['Class'] == 0]['Amount'].plot(kind='hist', bins=50, alpha=0.6, label='Legitimate', ax=ax2)
filtered_df[filtered_df['Class'] == 1]['Amount'].plot(kind='hist', bins=50, alpha=0.6, label='Fraudulent', ax=ax2, color='red')
ax2.set_title("Transaction Amount Distribution")
ax2.set_xlabel("Amount ($)")
ax2.set_ylabel("Frequency")
ax2.legend()
st.pyplot(fig2)

# 📁 Download Button
st.subheader("📥 Download Filtered Data")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_transactions.csv',
    mime='text/csv'
)

# Optional: Show raw data
with st.expander("🔎 Show full filtered data table"):
    st.dataframe(filtered_df.reset_index(drop=True))
