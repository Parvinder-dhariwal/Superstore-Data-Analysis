# Retail Business Intelligence

## Project Overview

This project analyzes retail sales data to understand business performance, profitability, customer behavior, product performance, and shipping trends.

The analysis is performed using Python, Pandas, NumPy, and data visualization libraries. The project follows a practical data analytics workflow including data cleaning, exploratory data analysis (EDA), KPI analysis, profitability analysis, and business insight generation.

The goal of this project is to identify important business trends and provide data-driven insights that can help improve sales and profitability.

## Business Problem

Retail businesses generate large amounts of sales and transaction data, but raw data alone does not provide clear business insights.

This project aims to analyze the retail dataset to answer important business questions such as:

- Which categories and sub-categories generate the most sales and profit?
- Which products are causing losses?
- How does discounting affect profitability?
- Which customer segments contribute the most to business performance?
- How does shipping time vary across orders?
- Which areas or regions perform better in terms of sales and profit?
- What factors may be contributing to low or negative profitability?

## Project Objectives

The main objectives of this project are:

- Clean and prepare the retail dataset for analysis.
- Perform exploratory data analysis (EDA) using Python.
- Calculate important business KPIs such as Sales, Profit, Orders, Customers, and Profit Margin.
- Analyze sales and profitability across categories and sub-categories.
- Identify loss-making products and areas of low profitability.
- Analyze the relationship between discounts and profit.
- Analyze customer segments and regional performance.
- Examine shipping performance and delivery time.
- Generate actionable business insights from the data.

## Tools & Technologies

- **Python** — Data analysis and data processing
- **Pandas** — Data cleaning, transformation, and analysis
- **NumPy** — Numerical operations and calculations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical data visualization
- **Excel** — Initial data preparation and dataset handling
- **VS Code** — Python development environment
- **Git & GitHub** — Version control and project management

## Dataset

The project uses the Superstore retail dataset containing **9,994 rows and 24 columns**.

The dataset contains information about:

- Orders and order dates
- Customers and customer segments
- Products, categories, and sub-categories
- Sales, quantity, discounts, and profit
- Shipping details
- Geographic information

Additional calculated columns were created during data preparation:

- **Year**
- **Shipping Days**
- **Profit Margin**

## Project Structure

```text
Retail-Business-Intelligence/
│
├── Data/
│   └── Superstore_Clean.xlsx
│
├── Python/
│   ├── 01_data_audit.py
│   └── 02_eda.py
│
├── Powerbi/
├── Screenshot/
├── Sql/
└── README.md