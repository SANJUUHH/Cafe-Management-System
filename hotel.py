#Hotel  services
#cafe management system


menu = { "PIZZA": 120,
        "BURGER": 80,
        "TEA": 10,
        "COFFEE": 20,
        "POHA": 40}

print("*******Welcome to Blitz Cafe********")
print()
 
print("MENU CARD:\nPIZZA: Rs.120\nBURGER: Rs.80\nTEA: Rs.10\nCOFFEE: Rs.20\nPOHA: Rs.40")
print()
print("Note: You can order 5 items at a time.\n")
def order():
    def customer_details():
        print("\n")
        name = input("What is your name? ").upper()
        phone_number = int(input("What is your phone number? "))
        print("\n")
        print(f"Hi {name},'{phone_number}'Your order is ready!\nPlease take it from the takeaway counter.\nEnjoy your Blitz cafe's meal.")
        print("\n")


    order_total = 0

    item1 = input("What would you like to order? ").upper()
    if item1 in menu:
        print(f"The {item1} is added.")
        order_total += menu[item1]
        print("\n")
    else:
        print(f"The {item1} is not available.")
        print("\n")

    item = input("Would you like to order more? (Yes/No) ").upper()
    if item == "YES":
        item2 = input("What would you like to order? ").upper()
        if item2 in menu:
            print(f"The {item2} is added.")
            order_total += menu[item2]
            print("\n")
        else:
            print(f"The {item2} is not available.")
            print("\n")
    else:
        
        print("Thank You for Ordering.")
        print(f"You have ordered {item1}.")
        print(f"Your order total is {order_total}.")
        customer_details()
        exit()

    item = input("Would you like to order more? (Yes/No) ").upper()
    if item == "YES":
        item3 = input("What would you like to order? ").upper()
        if item3 in menu:
            print(f"The {item3} is added.")
            order_total += menu[item3]
            print("\n")
        else:
            print(f"The {item3} is not available.")
            print("\n")
    else:
        print("Thank You for Ordering.")
        print(f"You have ordered {item1} and {item2}.")
        print(f"Your order total is {order_total}.")
        customer_details()
        exit()

    item = input("Would you like to order more? (Yes/No) ").upper()
    if item == "YES":
        item4 = input("What would you like to order? ").upper()
        if item4 in menu:
            print(f"The {item4} is added.")
            order_total += menu[item4]
            print("\n")
        else:
            print(f"The {item4} is not available.")
            print("\n")
    else:
        print("Thank You for Ordering.")
        print(f"You have ordered {item1}, {item2} and {item3}.")
        print(f"Your order total is {order_total}.")
        customer_details()
        exit()

    item = input("Would you like to order more? (Yes/No) ").upper()
    if item == "YES":
        item5 = input("What would you like to order? ").upper()
        if item5 in menu:
            print(f"The {item5} is added.")
            order_total += menu[item5]
            print("\n")
        else:
            print(f"The {item5} is not available.")
            print("\n")
    else:
        print("Thank You for Ordering.")
        print(f"You have ordered {item1}, {item2}, {item3} and {item4}.")
        print(f"Your order total is {order_total}.")
        print("\n")
        customer_details()
        exit()
    print(f"You have ordered {item1}, {item2}, {item3}, {item4} and {item5}.")
    customer_details()
    
order()


#Over and end
