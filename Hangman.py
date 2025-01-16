word = "secret"
guessed_letters = ["_"] * 6
while "_" in guessed_letters:
    guess = input("Guess a letter: ")
    if guess in word:
        print("Correct!")
        for i in range(6):
            if word[i] == guess:
                guessed_letters[i] = guess
    else:
        print("Incorrect.")
    print(" ".join(guessed_letters))
    if "_" not in guessed_letters:
        print("You won!")