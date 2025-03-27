# Customer Data Cleaning Project

## Overview
This project focuses on **cleaning and preprocessing raw data** to improve its quality and usability. We applied **Pandas and NumPy** functions to handle missing values, duplicates, and formatting issues.

## Dataset
- **Name:** Customer Sales Data
- **Issues Found:**
  - Missing values in key columns.
  - Inconsistent date formats.
  - Duplicate records.
  - Irregular capitalization in text fields.

## Cleaning Steps
1. **Handling Missing Data:** Used `.fillna()`, `.dropna()`, and `.replace()` functions.
2. **Fixing Duplicates:** Removed duplicate records.
3. **Standardizing Formats:** Converted dates to a common format (`YYYY-MM-DD`).
4. **Normalizing Text Data:** Corrected case inconsistencies in categorical fields.
5. **Outlier Detection:** Identified and removed outliers affecting sales trends.
