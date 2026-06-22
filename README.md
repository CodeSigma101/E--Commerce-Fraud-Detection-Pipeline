# End-to-End E-Commerce Fraud Detection Pipeline and Analytics Dashboard
#### App Link;https://e--commerce-fraud-detection-pipeline-md85njeqpuce9zmbznafhn.streamlit.app/

An enterprise-grade data science framework engineered to identify, analyze, and mitigate fraudulent transactions in e-commerce purchase streams. This repository covers the complete lifecycle: from handling extreme class imbalance to deploying an interactive web application for real-time risk assessment.

---

## Project Overview and Business Value

In e-commerce analytics, fraud is a classic "needle in a haystack" problem. Standard machine learning models trained on raw transaction data fail because they default to predicting the majority class (legitimate transactions) to achieve high accuracy, leaving the business exposed to critical chargeback losses.

This project solves this bottleneck by building a robust data processing pipeline that targets Recall Optimization (the percentage of actual fraud caught) while monitoring Precision to maintain a seamless user checkout experience.

---
---

## Technical Implementation Details

### 1. Advanced Data Preprocessing and Leakage Prevention
* **Target Mapping**: Fraud target vectorization maps OrderStatus == 'Cancelled' as the positive classification label (1). 
* **Feature Engineering**: Standardized transaction vectors are enriched by decomposing datetime strings into individual temporal indices (Year, Month, Day).
* **Noise Mitigation**: Dropped unique identifiers (OrderID, CustomerID, TrackingNumber) to prevent model overfitting on high-cardinality noise.
* **Resampling Rigor**: SMOTE is systematically isolated and applied only to the training split following a stratified partition, strictly protecting the validation data from synthetic leakages.

### 2. Machine Learning Classifiers
The pipeline trains and benchmark-evaluates two structurally distinct algorithmic approaches:
* **Logistic Regression**: Serves as a fast, highly interpretable linear baseline.
* **Random Forest Classifier**: Utilizes an ensemble of uncorrelated decision trees to capture non-linear transaction interactions and complex behavioral fraud variations.
### 3. Comprehensive Evaluation Matrix
We bypass basic accuracy entirely, grading models on performance metrics suited for severe operational class imbalances:
* **Recall (Sensitivity)**: Ensures the model catches the maximum volume of bad actors.
* **Precision**: Measures the rate of true positive alerts vs. frustrating false alarms.
* **ROC-AUC Score**: Computes the classifier's spatial capability to separate legitimate entries from malicious fraud risks.

---

## Live Monitoring Web Dashboard

The deployment layer leverages Streamlit and Plotly to convert production matrices into an analytical frontend for risk managers.

### Key Visual Assets and Functionality:
* **Live Operational Metrics**: Tracks total volume processed ($), aggregate transaction logs, and real-time fraud rate metrics dynamically.
* **Vulnerability Analysis**: Grouped bar charts map financial exposure concentrations across product lines to isolate targeted inventory categories.
* **Interactive Control Filters**: Dropdown selection bars allow immediate, isolated analysis of specific product sectors.

---
## Installation and Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Environment Configuration
Install all pipeline and application framework dependencies using pip:
```bash
pip install -r requirements.txt
```

### 3. Launch the Local Dashboard Instance
Execute the interface wrapper layer straight through your Python interpreter path:
```bash
python -m streamlit run app.py

---
---

## Technology Stack
* **Language Framework**: Python
* **Data Processing and ML Tools**: Pandas, NumPy, Scikit-Learn, Imbalanced-Learn (SMOTE)
* **Frontend Design**: Streamlit, Plotly, Seaborn, Matplotlib
