products = {'pen': 7, 'notebook': 15, 'ruler': 10, 
            'crayons': 35, 'paper': 25, 'bag': 350, 'pencil': 9}

while True:
    product = input("Enter product: ").lower()
    if product in products:
        price = products[product]
        print(f"The price of {product} is {price}.")
    else:
        print("Product not found. Please enter a product from the list.")
