# MGS 3101 - Assignment 1: Sales Analysis

# Required variables
shop_name = "Maven Roasters"
number_of_drinks = 100
price_per_drink = 3.50
number_of_pastries = 50
price_per_pastry = 2.50

# Calculate drink and pastry revenue
drink_revenue = number_of_drinks * price_per_drink
pastry_revenue = number_of_pastries * price_per_pastry
total_revenue = drink_revenue + pastry_revenue

# Display sales information
print("Shop Name:", shop_name)
print("Number of Drinks Sold:", number_of_drinks)
print("Price Per Drink: $", price_per_drink)
print("Number of Pastries Sold:", number_of_pastries)
print("Price Per Pastry: $", price_per_pastry)

print("\nDrink Revenue: $", drink_revenue)
print("Pastry Revenue: $", pastry_revenue)
print("Total Revenue: $", total_revenue)

# Print the written sales analysis
print("\n--- Written Sales Analysis ---")

with open("sales_analysis.txt", "r") as file:
    print(file.read())

# Check whether total revenue is at least $500
print("\n--- Revenue Check ---")

if total_revenue >= 500:
    print("Total revenue is at least $500.")
else:
    print("Total revenue is less than $500.")

# Data supporting recommendations
print("\n--- Recommendation Data ---")

# Recommendation 1: Focus on peak morning sales
peak_sales_hour = "10:00 AM"
print("Peak sales hour:", peak_sales_hour)
print("Recommendation: Schedule additional employees and prepare inventory")
print("before the morning sales period.")

# Recommendation 2: Focus on high-performing product categories
top_product_category = "Coffee"
coffee_revenue = 270000
print("Top product category:", top_product_category)
print("Approximate coffee category revenue: $", coffee_revenue)
print("Recommendation: Maintain strong inventory and promotions for")
print("high-performing coffee products.")

# Recommendation 3: Compare store locations
highest_revenue_location = "Hell's Kitchen"
print("Highest-revenue location identified in the analysis:",
      highest_revenue_location)
print("Recommendation: Compare practices at higher-performing locations")
print("with other locations to identify opportunities for improvement.")
