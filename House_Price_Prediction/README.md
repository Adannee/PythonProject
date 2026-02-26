# House Price Prediction

Predicting residential sale prices using the Ames Housing Dataset. The project covers the full ML pipeline: missing value handling, feature engineering, one-hot encoding, model training, and a comparison of three modelling approaches — with a key finding about what "feature importance" actually means in Linear Regression.

---

## Results

| Model | R² Score | MAE |
|-------|----------|-----|
| Linear Regression (all 280 features) | 0.85 | $16,412 |
| Linear Regression (top 50 features by coefficient) | 0.61 | — |
| **Ridge Regression (all 280 features)** | **0.89** | — |

**Ridge Regression achieved R² = 0.89**, explaining 89% of variance in sale price. This result also revealed why naive feature selection on Linear Regression backfires — and why regularisation is the right solution.

---

## Dataset

- **Source:** Ames Housing Dataset (Kaggle)
- **Size:** 2,930 properties, 82 original features
- **Target:** `SalePrice` (continuous, USD)
- **Train/test split:** 80/20 → 2,344 training, 586 test samples

---

## Pipeline

### 1. Missing Value Analysis

27 columns contained missing values. Notable cases:

| Feature | Missing | Reason |
|---------|---------|--------|
| Pool QC | 2,917 / 2,930 | Most houses have no pool |
| Misc Feature | 2,824 | Most houses have no misc feature |
| Alley | 2,732 | Most houses have no alley access |
| Lot Frontage | 490 | Genuine missing data |

**Strategy:** Numeric nulls → median imputation. Categorical nulls → `"Unknown"`. `Alley` dropped (99.3% missing — essentially no signal). No duplicate rows found.

### 2. Correlation Analysis (Top Features)

Before any modelling, Pearson correlation with `SalePrice` identified the strongest numeric predictors:

| Feature | Correlation with SalePrice |
|---------|---------------------------|
| Overall Qual | 0.799 |
| Gr Liv Area | 0.707 |
| Garage Cars | 0.648 |
| Garage Area | 0.640 |
| Total Bsmt SF | 0.632 |
| 1st Flr SF | 0.622 |
| Year Built | 0.558 |

Overall quality rating and above-ground living area are by far the strongest individual predictors.

### 3. Feature Engineering

Two new features created from existing columns:

- **`Total SF`** = `Total Bsmt SF` + `1st Flr SF` + `2nd Flr SF` — combined square footage across all floors
- **`House Age`** = `Yr Sold` − `Year Built` — age of property at time of sale
- **`Is Remodeled`** — binary flag: 1 if the house was remodelled after original construction

### 4. Encoding

`pd.get_dummies(drop_first=True)` applied to all categorical columns, expanding the feature space from 82 to **280 features**.

---

## Model Comparison

### Linear Regression — Full Model (R² = 0.85, MAE = $16,412)

Strong baseline. Predictions are within $16,412 of the actual sale price on average.

### Linear Regression — Top 50 Features (R² = 0.61)

**This model performed worse, not better.** The "top 50 features" were selected by raw coefficient magnitude — but Linear Regression coefficients reflect scale, not true importance. The highest coefficients belonged to rare roof material dummy variables (e.g. `Roof Matl_Membran`, `Roof Matl_Metal`) with inflated coefficients caused by multicollinearity, not genuine predictive power. Dropping the other 230 features removed real signal.

> This is a classic mistake: confusing coefficient magnitude with feature importance in unregularised regression.

### Ridge Regression (R² = 0.89)

Ridge adds an L2 penalty that shrinks large, unstable coefficients — solving the exact problem identified above. Rather than discarding features, Ridge keeps all 280 while preventing any single coefficient from dominating. Result: R² improved from 0.85 to **0.89** without changing the feature set.

---

## Key Finding

The project originally attempted feature selection based on Linear Regression coefficients, which *reduced* R² from 0.85 to 0.61. Investigating why led directly to Ridge Regression — which recovered and improved performance. The failure of naive feature selection was more instructive than if it had worked.

---

## Tech Stack

| Tool | Use |
|------|-----|
| `pandas` | Data loading, preprocessing, feature engineering |
| `numpy` | Numerical operations |
| `seaborn` / `matplotlib` | Correlation heatmap, visualisations |
| `scikit-learn` | Train/test split, Linear Regression, Ridge, metrics |

---

## File Structure

```
House_Price_Prediction/
│
├── housing_price_predicition.ipynb   # Main notebook
├── AmesHousing.csv.xls               # Dataset
├── House Price Prediction Report.pdf # Written report
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy scikit-learn matplotlib seaborn

jupyter notebook housing_price_predicition.ipynb
```

---

## What I Learned

**Coefficient magnitude ≠ feature importance.** In multicollinear data, Linear Regression distributes weight arbitrarily across correlated features, producing large, unstable coefficients. Selecting features by this criterion throws away good predictors and amplifies noise.

**Regularisation is often better than feature selection.** Ridge Regression achieved the best result without removing a single feature. When the problem is multicollinearity, L2 regularisation addresses the root cause; feature selection based on flawed importance estimates just moves the problem around.

**The pipeline order matters.** Imputing with median before one-hot encoding avoids leaking test set statistics. This project uses a simple global median, but a production-ready version would fit the imputer on training data only and transform test data separately.

---

## Next Steps

- [ ] Fit imputer on training data only (prevent data leakage in preprocessing)
- [ ] Try Lasso (L1) — performs automatic feature selection via zero coefficients
- [ ] Try Gradient Boosting (XGBoost / LightGBM) — likely to outperform linear models on this dataset
- [ ] Use SHAP values for interpretable feature importance (correct approach vs. raw coefficients)
- [ ] Log-transform `SalePrice` — right-skewed targets often improve linear model performance
- [ ] Cross-validation (5-fold) for more robust R² estimate
