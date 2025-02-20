import random
secret_words = ["jahe", "kopi", "gula", "merica", "bawang"]

wins = 0
losses = 0

def updateText(kata_ditebak, guess):
    display_text = " ".join(kata_ditebak)
    if guess in kata:
        feedback = f"Mantap!, '{guess}' is in the secret word!"
    else:
        feedback = f"Sorry bro, '{guess}' is not in the secret word."
    return display_text + "\n" + feedback

def play_game():
    global wins, losses
    kata = random.choice(secret_words)
    secret_words.remove(kata)
    kata_ditebak = ["_"] * len(kata)
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
            for i in range(len(kata)):
                if kata[i] == guess:
                    kata_ditebak[i] = guess
        else:
            print("Salah boyy.")
            attempts = attempts - 1
            print(f"Anda memiliki {attempts} kesempatan lagi.")

        print(updateText(kata_ditebak, guess))

    if "_" not in kata_ditebak:
        print("Gacor!!!")
        wins += 1
    else:
        print(f"Nice try boy, yang bener tuh: {kata}")
        losses += 1

    print(f"Score: Wins {wins}, Losses {losses}")

def main():
    while True:
        play_game()
        if not secret_words:
            print("No more words left! Game over.")
            break
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print(f"Final Score: Wins {wins}, Losses {losses}")
            break

if __name__ == "__main__":
    main()