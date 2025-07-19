def calculate_total(price, quantity=1):
    total = price * quantity
    print(f"Total cost: Rs:{total}")

price_number = float(input("Enter the value of price of the items: "))
quantity_number =input("Enter the value of quantity of the items: ")

if quantity_number.strip() == "":
	calculate_total(price_number)
else:
	calculate_total(price_number  , int(quantity_number))
