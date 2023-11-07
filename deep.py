def main():
    name = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().replace(" ","")

    match name:
        case "42" | "fortytwo" | "forty-two":
            print ("yes")
        case _:
            print ("no")

main()