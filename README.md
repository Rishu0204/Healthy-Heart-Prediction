# ❤️ Heart Failure Prediction Web App

An intelligent and interactive web application for predicting heart failure risk using patient medical data. Powered by a Random Forest Classifier, the app helps visualize input features, make predictions, and understand historical data — all in a clean and responsive interface.

---

## 🚀 Features

### 🩺 Input-Based Prediction
Users can input patient health parameters such as:
- Age
- Anaemia status
- Diabetes
- Ejection Fraction
- High Blood Pressure
- Platelet Count
- Serum Creatinine
- Serum Sodium
- Sex
- Smoking Habit
- Time (Follow-up Period)

Based on these inputs, the trained model predicts the likelihood of a heart failure event.

### 📄 Data Viewer (`data.html`)
- Displays uploaded dataset in a clean, paginated format (10-20 rows per page)
- CSV Download button to export the dataset
- Manual navigation: Previous / Next page buttons

### 🔙 Navigation
- Manual navigation bar for returning to Home or Data View pages
- Consistent layout and responsive design

---
### Sample Dataset

| age | anaemia | creatinine_phosphokinase  | diabetes | ejection_fraction | high_blood_pressure | platelets | serum_creatinine | serum_sodium | sex | smoking | DEATH_EVENT |
|-----|---------|---------------------------|----------|-------------------|---------------------|-----------|------------------|------------- |-----|---------|-------------|
| 75  | 0       | 582                       | 0        | 20                | 1                   | 265000.0  | 1.9              | 130          | 1   | 0       | 1           |
| 55  | 0       | 7861                      | 0        | 38                | 0                   | 263358.03 | 1.1              | 136          | 1   | 0       | 1           |
| 65  | 1       | 146                       | 0        | 20                | 0                   | 162000.0  | 1.3              | 129          | 1   | 1       | 1           |
| 50  | 1       | 1110                      | 1        | 38                | 0                   | 210000.0  | 1.9              | 137          | 1   | 0       | 1           |


> Note: Boolean fields are represented as 0 (No) and 1 (Yes).

---

## 🧠 Model Training (Random Forest Classifier)

The machine learning backend is based on a **Random Forest Classifier**, trained using a cleaned dataset of heart failure patient records. The model uses multiple health parameters as features and predicts a binary outcome (event/no event).

Steps involved:
1. Load and preprocess the dataset.
2. Handle missing values and normalize formats if needed.
3. Split the dataset into training and testing sets.
4. Train a `RandomForestClassifier` from `sklearn.ensemble`.
5. Save the trained model using `pickle` or `joblib` for Flask integration.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (manual styling)
- **Backend**: Python, Flask
- **ML Model**: RandomForestClassifier (scikit-learn)
- **Data Handling**: pandas
- **Deployment**: Localhost or can be deployed to Streamlit/Vercel with minor changes

---

## 🏁 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/Rishu0204/heart-failure-predictor.git
   cd heart-failure-predictor
2. Install all required requirements in a virtual environment (numpy,pandas,scikit-learn,Flask)
    ```bash
    python -m venv myenv
3. Run the App using:
    ```bash
    python app.py
4. Open in browser

---

## 📂 File Structure
```
.
├── venv
├── model_training
├── app.py
├── model.pkl
├── templates/
│   ├── index.html
│   ├── data.html
│   └── index1.html
├── README.md
└── heart_failure_clinical_records_dataset.csv


