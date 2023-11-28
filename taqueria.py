d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

# ask user to order item
order = input("Item: ").lower()


# check to see if item is in dictionary
while True:
    try:
        if order in d:
            total += d[order]
        
    except (ValueError, ZeroDivisionError):
        pass
    print("Price: ${:.2f}".format(d[order])) 
# if item is in dictionary, add price to total

# print total

# if not in dictionary, handle error