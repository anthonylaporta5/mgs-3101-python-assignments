# Assignment 1 - Sales Analysis

# Store required values
shop_name = "Maven Roasters"
number_of_drinks = 100
price_per_drink = 3.50
number_of_pastries = 50
price_per_pastry = 2.50

# Calculate revenue
drink_revenue = number_of_drinks * price_per_drink
pastry_revenue = number_of_pastries * price_per_pastry
total_revenue = drink_revenue + pastry_revenue

# Display revenue
print("Shop:", shop_name)
print("Drink revenue: $", drink_revenue)
print("Pastry revenue: $", pastry_revenue)
print("Total revenue: $", total_revenue)
# Calculate drink and pastry revenue
drink_revenue = number_of_drinks * price_per_drink
pastry_revenue = number_of_pastries * price_per_pastry
total_revenue = drink_revenue + pastry_revenue

# Display revenue
print("Drink revenue: $", drink_revenue)
print("Pastry revenue: $", pastry_revenue)
print("Total revenue: $", total_revenue)
# Print the written sales analysis
with open("sales_analysis.txt", "r") as file:
    print(file.read())
