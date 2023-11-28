# Create a grocery list
grocery_list = {}

#Begin loop
while True:
    try:
        # Prompt the user for items
        item = input()
        # Check if item is in list
        if item in grocery_list:
            # If it is, add 1 to the value
            grocery_list[item] +=1
        else:
            grocery_list[item] = 1
    except EOFError:
        # Sort the items alphabetically
        for key in sorted(grocery_list.keys()):
            
            # Print the grocery list
            print(f"{grocery_list[key]} {key.upper()}")
        break
