def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number_in_plate = 0

    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:2].isalpha == False:
        return False

    for char in s:
        if number_in_plate >1 and char.isalpha():
            return False

        if char.isdigit():
            number_in_plate += 1

        if char in ".,!?":
            return False

        if number_in_plate == 1 and char == "0":
            return False

    return True

main()
