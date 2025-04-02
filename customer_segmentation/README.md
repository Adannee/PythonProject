#  Customer Segmentation using K-Means Clustering

##  Project Overview  
This project applies **K-Means Clustering** to segment customers based on their shopping behavior. The dataset contains features such as **age, gender, quantity purchased, price, payment method, and shopping mall**. The goal is to identify distinct customer groups for better marketing strategies.

##  Dataset Information  
- **Columns:**
  - `Customer Id`: Identification number of customer
  - `Age`: Age of the customer.
  - `Gender`: Male/Female.
  - `Quantity`: Number of items purchased.
  - `Price`: Total purchase amount.
  - `Category`: Category of items being purchased
  - `Payment Method`: How the customer paid (Card, Cash, etc.).
  - `Shopping Mall`: Mall where the purchase was made.

##  Methodology  
1. **Data Preprocessing**
   - Handle missing values and data inconsistencies.
   - Convert categorical variables using **One-Hot Encoding**.
   - Standardize numerical features.

2. **Exploratory Data Analysis (EDA)**
   - Visualize distributions of **age, quantity, and price**.
   - Identify spending patterns by **gender and mall**.

3. **Feature Engineering**
   - Created new features like **total spending**.
   - Applied **Principal Component Analysis (PCA)** for dimensionality reduction.

4. **K-Means Clustering**
   - Determined optimal **K value** using **Elbow Method & Silhouette Score**.
   - Clustered customers into **3-5 segments**.
   - Analyzed cluster characteristics.

5. **Visualization**
   - Scatter plots of customer segments.
   - Distribution of key attributes within clusters.

##  Key Insights  
✔ **Customer Segments Identified:** `[e.g., High Spenders, Budget Shoppers, Frequent Shoppers]`  
✔ **Spending Trends:** `[e.g., Younger shoppers spend less but visit frequently.]`  
✔ **Mall-Specific Preferences:** `[e.g., Mall A attracts high spenders, while Mall B has more budget-conscious buyers.]`  
