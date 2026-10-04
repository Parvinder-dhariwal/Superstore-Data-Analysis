import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("data/Superstore_Clean.xlsx")

# ==============================
# BUSINESS KPI
# ==============================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_products = df["Product ID"].nunique()

profit_margin = total_profit / total_sales
average_order_value = total_sales / total_orders
average_order_profit = total_profit / total_orders

print("\n ========  BUSINESS KPI ========")

print(f"Total Sales       : ${total_sales:,.2f}")
print(f"Total Profit      : ${total_profit:,.2f}")
print(f"Profit Margin     : {profit_margin:.2%}")
print(f"Total Orders      : {total_orders:,}")
print(f"Customers         : {total_customers:,}")
print(f"Products          : {total_products:,}")
print(f"Total Quantity    : {total_quantity:,}")
print(f"Average Order Value   : ${average_order_value:,.2f}")
print(f"Average Order Profit  : ${average_order_profit:,.2f}")

# ==============================
# YEARLY PERFORMANCE
# ==============================

yearly = df.groupby("Year").agg(
    Sales = ("Sales", "sum"),
    Profit = ("Profit", "sum"),
    Orders = ("Order ID", "nunique")
).reset_index()

yearly["Profit Margin"] = yearly["Profit"] / yearly["Sales"]

print("\n ======== YEARLY PERFORMANCE  ========")

print(yearly.to_string(index= False))

# ==============================
# CATEGORY PERFORMANCE
# ==============================

category = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

category["Profit Margin"] = category["Profit"] / category["Sales"]

print("\n========== CATEGORY PERFORMANCE ==========")
print(category.sort_values("Sales", ascending=False).to_string(index=False))


# ==============================
# REGION PERFORMANCE
# ==============================

region = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

region["Profit Margin"] = region["Profit"] / region["Sales"]

print("\n========== REGION PERFORMANCE ==========")
print(region.sort_values("Sales", ascending=False).to_string(index=False))

# ==============================
# DISCOUNT
# ==============================

total_discount = df["Discount"].nunique()

discount = df.groupby("Discount").agg(
    Sales = ("Sales", "sum"),
    Profit = ("Profit", "sum"),
    Quantity = ("Quantity", "sum"),
    Order = ("Order ID","nunique")
).reset_index()

discount["Profit Margin"] = discount["Profit"] / discount["Sales"]

print("\n========== DISCOUNT ==========")
print(discount.sort_values("Discount",ascending=True).to_string(index=False))

# ==============================
# SUB-CATEGORY PROFITABILITY
# ==============================

sub_category = df.groupby("Sub-Category").agg(
    Sales = ("Sales", "sum"),
    Profit = ("Profit", "sum"),
    Quantity = ("Quantity", "sum"),
    Order = ("Order ID","nunique")
).reset_index()

sub_category["Profit Margin"] = sub_category["Profit"] / sub_category["Sales"]

print("\n========== SUB-CATEGORY PROFITABILITY ==========")
print(sub_category.sort_values("Profit",ascending=False).to_string(index=False))

# ==============================
# PRODUCT WISE PROFITABILITY / LOSS
# ==============================

product_name = df.groupby("Product Name").agg(
    Sales = ("Sales", "sum"),
    Profit = ("Profit", "sum"),
    Quantity = ("Quantity", "sum"),
    Order = ("Order ID","nunique"),
    Discount = ("Discount", "mean")
).reset_index()

product_name["Profit Margin"] = product_name["Profit"] / product_name["Sales"]

print("\n========== PRODUCT NAME PROFITABILITY / LOSS ==========")
print(product_name.sort_values("Profit",ascending=True).head(10).to_string(index=False))

# ==============================
# LOSS-MAKING PRODUCTS WITH HIGH DISCOUNTS
# ==============================

loss_products = product_name.loc[(product_name["Profit"] < 0) & (product_name["Discount"] >= 0.30)]

