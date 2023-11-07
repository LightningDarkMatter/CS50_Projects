def main():

    camel_case = input("camelCase: ")
    print("snake_case: ", end="")
    snake_case(camel_case)

def snake_case(letters):
    for i in letters:
        if i.isupper():
            print ("_"+i.lower(), end="")
        else:
            print(i, end="")
    print()

main()