import random
favpurite_fruits = ["Apple", "Orange", "Mango", "Pineapple", "Banana" ]

word_list = favpurite_fruits

word = random.choice(word_list)

guess = input("Guess a letter ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.1")
print(word_list)
print(word)