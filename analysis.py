import pandas as pd

df = pd.read_csv("data/textile_sales_production.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("TEXTILE COMPANY DATA ANALYTICS")
print("=" * 40)
print(f"Total Revenue: ₹{df['Revenue_INR'].sum():,.0f}")
print(f"Total Profit: ₹{df['Profit_INR'].sum():,.0f}")
print(f"Units Sold: {df['Units_Sold'].sum():,}")
print(f"Average Profit Margin: {df['Profit_Margin_Pct'].mean():.2f}%")
print(f"Average Defect Rate: {df['Defect_Rate_Pct'].mean():.2f}%")
print(f"Average Satisfaction: {df['Customer_Satisfaction'].mean():.2f}/5")

print("\nRevenue by Product")
print(df.groupby("Product")["Revenue_INR"].sum().sort_values(ascending=False))

print("\nRevenue by Region")
print(df.groupby("Region")["Revenue_INR"].sum().sort_values(ascending=False))

print("\nFactory Quality")
print(df.groupby("Factory")[["Defect_Rate_Pct","Waste_Pct","Lead_Time_Days"]].mean().round(2))
