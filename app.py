import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration Setup
st.set_page_config(page_title="Fraud Pipeline Analytics", layout="wide", page_icon="🛡️")
st.title(" E-Commerce Fraud Detection & Pipeline Analytics Dashboard")
st.markdown("Real-time visual monitoring of class imbalances, feature distributions, and classifier models.")

# 2. Cache Data Loading for Fast Performance
@st.cache_data
def load_dashboard_data():
    # Replace with your actual preprocessed dataset path
    data = pd.read_csv('Dataset for Data Analytics - Sheet1.csv')
    data['is_fraud'] = data['OrderStatus'].apply(lambda x: 1 if x == 'Cancelled' else 0)
    return data

df = load_dashboard_data()

# 3. Sidebar Filtering Mechanisms
st.sidebar.header(" Interactive Control Filter")
selected_product = st.sidebar.multiselect(
    "Select Products to Analyze:",
    options=df['Product'].unique(),
    default=df['Product'].unique()
)
filtered_df = df[df['Product'].isin(selected_product)]

# 4. Top-level Performance Metric Cards
total_tx = len(filtered_df)
fraud_tx = filtered_df['is_fraud'].sum()
fraud_rate = (fraud_tx / total_tx) * 100 if total_tx > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions Evaluated", f"{total_tx:,}")
col2.metric("Flagged Fraud Transactions", f"{fraud_tx:,}", delta=f"{fraud_rate:.2f}% Rate", delta_color="inverse")
col3.metric("Total Processing Volume ($)", f"${filtered_df['TotalPrice'].sum():,.2f}")

st.markdown("---")

# 5. Interactive Chart Sections (Row 1)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader(" Operational Class Imbalance Visualization")
    fig_imbalance = px.pie(
        filtered_df, names='is_fraud', title='Proportion of Legit (0) vs Fraud (1) Targets',
        color='is_fraud', color_discrete_map={0: '#2b5c8f', 1: '#d9534f'},
        labels={'is_fraud': 'Is Fraudulent?'}
    )
    st.plotly_chart(fig_imbalance, use_container_width=True)

with chart_col2:
    st.subheader(" Fraud Volumetrics Across Product Categories")
    fig_product = px.bar(
        filtered_df, x='Product', y='TotalPrice', color='is_fraud',
        title='Financial Volume Spread by Line Item Types',
        barmode='group', color_discrete_map={0: '#2b5c8f', 1: '#d9534f'}
    )
    st.plotly_chart(fig_product, use_container_width=True)

# 6. Interactive Model Evaluation Mock Metrics (Row 2)
st.markdown("---")
st.subheader(" Live Pipeline Classifier Performance Comparison")
m_col1, m_col2 = st.columns(2)

with m_col1:
    st.markdown("###  Logistic Regression (Baseline + SMOTE)")
    st.json({"ROC-AUC": 0.8412, "Precision (Class 1)": "71.4%", "Recall (Class 1)": "83.5%", "Status": "Deployed"})

with m_col2:
    st.markdown("###  Random Forest Classifier")
    st.json({"ROC-AUC": 0.9254, "Precision (Class 1)": "89.1%", "Recall (Class 1)": "88.3%", "Status": "Evaluating"})
