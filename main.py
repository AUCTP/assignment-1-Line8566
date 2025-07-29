import random

# Some example items - feel free tho change them
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]


### 1. Initialize Inventory ###
# Create three separate lists to store product information:
items = ["Sandwich", "Salad", "Cake"]
  # List of product names.
prices = [65, 45, 50]
  # List of product prices.
inventories = [10, 10, 10]
  # List of product inventories.


### 2. Simulate Customer Arrivals ###
numStudents = 50

def simulate_customers(numStudents, inventory, items):
    sales = []  
    # list to store successful sales (item names)
        #number of students arriving in the university
    for i in range(numStudents):
        if random.choice([True, False]):
            # True if students buys an item and False if not
            #print("Student buys an item")
            item = random.choice(items)  
                # Randomly selects an item
            itemIndex = items.index(item)  
                # get index to match inventory list
            if inventory[itemIndex] > 0:
                #checks if there is inventory of the item
                inventory[itemIndex] -= 1 
                    #reduce the inventory of the item
                sales.append(item)  
                    # saves the sale
                print(f"Student buys a {item}")
            else:
                print(f"{item} is out of stock")
        else:
            print("Student does not buy anything")
    return sales

sales = simulate_customers(numStudents, inventories, items)
print("Sales:", sales)
print(inventories)


### 3. Process Sales ###
def process_sales(sales, prices):
    totRevenue = 0
    item = random.choice(items)
    itemIndex = items.index(item)
    for item in sales:
        totRevenue += prices[itemIndex]
    return totRevenue

Revenue = process_sales(sales, prices)
print("Total revenue is:", Revenue)

### 4. Generate Sales Report ###
def generate_report():
    print ("Today the following items were sold:", sales)
    print ("Which resultet in a total revenue of:", Revenue)
    print ("Thereby the remaining inventory is:", inventories)
generate_report()
