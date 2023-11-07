def main ():
    greeting = input("Greeting: ").lower().replace(" ","").replace("?","")

    if greeting == "hello":
        print("$0")
    elif greeting == "hello,newman":
        print("$0")
    elif greeting == "howyoudoing":
        print("$20")
    elif greeting == "what'shappening":
        print("$100")
    elif greeting == "what'sup":
        print("$100")

main()