user = []
password_list = []

for x in range(0, 2):
    user.append(input("insert your user name: "))
    password_list.append(input("insert your password: "))

for x in range(0,2):
    name = input("LOGIN - Insert you name: ")
    password = input("LOGIN - Insert your password")

    if user[x] == name and password_list[x] == password:
        print("login done")
        break;
    else:
        print("unexist")
