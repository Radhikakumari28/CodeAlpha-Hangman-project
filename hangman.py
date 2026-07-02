import random

words = ["python", "computer", "developer", "programming", "internship"]

while True:
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("\n===== HANGMAN GAME =====")

    while attempts > 0:
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed Letters:", " ".join(guessed_letters))
        print("Remaining Attempts:", attempts)

        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    if attempts == 0:
        print("\nGame Over!")
        print("The correct word was:", word)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break