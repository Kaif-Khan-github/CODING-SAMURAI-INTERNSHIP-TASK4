📊 Stock Price Prediction Model Summary
=======================================

📅 Data Source:
- Stock Data pulled from Yahoo Finance using `yfinance`
- Duration: 2010-01-01 to 2022-04-30
- User provides the stock ticker (e.g., TCS.NS, INFY.NS)

📈 Features Used for Prediction:
- Open Price
- High Price
- Low Price
- Volume

🎯 Target:
- Close Price (to be predicted)

🔧 Models Trained:
1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. SVR (Support Vector Regression) with GridSearchCV for best params

🧪 Train-Test Split:
- 80% Training | 20% Testing
- X shape (features): (2482, 4)
- y shape (target): (2482, 1)
- Test Set Size: (621 samples)

📐 Model Evaluation Metrics:

--- Linear Regression ---
- Mean Squared Error: 0.0113
- RMSE: 0.1064
- R² Score: 0.9996

--- Lasso Regression ---
- Mean Squared Error: 0.0632
- RMSE: 0.2514
- R² Score: 0.9978

--- Ridge Regression ---
- Mean Squared Error: 0.0111
- RMSE: 0.1056
- R² Score: 0.9996

📊 Visualizations:
- Line chart of historical Close prices
- Distribution plots for Open, High, Close prices using Seaborn

🧠 Final Model Used for Prediction:
- Linear Regression Model (best balance of performance and simplicity)

📥 Custom Input Prediction:
The model accepts user input for:
- Opening Price
- High Price
- Low Price
- Volume

Even if user skips input, default values are used:
(Open=100, High=120, Low=95, Volume=3000)

✅ Example Run:
Opening Price: 120
High Price: 200
Low Price: 150
Volume: 2500

📈 Predicted Closing Price: ₹169.84

