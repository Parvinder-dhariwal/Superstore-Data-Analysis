# Retail Business Intelligence

## Project Overview

This project analyzes retail sales data to understand business performance, profitability, customer behavior, product performance, and shipping trends.

The analysis uses Python and follows a practical data analytics workflow including data auditing, data preparation, exploratory data analysis (EDA), KPI analysis, and business insight generation.

## Business Problem

The project aims to answer key business questions such as:

- Which categories and sub-categories are most profitable?
- Which products are generating losses?
- How do discounts affect profitability?
- Which customer segments and regions perform better?
- How does shipping time vary across orders?

## Project Objectives

- Clean and prepare the retail dataset.
- Perform exploratory data analysis using Python.
- Calculate important business KPIs.
- Analyze sales and profitability across categories and sub-categories.
- Identify loss-making products.
- Analyze the impact of discounts on profit.
- Generate data-driven business insights.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Excel
- VS Code
- Git & GitHub

## Dataset

The cleaned Superstore dataset contains 9,994 rows and 24 columns.

The dataset includes information about:

- Orders and customers
- Products and categories
- Sales, quantity, discounts, and profit
- Shipping details
- Geographic information

Additional calculated columns include:

- Year
- Shipping Days
- Profit Margin

## Project Structure

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

## Python Analysis 

Python was used for data auditing, preparation, exploratory data analysis, KPI calculation, and profitability analysis.

## Key KPIs
Total Sales
Total Profit
Total Quantity
Total Orders
Total Customers
Total Products
Profit Margin
Average Order Value
Average Order Profit
Analysis Performed
Year-wise sales and profit analysis
Category-wise performance
Region-wise performance
Discount analysis
Sub-category profitability
Product-wise profitability
Loss-making product identification
High-discount loss analysis
Customer profitability analysis

## Power BI Dashboard
An interactive Power BI dashboard was created to visualize business performance and provide actionable insights.

## Dashboard Pages
1. Sales & Profit Analysis

Includes:

KPI cards
Year-wise Sales & Profit
Category-wise Sales & Profit
Profit by Sub-Category
Region-wise Sales & Profit
Year and Region filters

2. Customer & Product Analysis

Includes:

Top 10 Products by Profit
Bottom 10 Products by Profit
Sales by Customer Segment
Profit by Customer Segment
Year and Region filters

3. Discount & Return Analysis

Includes:

Discount vs Profit
Profit by Discount Level
Returned Orders
Return Rate
Year and Region filters

## Key Business Insights

Sales increased over the years, with 2018 showing the highest overall sales.
Technology was one of the strongest categories in terms of sales and profitability.
The Consumer segment contributed the highest sales and profit.
Copiers was one of the most profitable sub-categories.
Higher discount levels were generally associated with lower profitability.
Several highly discounted products generated negative profit.
The West region contributed the highest sales.
The overall return rate was approximately 3%, with 296 returned orders.