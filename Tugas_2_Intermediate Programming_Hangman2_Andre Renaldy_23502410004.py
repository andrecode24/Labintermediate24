kata = "jahe"
kata_ditebak = ["_"] * 4
attempts = 6
guessed_letters = []

while "_" in kata_ditebak and attempts > 0:
    while True:
        guess = input("hayo tebak: ").lower()
        if len(guess) == 1 and guess not in guessed_letters:
            guessed_letters.append(guess)
            break
        elif len(guess) != 1:
            print("Masukkan satu huruf saja!")
        else:
            print("Kamu sudah menebak huruf ini!")


    if guess in kata:
        print("Betul!")
        for i in range(4):
            if kata[i] == guess:
                kata_ditebak[i] = guess
    else:
        print("Salah boyy.")
        attempts = attempts - 1
        print(f"Anda memiliki {attempts} kesempatan lagi.")

    print(*kata_ditebak)

if "_" not in kata_ditebak:
    print("Gacor!!!")
else:
    print(f"nt boy, yang bener tuh:", {kata})
