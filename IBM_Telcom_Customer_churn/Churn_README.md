# Customer Churn Analysis — NovaSub Telecom

> **The business question:** Monthly revenue is flat despite growing signups. Is churn the problem, and where should retention spend go?

---

## Key Findings (TL;DR)

- **26.5% of customers churn** — more than 1 in 4, well above the healthy industry benchmark of 5–7%
- **$7.75M in lifetime value** has already been lost to churned customers
- **47.7% of customers churn within their first 12 months** — this is an onboarding problem, not a broad retention problem
- **The #1 churn reason is attitude of support staff (192 customers)** — not price, not competitors
- **Fiber optic customers churn at 41.9%** — the premium product has a product-market fit problem
- **Deploying the churn model generates an estimated $1.52M net annual value** at a 1,310% ROI

---

## Revenue Impact

| Metric | Value |
|--------|-------|
| Churned customers | 1,869 |
| Average monthly charge (churned) | $74.44 |
| Monthly revenue lost | $139,131 |
| **Annualised revenue lost** | **$1,669,570** |
| Average CLTV per churned customer | $4,149 |
| **Total lifetime value lost** | **$7,755,256** |

---

## Dataset

- **Source:** IBM Telco Customer Churn Dataset (Kaggle)
- **Size:** 7,043 customers, 33 features
- **Target:** `Churn Value` (0 = Retained, 1 = Churned)
- **Key features:** Tenure, contract type, internet service, monthly charges, CLTV, churn reason

---

## Analysis Pipeline

### 1. Data Cleaning
- Fixed `Total Charges` column mistyped as string — contained 11 blank entries for new customers (0 months tenure), filled with 0
- No duplicate rows found
- Dropped geographic identifiers and `Churn Score` (pre-calculated, would leak into model)
- Saved `Churn Reason` separately for EDA — not used in modelling

### 2. Exploratory Data Analysis

**Churn by contract type — the strongest single signal:**

| Contract | Churn Rate | Monthly Revenue Lost |
|----------|------------|---------------------|
| Month-to-month | ~42% | ~$120,000 |
| One year | ~11% | ~$14,000 |
| Two year | ~3% | ~$5,000 |

**High-risk customer profiles identified:**

| Segment | Churn Rate | vs. Average |
|---------|------------|-------------|
| Month-to-month contract | ~42% | +15.5pp |
| Fiber optic internet | 41.9% | +15.4pp |
| Senior citizens | 41.7% | +15.2pp |
| DSL internet | 19.0% | -7.5pp |
| Two-year contract | ~3% | -23.5pp |

**The early churn problem:**

| Tenure | Churn Rate | Retention |
|--------|------------|-----------|
| 0–12 months | **47.7%** | 52.3% 🔴 |
| 13–24 months | 28.7% | 71.3% 🟠 |
| 25–36 months | 21.6% | 78.4% 🟠 |
| 37–48 months | 19.0% | 81.0% 🟢 |
| 49–60 months | 14.4% | 85.6% 🟢 |
| 61–72 months | 6.6% | 93.4% 🟢 |

If a customer survives 36 months, they are likely a customer for life. The problem is concentrated entirely in the first year — this is an onboarding and activation failure, not a broad retention problem.

**Why customers actually leave:**

| Category | Customers | % of Churners | Business Response |
|----------|-----------|---------------|-------------------|
| Service quality (support attitude) | 327 | 17.5% | CS training — low cost, high impact |
| Competitor product (speed, data) | 481 | 25.7% | Product roadmap review |
| Competitor offer | 140 | 7.5% | Targeted retention offers |
| Network reliability | 103 | 5.5% | Infrastructure investment |
| **Price too high** | **98** | **5.2%** | **Last resort only** |

> Price is the least common reason for leaving. A blanket discount programme would address 5% of churners while burning margin on customers leaving for other reasons entirely.

### 3. Feature Engineering

| Feature | Description | Rationale |
|---------|-------------|-----------|
| Encoded binary cols | Yes/No → 0/1 | Required for modelling |
| One-hot encoded categoricals | Contract, internet service, payment method etc. | Captures categorical signal |

Final feature space: 31 features after encoding.

### 4. Modelling

Three models trained on an 80/20 stratified split (26.5% churn rate preserved in both sets):

| Model | AUC-ROC | Precision | Recall | F1 |
|-------|---------|-----------|--------|----|
| **Logistic Regression** | **0.849** | **0.643** | **0.572** | **0.605** |
| Random Forest | 0.838 | 0.642 | 0.513 | 0.571 |
| XGBoost | 0.836 | 0.610 | 0.532 | 0.569 |

**Logistic Regression outperformed both tree-based models.** Churn in this dataset is driven by a small number of strong linear signals — contract type, tenure, and internet service type. XGBoost's additional complexity adds noise rather than signal here. Logistic Regression is also preferred for interpretability: coefficients can be presented directly to business stakeholders as odds ratios.

### 5. Threshold Optimisation

Default threshold of 0.5 is too conservative for churn — missing a real churner costs full CLTV ($4,149), while a false alarm costs only a retention offer ($50). These costs are asymmetric.

