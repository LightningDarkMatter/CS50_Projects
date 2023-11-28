# List of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Start loop
while True:
    # Get user input
    date = input("Date: ").rstrip()
    try:
        # Split input by /
        month, day, year = date.split("/")

        # Check month is 1-12 and day is 1-31
        if (int(month) >=1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break

    except:
        try:
            # Split input by space
            w_month, w_day, year = date.split(" ")

            # find number value of month
            for i in range(len(months)):
                if w_month == months[i]:
                    month = i + 1

            # Remove comma
            try:
                if "," in w_day:
                    day = w_day.replace(",","")
            except:
                print()
                pass

            # Check month is 1-12 and day is 1-31
            if (int(month) >=1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            # Next line
            print()
            pass
# If month less than 10 add zero
# If day less than 10 add zero
# Print answer
print(f"{year}-{int(month):02}-{int(day):02}")

