# Menu of Cafe
menu = {
    "Pizza": 120,
    "Pasta": 100,
    "Burger": 70,
    "Coffee": 60,
    "Sandwich": 50,
}

print("Welcome to HASHTAG Cafe!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0
order_details = {}

while True:
    item = input("Enter the item you want to order (or type 'done' to finish): ").strip().title()
    
    if item.lower() == "done":
        break

    if item in menu:
        quantity = int(input(f"How many {item}s would you like? "))
        order_total += menu[item] * quantity
        order_details[item] = order_details.get(item, 0) + quantity
        print(f"{quantity} {item}(s) added to your order.")
    else:
        print(f"Sorry, {item} is not available!")

# Apply discount if applicable
discount = 0
if order_total > 300:
    discount = order_total * 0.10  # 10% discount
    print("You got a 10% discount!")

final_total = order_total - discount

# Display the bill
print("\n===== YOUR BILL =====")
for item, qty in order_details.items():
    print(f"{item} x {qty} = Rs{menu[item] * qty}")
print(f"Subtotal: Rs{order_total}")
if discount:
    print(f"Discount: -Rs{discount}")
print(f"Total to Pay: Rs{final_total}")

# Payment option
payment_method = input("Would you like to pay with Cash or Card? ").strip()
if payment_method == "card":
    print("Processing  Card payment... Payment successful!")
else:
    print("Please pay cash at the counter.")

print("Thank you for visiting HASHTAG Cafe!")

