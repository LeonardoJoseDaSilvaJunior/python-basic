user = []
password = []

for x in range (0,5):
    user.append(input("insert your user name: "))
    password.append(input("insert your password: "))

for x in range (0,5):
    print(f"\nposition: {x}\nUser {user[x]}\nPassword  : {password[x]}")
