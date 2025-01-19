kata = "jahe"
kata_ditebak = ["_"] * 4
while "_" in kata_ditebak:
    guess = input("hayo tebak: ")
    if guess in kata:
        print("Betul!")
        for i in range(4):
            if kata[i] == guess:
                kata_ditebak[i] = guess
    else:
        print("Salah boyy.")
    print(*kata_ditebak)

    if "_" not in kata_ditebak:
        print("Gacor!!!")