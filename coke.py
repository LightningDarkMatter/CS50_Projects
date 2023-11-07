amount_due = 50

while amount_due >= 0:

    print ("Amount Due:", amount_due)
    money = int(input ("Insert Coin:"))

    if money == 25 or money == 10 or money == 5:

        amount_due = amount_due - money

    if amount_due <= 0:
        print ("Change Owed:", (amount_due*-1))
        break