print("\n========== LOSS-MAKING PRODUCTS WITH HIGH DISCOUNTS ==========")
print(loss_products.sort_values("Profit",ascending=True).head(10).to_string(index=False))

# ==============================
# CATEGORY + DISCOUNT ANALYSIS
# ==============================

category_discount = df.groupby(["Category", "Discount"]).agg(
    Sales = ("Sales", "sum"),
    Profit = ("Profit", "sum"),
    Quantity = ("Quantity", "sum"),
    Order = ("Order ID","nunique")
).reset_index()

category_discount["Profit Margin"] = category_discount["Profit"] / category_discount["Sales"]

print("\n========== CATEGORY + DISCOUNT ANALYSIS ==========")
print(category_discount.sort_values("Profit",ascending=False).to_string(index=False))

# ==============================
#  LOSS-MAKING CATEGORY + DISCOUNT ANALYSIS
# ==============================

category_discount_loss = category_discount.loc[category_discount["Profit"] < 0]
print("\n========== LOSS-MAKING CATEGORY + DISCOUNT ANALYSIS ==========")
print(category_discount_loss.sort_values("Profit",ascending=False).to_string(index=False))

# ==============================
#  REGION &  CATEGORY ANALYSIS
# ==============================

region_category = df.groupby(["Region","Category"]).agg(
    Sales = ("Sales", "sum"),
    Profit = ("Profit", "sum"),
    Quantity = ("Quantity", "sum"),
    Order = ("Order ID","nunique")
).reset_index()

region_category["Profit Margin"] = region_category["Profit"] / region_category["Sales"]
print("\n========== REGION & CATEGORY ANALYSIS ==========")
print(region_category.sort_values("Profit",ascending=False).to_string(index=False))

# ==============================
#  CUSTOMER ANALYSIS
# ==============================

customer_analysis = df.groupby("Customer ID").agg(
    Sales = ("Sales", "sum"),
    Profit = ("Profit", "sum"),
    Quantity = ("Quantity", "sum"),
    Order = ("Order ID","nunique")
).reset_index()

customer_analysis["Profit Margin"] = customer_analysis["Profit"] / customer_analysis["Sales"]
print("\n========== CUSTOMER ANALYSIS ==========")
print(customer_analysis.sort_values("Profit",ascending=False).head(10).to_string(index=False))

loss_customers = customer_analysis.loc[customer_analysis["Profit"] < 0]
print("\n========== LOSS MAKING CUSTOMERS ==========")
print(loss_customers.sort_values("Profit", ascending=True).head(10).to_string(index=False))

# ==============================
#  VISUALIZATION
# ==============================

# =========YEARLY SALES CHART================
plt.plot(
    yearly["Year"],
    yearly["Sales"]
)
plt.title("Sales Trend by Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()

# ========= CATEGORY SALES vs PROFIT VISUALIZATION===============

x = np.arange(len(category["Category"]))
width = 0.35
plt.bar(x - width/2, category["Sales"],width, label = "Sales")
plt.bar(x + width/2, category["Profit"],width, label = "Profit")

plt.xticks(x, category["Category"])
plt.title("Sales vs Profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.legend()
plt.show()

# ========= DISCOUNT vs PROFIT VISUALIZATION===============
plt.plot(discount["Discount"],discount["Profit"], marker="o")

plt.title("Discount Level vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

# ========= TOP PRODUCTS VISUALIZATION===============
top_products = product_name.sort_values("Profit",ascending=False).head(10)

plt.barh(top_products["Product Name"], top_products["Profit"])

plt.title("Top 10 Products by Profit")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.show()

# ========= BOTTOM PRODUCTS VISUALIZATION===============
bottom_products = product_name.sort_values("Profit",ascending=True).head(10)

plt.barh(bottom_products["Product Name"], bottom_products["Profit"])

plt.title("Bottom 10 Products by Profit")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.show()
