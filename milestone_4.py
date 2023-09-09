import random

class Hangman:
    def __init__(self, word_list, num_lives =5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.random_word = random.choice(word_list)
        self.letter_guessed = ['_'] * len(self.random_word)
        self.num_letters = len(set(self.random_word))
        self.list_of_guesses = []


    def check_guess(self, user_guess):
        if user_guess in self.random_word:
            print(f"Good guess {user_guess} is in the word")
        else:
            print(f"Sorry, {user_guess} is not in the word. Try again.")

        for i, letter in enumerate(self.random_word):
            if self.letter_guessed == '-':
                self.letter_guessed = letter
            self.num_letters = self.num_letters - 1
        if user_guess not in self.random_word :
            self.num_lives = self.num_lives - 1
        print(f"You have {self.num_lives} lives left")


    def ask_for_input(self):
        while True:
            user_guess = input("Guess a letter ").lower()
            if len(user_guess) == 1 and user_guess.isalpha():
                if user_guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        if user_guess not in self.list_of_guesses:
            self.check_guess(user_guess)
        self.list_of_guesses.append(user_guess)

word_list = ["Apple", "Orange", "Mango", "Pineapple", "Banana"]
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()