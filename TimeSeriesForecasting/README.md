#  Tesla Stock Price Forecasting

This project uses two powerful time series forecasting models—**ARIMA** and **LSTM**—to predict Tesla stock prices based on historical data.

---

##  Dataset

- **Source**: Yahoo Finance  
- **Ticker**: `TSLA` (Tesla Inc.)  
- **Features Used**: Date, Open, High, Low, Close, Volume  
- **Size**: ~150MB (compressed for GitHub)

---

##  Objectives

- Clean and prepare stock price data
- Test for stationarity using Augmented Dickey-Fuller (ADF) test
- Build and evaluate forecasting models using:
  - 🔹 ARIMA (AutoRegressive Integrated Moving Average)
  - 🔹 LSTM (Long Short-Term Memory Neural Network)
- Visualize predictions vs actual stock prices

---

##  Models Used

### 🔷 ARIMA
- Used for classical time series forecasting
- Differencing to make the series stationary
- Selected parameters via ACF/PACF and AIC
- Evaluated with ADF statistic and p-value

### 🔷 LSTM
- Deep learning model using `TensorFlow` / `Keras`
- Scaled prices with `MinMaxScaler`
- Trained on sequences of past 60 days to predict the next day
- Saved model: `lstm_stock_model.h5`

---

## 🧪 Evaluation Metrics

- 📉 Mean Squared Error (MSE)
- 📉 Mean Absolute Error (MAE)
