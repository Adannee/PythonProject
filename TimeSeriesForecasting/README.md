# Tesla Stock Market Analysis

Exploratory analysis and trend forecasting of Tesla (TSLA) stock using 5 years of historical price data. The project applies technical indicators and a baseline regression model to understand price behaviour and trend direction.

---

## What This Project Does

| Step | Technique | Purpose |
|------|-----------|---------|
| Data collection | `yfinance` API | Pull OHLCV data, Jan 2020 – Dec 2024 |
| EDA | Summary stats + price chart | Understand price distribution and range |
| Technical indicators | 50-day SMA, 20-day EMA | Smooth noise, identify momentum |
| Volatility analysis | Bollinger Bands (20-day, ±2σ) | Flag overbought/oversold conditions |
| Trend forecasting | Linear Regression (date → close) | Establish a naive trend baseline |

---

## Dataset

- **Source:** Yahoo Finance via `yfinance`
- **Ticker:** TSLA (Tesla Inc.)
- **Period:** January 2, 2020 – December 30, 2024
- **Trading days:** 1,257
- **Features used:** Date, Open, High, Low, Close, Volume

| Statistic | Close Price |
|-----------|-------------|
| Mean | $213.28 |
| Std Dev | $83.32 |
| Min | $24.08 (Jan 2020) |
| Max | ~$479 (Nov 2021 peak) |
| 25th pct | $173.86 |
| 75th pct | ~$266 |

---

## Technical Indicators

### Moving Averages
- **50-day SMA** — identifies medium-term trend direction; lags price but filters short-term noise
- **20-day EMA** — reacts faster to price changes; useful for spotting momentum shifts earlier

### Bollinger Bands
Constructed around a 20-day rolling mean ± 2 standard deviations:
- **Upper band** — price approaching here signals potential overbought territory
- **Lower band** — price approaching here signals potential oversold territory
- **Width** — expanding bands indicate higher volatility; contracting bands suggest consolidation

TSLA is known for wide, volatile Bollinger Bands — periods like late 2020 and late 2021 showed extreme band expansion.

---

## Baseline Model: Linear Regression

A Linear Regression was fit using the trading day index as the sole feature — a naive trend line that captures the overall direction of price across the full 5-year period.

- **Train/test split:** 80% / 20% (1,005 / 252 samples)
- **Input feature:** Numerical date index (factorized)
- **Target:** Closing price

> **Note:** This is intentionally a baseline. A date-indexed regression cannot capture TSLA's volatility, regime changes, or non-linear patterns — but it establishes a trend floor useful for comparison with more sophisticated models.

---

## Key Observations

1. **Price range is extreme** — TSLA went from ~$28 in Jan 2020 to a ~$479 peak in Nov 2021, then corrected sharply to ~$110 in late 2022, before recovering above $400 by end of 2024. Linear trend models struggle significantly with this behaviour.

2. **Technical indicators reveal regime shifts** — The 50-day SMA and 20-day EMA crossed meaningfully in mid-2021 and again in mid-2022, aligning with major price inflection points.

3. **Bollinger Bands confirm volatility clustering** — Tesla has unusually wide bands compared to stable stocks, making mean-reversion strategies risky without additional confirmation signals.

4. **Linear regression captures trend, not volatility** — The baseline model fits the general upward slope but misses every peak and trough. This confirms the need for time-series-aware models for actual forecasting.

---

## Tech Stack

| Tool | Use |
|------|-----|
| `yfinance` | Data download |
| `pandas` | Data wrangling, rolling calculations |
| `numpy` | Numerical operations |
| `matplotlib` | All visualizations |
| `scikit-learn` | Linear Regression, train/test split |

---

## File Structure

```
TimeSeriesForecasting/
│
├── Tesla_Stock_Market_Analysis.ipynb   # Main notebook
├── tesla_stock.csv                     # Raw price data
├── lstm_stock_model.h5                 # Saved model (future extension)
└── README.md
```

---

## How to Run

```bash
pip install yfinance pandas numpy matplotlib scikit-learn

# Open the notebook
jupyter notebook Tesla_Stock_Market_Analysis.ipynb
```

Cells run top-to-bottom. Data is fetched live from Yahoo Finance — results may differ slightly if re-run on a later date.

---

## What I Learned

**Technical indicators are interpretation tools, not signals.** SMAs and Bollinger Bands describe what has happened — combining them meaningfully requires domain context. For a stock like Tesla, which is driven heavily by news cycles and sentiment, technical indicators alone are insufficient for prediction.

**Baseline models matter.** Building the linear regression first made it immediately obvious why more complex approaches are needed. It's easy to jump to LSTM and claim good results; it's harder to show *why* a simple model fails and what that reveals about the data's structure.

**Random splitting is wrong for time series.** The train/test split in this notebook uses `sklearn`'s default random shuffle, which leaks future data into training. A proper time-series split should use a cutoff date (e.g., train on 2020–2023, test on 2024). This is a known limitation of the current implementation.

---

## Next Steps

- [ ] Fix train/test split to use a chronological cutoff (no data leakage)
- [ ] Add proper evaluation metrics: MSE, MAE, RMSE on the test set
- [ ] Implement ARIMA with stationarity testing (ADF test) and parameter selection via ACF/PACF
- [ ] Build LSTM on 60-day lookback windows (framework already scaffolded with `lstm_stock_model.h5`)
- [ ] Add a confusion matrix / direction-accuracy metric (did the model predict up/down correctly?)
- [ ] Compare all models in a single results table
