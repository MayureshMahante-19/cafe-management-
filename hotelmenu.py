# This is a simple Cafe Management System in Python 
# where a customer can order items from a menu, and the program calculates the total bill.

# I used a dictionary because it is fast and efficient for storing items
# menu of cafe 
menu = {
    "Pizza" : 120,
    "Pasta" : 100,
    "Burger" :70,
    "Coffee" : 60,
    "Sandwich" : 50,
}

#greet
print("Welcome to HASTAG Cafe")
print ("Pizza : Rs120\nPasta: Rs100\nBurger :Rs70\nCoffee :Rs60\nSandwich :Rs50" )


order_total = 0

item1 = input("Enter the name of item you want to order = ") 
if item1 in menu :
    order_total += menu [item1]
    print(f"Your item {item1} has been added in your order")

else:
    print(f"Ordered item {item1} is not available yet!")

another_item = input("Do you want to add another item? (Yes/No) : ")
if another_item == "Yes":
    item2 = input("Enter the name of second item = ")
    if item2 in menu :
        order_total += menu[item2]
        print(f"Item {item2} has been added in your order")
    else :
        print(f"Ordered item {item2} is not available!")    


    print(f"The total amount of items to pay is {order_total}")



