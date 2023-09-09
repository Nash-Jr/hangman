import random
favpurite_fruits = ["Apple", "Orange", "Mango", "Pineapple", "Banana" ]

word_list = favpurite_fruits

word = random.choice(word_list)



def check_guess(user_guess):
    if user_guess in word:
        print(f"Good guess {user_guess} is in the word")
    else:
        print(f"Sorry, {user_guess} is not in the word. Try again.")
    

def ask_for_input():
    while True:
        user_guess = input("Guess a letter ").lower()
        if len(user_guess) == 1 and user_guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(user_guess)

ask_for_input()

print(word)


