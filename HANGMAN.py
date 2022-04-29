import random
words = ["apple", "mango", "football", "cricket", "python", "javascript", "redbull", "sting"]
word = random.choice(words)
word_len = len(word)
guess_word = []
print("WELCOME TO HANGMAN GAME")
print("Your word is : ", end="")
for i in range(word_len):
    guess_word.append("_ ")
lives = 2
while True:
    print("".join(guess_word))
    print(f"No. of lives is {lives}")
    user_choice = input("Guess the letters : ").lower()
    z = 0
    for i, letter in enumerate(word):
        if user_choice == letter:
            guess_word[i] = letter
            z += 1
    if z == 0:
        lives -= 1
    if lives == 0:
        print("YOU LOOSE")
        break
    if "".join(guess_word) == word:
        print("YOU WIN")
        break
print("GAME OVER")