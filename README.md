# ✈️ Airlines Flight Price Prediction in India

## 👋 Introduction

Hi, my name is **Muhammad Erico Ricardo**.
In this project, I analyzed the **Airlines Flight in India Dataset** from Kaggle:
🔗 [Airlines Flights Data](https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data)

The goal of this analysis is to **predict airline ticket prices** using regression models. After evaluating multiple models, I found that tree-based and boosting models provide the best performance due to the **non-linear and complex relationship** between flight features and ticket prices.

You can try the deployment of my model here:
🚀 [HuggingFace Space – Indian Airplane Price Prediction](https://huggingface.co/spaces/EricoR/Indian_Airplane_Price_Prediction)

---

## 📊 Model Performance Ranking

1. **XGBoost** – Best-performing model, most accurate predictions.
2. **Decision Tree Regressor** – Second-best performance.
3. **LightGBM** & **Gradient Boosting Regressor** – Solid results, better than linear models.
4. **Linear Regression** & **Ridge Regression** – Worst performance, not suitable for this dataset.

✅ The results confirm that **simple linear models are not sufficient**, while boosting-based approaches excel in capturing the complexity of ticket pricing.

---

## ⚙️ Tuned XGBoost Model

### 🔧 Best Parameters

* `subsample: 0.8`
* `reg_lambda: 5`
* `reg_alpha: 1`
* `n_estimators: 300`
* `max_depth: 7`
* `learning_rate: 0.1`
* `colsample_bytree: 0.8`

### 📈 Model Metrics

* **Negative Mean Squared Error (neg MSE):** `-10,948,750` (improved from \~ -12,300,000)
* **R² Score:** `0.9787` → The model explains **97.9% of ticket price variance**

This makes the **tuned XGBoost model a highly reliable predictor** for flight ticket prices.

---

## 🛫 Flight Analysis Insights

### ✈️ Flight Volume & Popular Routes

* **Vistara** → Airline with the highest number of flights.
* **Air India** & **Indigo** → Follow closely behind.
* **Delhi** & **Mumbai** → Main flight hubs.
* **Bangalore** → Another highly connected city.
* Morning flights → Most frequent departures.

### 💰 Factors Influencing Ticket Prices

* **Airline Type**

  * *Low-Cost Carriers* (AirAsia, Indigo, GO\_FIRST) → Affordable & stable prices.
  * *Full-Service Carriers* (Vistara, Air India) → Higher & more varied prices.
* **Departure & Arrival Times** → Strong impact on ticket cost.
* **Distance** → Longer routes cost more.
* **Booking Time** → Prices increase as departure date approaches.

---

## 🏆 Model Selection & Final Performance

After evaluating different regression models, **XGBoost** was chosen as the best due to its strong predictive power.

**Final Results:**

* ✅ **Mean R² Score:** `0.9787` (≈ 98% accuracy)
* ✅ **Mean Negative MSE:** `-10,948,750` (low prediction error)

This confirms that boosting models like **XGBoost** are the most effective for complex and non-linear datasets like flight ticket pricing.

---

## 🚀 Deployment

You can test the deployed model here:
👉 [Indian Airplane Price Prediction – HuggingFace Space](https://huggingface.co/spaces/EricoR/Indian_Airplane_Price_Prediction)

---

✨ **Conclusion:**
This project demonstrates the effectiveness of advanced regression models (especially **XGBoost**) in predicting airline ticket prices with very high accuracy. Beyond modeling, the analysis also highlights the key factors influencing pricing strategies in the Indian airline industry.
