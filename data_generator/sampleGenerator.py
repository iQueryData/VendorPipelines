import pandas as pd
import random
from datetime import datetime, timedelta

# Sample data
names = [
    "Margherita", "Pepperoni", "Spinach & Feta", "BBQ Chicken", "Hawaiian", 
    "Meat Lovers", "Veggie Deluxe", "Pesto Veggie", "Shrimp Pizza", "Caprese"
]

ingredients = [
    "Tomato, Mozzarella, Basil", "Pepperoni, Cheese", "Spinach, Feta", 
    "BBQ Chicken, Cheese", "Ham, Pineapple", "Sausage, Pepperoni, Cheese", 
    "Peppers, Onions, Mushrooms", "Goat Cheese, Arugula", "Shrimp, Garlic, Mozzarella", 
    "Tomato, Basil, Mozzarella"
]

cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]
city_codes = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
populations = [8419600, 3980400, 2716000, 2328000, 1686000, 
               1584200, 1547000, 1426000, 1340000, 1035000]

sales_data = []

# Generate 20,000 sales records
for i in range(1, 20001):
    pizza_id = i
    order_id = 20000 + i
    pizza_name_id = 500 + (i % 10)  # Example for simplicity
    quantity = random.randint(1, 5)
    order_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
    order_time = (datetime.now() + timedelta(minutes=random.randint(0, 1439))).strftime('%I:%M %p')
    unit_price = round(random.uniform(10, 30), 2)
    total_price = round(quantity * unit_price, 2)
    pizza_size = random.choice(["Small", "Medium", "Large"])
    pizza_category = random.choice(["Vegetarian", "Meat", "Gourmet", "Seafood"])
    ingredients_choice = random.choice(ingredients)
    pizza_name = random.choice(names)
    city_index = random.randint(0, 9)

    sales_data.append([
        pizza_id, order_id, pizza_name_id, quantity, order_date,
        order_time, unit_price, total_price, pizza_size, pizza_category,
        ingredients_choice, pizza_name, cities[city_index], city_codes[city_index],
        populations[city_index], round(populations[city_index] * random.uniform(0.8, 1.2), 0),
        round(random.uniform(40, 70), 1), round(random.uniform(-90, 90), 4)
    ])

# Create DataFrame
df = pd.DataFrame(sales_data, columns=[
    "pizza_id", "order_id", "pizza_name_id", "quantity", "order_date",
    "order_time", "unit_price", "total_price", "pizza_size",
    "pizza_category", "pizza_ingredients", "pizza_name", "city",
    "city_code", "population", "estimated", "percent", "latitude"
])

# Save to CSV
df.to_csv('pizza_sales_data_20000_samples.csv', index=False)
print("Generated 20,000 pizza sales records and saved to 'pizza_sales_data_20000_samples.csv'.")
