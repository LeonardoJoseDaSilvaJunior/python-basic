def vogais (texto):
    count = 0
    for x in texto:
        if x in "AaEeIiOoUu":
            count +=1
    print(count)

vogais("O rato roeu a roupa do rei de roma")