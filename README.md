# 💊 Medical Expense Prediction System

## 📌 Project Overview

This project is a machine learning-based web application that predicts an individual's **annual medical insurance cost** based on personal and health-related attributes such as age, BMI, smoking habits, and region.

The model is trained on real-world insurance data and deployed as an interactive web application using Flask.

---

## 🚀 Features

* Predicts **annual and monthly medical expenses**
* Handles both **numerical and categorical inputs**
* Uses **machine learning pipeline (ColumnTransformer + Random Forest)**
* Clean and responsive **web interface using Flask & Bootstrap**
* Real-time predictions via browser

---

## 🧠 Machine Learning Details

* **Algorithm Used:** Random Forest Regressor
* **Preprocessing:**

  * StandardScaler (for numerical features)
  * OneHotEncoder (for categorical features)
* **Pipeline:** Ensures consistent preprocessing during training and prediction
* **Evaluation Metrics:** R² Score, RMSE

---

## 📊 Input Features

* Age
* Sex
* BMI
* Number of Children
* Smoking Status
* Region

---

## 📈 Output

* Predicted **Yearly Medical Expense (INR)**
* Estimated **Monthly Cost**

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* Bootstrap

---

## 🌐 Live Demo

👉 (Add your Render link here after deployment)

---

## ⚙️ How to Run Locally

```bash
git clone <your-repo-link>
cd medical-expense-predictor
pip install -r requirements.txt
python app/app.py
```

Then open:
http://127.0.0.1:5000/

---

## 📂 Project Structure

```
medical-expense-predictor/
│
├── app/
│   ├── app.py
│   └── templates/
│
├── model/
│   └── model.pkl
│
├── src/
│   └── train.py
│
├── data/
│   └── insurance.csv
│
├── requirements.txt
└── README.md
```

---

## 🎯 Key Highlights

* End-to-end ML project (data → model → deployment)
* Industry-standard pipeline implementation
* User-friendly web interface
* Deployment-ready application

---

## 📌 Future Improvements

* Add risk classification (Low / Medium / High)
* Improve model accuracy with advanced algorithms
* Deploy with custom domain
* Add data visualization dashboard

---

## 👨‍💻 Author

Developed by SwardaNaik31

---
