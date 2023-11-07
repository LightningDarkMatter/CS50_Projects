def main():
    x = input("What time is it? ")

    if 7<= convert(x) < 8:
        print("breakfast time")
    elif 12<= convert(x) <= 13:
        print("lunch time")
    elif 18<= convert(x) <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hour, minutes = time.split(":")
    hour = float(hour)
    minutes = float(minutes) / 60

    return hour + minutes


if __name__ == "__main__":
    main()