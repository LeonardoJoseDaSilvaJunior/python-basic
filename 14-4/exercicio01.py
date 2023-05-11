password = "123"
chance = 3
while chance != 0:
    confirmation = input("insert your password: ")
    if confirmation == password:
        print("your password is correct! ")
        break
    else: chance -= 1
else: print("Your password is bloccked")
