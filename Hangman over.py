import random

words = ["apple", "house", "tiger", "robot", "table"]
word = random.choice(words)

display = []
for letter in word:
    display.append("_")

lives = 6
guessed_letters = []

print("Welcome to Hangman Game!")

while lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Lives Left:", lives)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        lives -= 1
        print("Wrong Guess!")

if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)