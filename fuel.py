while True:
    try:
        # Ask the user to input a fraction
        get_input = input("Fraction: ")
        # Split the fraction into two parts
        x, y = get_input.split("/")
        # Convert the two parts into integers
        x = int(x)
        y = int(y)
        # Divide the two parts
        outcome = x / y
        # Multiply the outcome by 100 and round it
        outcome = round(outcome * 100)
        # If outcome is greater than 99%, print "F"
        if outcome > 99:
            print("F")
            break
        # If outcome is less than 1% print "E"
        elif outcome < 1:
            print("E")
            break
        # Print the outcome to the screen
        else:
            print(f"{outcome}%")
            break
            # Error checking
    # If the user enters a non-integer value, create a ValueError
    # If the users enters a division error, present ZeroDvisionError
    except (ValueError, ZeroDivisionError):
        pass