| Threshold | Churners Caught | Churners Missed | False Alarms |
|-----------|----------------|-----------------|--------------|
| Default (0.50) | 214 | 160 | 119 |
| **Optimised (0.37)** | **266** | **108** | **199** |

Lowering the threshold from 0.5 to 0.37 catches 52 additional churners at the cost of 80 additional false alarms — justified given the CLTV asymmetry.

### 6. Churn Risk Segmentation

| Segment | Customers | Actual Churn Rate | Avg CLTV |
|---------|-----------|-------------------|----------|
| High Risk | 115 | 77.0% | $3,954 |
| Medium Risk | 318 | 51.0% | $3,990 |
| Low Risk | 976 | 13.0% | $4,565 |

The model successfully concentrates real churners into the High Risk bucket — 77% of customers flagged as high risk actually churn, validating the model's discriminative power.

---

## Business Recommendation

### Intervention Strategy by Segment

| Segment | Action | Rationale |
|---------|--------|-----------|
| 🔴 High Risk (115) | Immediate personal CS call | 77% will churn — high confidence, high stakes |
| 🟠 Medium Risk (318) | Automated offer + follow-up email | 51% churn rate justifies spend |
| 🟢 Low Risk (976) | Monitor only — no spend | 13% churn rate, intervention cost not justified |

### ROI of Deploying the Model

| Scenario | Annual Cost | CLTV Recovered | Net Value | ROI |
|----------|-------------|----------------|-----------|-----|
| Status quo | $0 | $0 | $0 | — |
| Default threshold (0.5) | $999,000 | $1,327,811 | **$1,244,561** | 1,495% |
| **Optimised threshold (0.37)** | $1,395,000 | $1,639,017 | **$1,522,767** | **1,310%** |

*Assumptions: $50 per intervention, 30% retention success rate, $4,149 avg CLTV*

### The single highest-ROI action:
Fix the onboarding experience for **month-to-month fiber optic customers in months 0–12**. This segment combines the three highest churn risk factors and accounts for the majority of early-life revenue loss. Reducing first-year churn from 47.7% to the 13–24 month rate of 28.7% would recover an estimated **$2.05M in lifetime value**.

---

## Tech Stack

| Tool | Use |
|------|-----|
| `pandas`, `numpy` | Data cleaning, feature engineering |
| `matplotlib`, `seaborn` | Visualisations |
| `scikit-learn` | Modelling, evaluation, threshold analysis |
| `xgboost` | Gradient boosted model comparison |
| `shap` | Feature importance and model explainability |

---

## File Structure

```
churn-analysis/
│
├── churn_analysis.ipynb          # Full analysis notebook
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset
├── churn_by_contract.png         # Contract churn visualisation
├── churn_reasons.png             # Top 10 churn reasons
├── demographics_internet.png     # Senior/internet churn rates
├── tenure_retention.png          # Retention curve by tenure
├── model_comparison.png          # ROC curves + confusion matrix
├── precision_recall.png          # Threshold trade-off curve
├── risk_segmentation.png         # Customer risk segments
├── shap_importance.png           # Feature importance (SHAP)
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap

jupyter notebook churn_analysis.ipynb
```

---

## What I Learned

**The metric you choose encodes a business decision.** Optimising for accuracy on an imbalanced churn dataset is meaningless — a model that predicts "retained" for everyone is 73.5% accurate and catches zero churners. Precision, recall, and the threshold you set reflect what failure costs the business. Getting this wrong in production means either burning retention budget on loyal customers or letting real churners walk out undetected.

**Simpler models can win — and the reason why matters.** Logistic Regression outperformed Random Forest and XGBoost here. The reason is that churn is driven by a few strong, near-linear signals: contract type, tenure, and internet service type. XGBoost's ability to model complex interactions provides no benefit when the underlying relationships are simple. Knowing *why* a simpler model wins is more valuable than blindly reaching for the most complex one.

**EDA findings and model outputs should tell the same story.** The three highest-risk factors identified in EDA — month-to-month contracts, fiber optic service, and short tenure — are also the top SHAP features driving the model's predictions. When these align, it validates both the analysis and the model. When they don't, it's a signal something is wrong.

**Price is rarely the real problem.** The instinct when customers leave is to offer discounts. The data shows price ranks 10th out of 10 churn reasons. The real drivers are service quality and product gaps versus competitors. Discounting would be expensive, largely ineffective, and would train customers to expect price concessions.

---

## Limitations & Next Steps

- [ ] Retention success rate (30%) is assumed — A/B test retention interventions to measure actual rate
- [ ] CLTV is provided in the dataset — a production version would calculate this dynamically from transaction data
- [ ] Model retraining cadence needed — churn drivers shift over time, model should be retrained quarterly
- [ ] Exit survey for the 154 "Don't know" churners — this is free qualitative signal being left uncollected
- [ ] Segment the fiber optic churn investigation further — are these customers in specific geographies or age groups?
- [ ] Build a real-time scoring pipeline — batch predictions are a start, event-triggered scoring (e.g. after a support call) would be more actionable
