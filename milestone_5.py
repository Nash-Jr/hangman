import random
class Hangman:
    def __init__(self, word_list, num_lives =5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.random_word = random.choice(word_list)
        self.word_length = ['_'] * len(self.random_word)
        self.num_letters = len(set(self.random_word))
        self.list_of_guesses = []


    def _check_guess(self, user_guess):
        """
    This function checks if the users guessed letter is in the random word.

    Parameters:
    user_guess (string): The letter the user guessed.

    Returns:
    if correect:
        str: "good guess user_guess is in the word".
    if incorrect:
        str: "Sorry user_guess is not int the word"
        int: The number of lives the user has left
    """
        if user_guess in self.random_word:
            print(f"Good guess {user_guess} is in the word")
            for i, letter in enumerate(self.random_word):# iterates through the letters of a string
                if self.word_length[i] == '_':
                    self.word_length[i] = letter
            self.num_letters = self.num_letters - 1
            print(f"You have {self.num_lives} lives left")
        else:
            print(f"Sorry, {user_guess} is not in the word. Try again.")
            if user_guess not in self.random_word :
                self.num_lives = self.num_lives - 1
                print(f"You have {self.num_lives} lives left")


    def display_word(self):
        displayed_word = [letter if letter != '_' and letter in self.list_of_guesses else '_' for letter in self.random_word]
        print(" ".join(displayed_word))


    def ask_for_input(self):
        """
    This function asks the user to guess a letter, checks if the letter has already been guessed,
    and validates that the input is a single alphabetical character.

    Returns:
    str: 'You already tried that letter!' if the letter has already been guessed.
    str: 'Invalid letter. Please, enter a single alphabetical character.' if the input is not valid.
    """  
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
            self._check_guess(user_guess)
        self.list_of_guesses.append(user_guess)


def play_game(word_list):
    """
        This function plays the game until the user has either won or used up all their lives.

    Returns:
    str: 'You lost'
    str: 'Congratulations. You won the game!'
    
    
    """

    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"The word was {game.random_word}")
            print("You lost")
            break    
        if game.num_letters > 0:
            game.display_word()
            game.ask_for_input()
        else:
            game.display_word()
            print("Congratulations. You won the game!")
            print(f"The word was {game.random_word}!")
            break


word_list = ["apple", "orange", "mango", "pineapple", "banana"]
Hangman.display_word 
play_game(word_list)
