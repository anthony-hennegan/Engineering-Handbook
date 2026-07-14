store_name = "Anthony's General Store"
products = [
    {
        "name": "nails",
        "price": 0.89,
        "in_stock": True
    },
    {
        "name": "hammer",
        "price": 3.99,
        "in_stock": False
    },
    {
        "name": "wood",
        "price": 5.50,
        "in_stock": True
    }
]

def format_name(name):
    return name.strip().title()

def is_available(item):
    return item['in_stock']

def display_available_products(item_list):
    print("Inventory List")
    print("------------------")
    for item in item_list:
        if is_available(item):
            print(f"{item['name']}: ${item['price']}")
            
def count_available_products(product_list):
    available_product_count = 0
    
    for product in product_list:
        if is_available(product):
            available_product_count += 1
            
    return available_product_count

print(f"Welcome to {store_name}")
print("")

user_name_response = input("What is your name? ")
user_name = format_name(user_name_response)
print(f"Hello {user_name}")
print("")

view_products_response = input("Would you like to view our inventory? ")
view_products_response = view_products_response.strip().lower()

if view_products_response == "yes" or view_products_response == "y":
    display_available_products(products)
    print("")
    print(f"We have {count_available_products(products)} products available.")
elif view_products_response == "no" or view_products_response == "n":
    print("No worries. Have a nice day.")
else:
    print("Please type yes or no.")