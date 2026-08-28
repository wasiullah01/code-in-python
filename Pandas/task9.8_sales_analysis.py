#Real-World Sales Analysis!
import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', 
             '2024-01-06', '2024-01-07', '2024-01-08'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone', 'Tablet', 'Laptop', 'Phone'],
    'Quantity': [2, 5, 1, 3, 4, 2, 3, 6],
    'Price': [50000, 15000, 50000, 25000, 15000, 25000, 50000, 15000],
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Lahore']
}

df = pd.DataFrame(data)

print("SALES ANALYSIS REPORT\n","="*20)
df['Total'] = df['Quantity'] * df['Price']

#group by products
group_by_product = df.groupby('Product')['Total'].sum()
print(group_by_product,"\n")

#group by cities
group_by_city = df.groupby('City')['Total'].sum()
print(group_by_city, "\n")

#Best sellig Products
best_selling_product = group_by_product.idxmax()
print(f"Best Selling Product: {best_selling_product} \n")

#highest revenue City
highest_revenue_city = group_by_city.idxmax()
print(f"Highest Revenue: {highest_revenue_city} \n")


#lowest revenue City
lowest_revenue_city = group_by_city.idxmin()
print(f"Lowest Revenue: {lowest_revenue_city} \n")


print(f"Total Revenue {df['Total'].sum()} \n")
print(f"Average Scale {df['Total'].mean()} \n")
print(f"Highest Scale {df['Total'].max()} \n")
print(f"Lowest Scale {df['Total'].min()} \n")

df.to_csv("Analysis.csv")
print("Analysis.csv (Saved) \n")

report = f"""
Sales Analysis
==============

Group by Product: {group_by_product} \n
Group by City: {group_by_city} \n

Best Selling Product: {best_selling_product} \n
Highest Revenue: {highest_revenue_city} \n
Lowest Revenue: {lowest_revenue_city} \n

Total Revenue: {df['Total'].sum()} \n
Average Scale: {df['Total'].mean()} \n
Highest Scale: {df['Total'].max()} \n
Lowest Scale:  {df['Total'].min()} \n
"""

with open("Sales Analysis.txt", "w") as file:
    file.write(report)


print("Report saved: Sales Analysis.txt")