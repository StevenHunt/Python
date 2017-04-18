# Steven Hunt - Logistic Solutions ( Lupe and Brenna )
# CST 205 - Lab # 10
# 03.26.2017

# ---------------------------------------

# Warm Up: 

# A
def example():

  a = requestString("What is your name?")
  printNow (name)

# B: 
def loop():
  
  pwd = "Drowssap1"
  loop_condition = True
  
  while loop_condition:
    word = requestString("Enter the password: ")
    if word == pwd:
      loop_condition = False
    elif word == "stop":
      loop_condition = False
    else:
      pass
    
# *********************************************************************************************

# Hangman: 

""" 
1. Output a brief description of the game of hangman and how to play
2. The word to guess can be hard-coded in your program, but it should be easy to change the word.
3. Output the appropriate number of dashes and spaces to represent the phrase.
4. Continuously read guesses of a letter from the user and fill in the corresponding blanks if the letter is in the word, otherwise report that the user has made an incorrect guess. 
    - If the user guesses a letter in the word, it does not count against their 6 guesses
    - Any guess that is not in the word counts against the allowed six
    - The user MUST enter letters - if the user enters anything that is not a letter, you should print an error message and reprompt for input
    - Your program should handle input either as uppercase or lowercase letters
5. Each turn you will display the phrase as dashes but with any already guessed letters filled in, as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
6. Use at least 3 string methods or operators in a useful manner 
"""

def introduction():
  printNow(" ============================================================================================================================================================ \n ")
  printNow("Welcome to Hangman! \n")
  printNow("Description: A simple 2 player game. One person chooses a word, while the other person has to guess it letter-by-letter within a certain amount of tries. \n")   
  printNow("Rules:")
  printNow("1. The player chooses a single letter at a time, if the chosen letter is part of the word, it will be revieled to the player in it's specific location.")
  printNow("2. The player has a maximum of 6 incorrect guesses. If the player guesses a letter in the word, and it is incorrect, it will be displayed, and the incorrect count will be increased.")
  printNow("3. The game ends if the player runs out of guesses or if the player spells out the correct word. \n")
  printNow("Good luck!")


def hangman():
  
  introduction()                        # Calls introduction
      
  secretWord = "sailor"                 # The word to be guessed
  
  wordDashes = "-" * len(secretWord)    # Dashes for the word                                   
  guessedLetters = ""                   # The guessed letters (Correct or incorrect)
  correctLetters = 0                    # Counts the correct letters
  wrongAnswers = 0                      # Counts wrong answers
  
  # Range of possible inputs:
  possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  # Beginning of the game: 
  printNow ("The secret word is : " + wordDashes)
  
  while wrongAnswers <= 5:
     guessedLetter = requestString("Enter a single letter: " )   
     guessedLetter = guessedLetter.lower()                                 
    
     # IF input not allowed:
     if len(guessedLetter) != 1:
       printNow("Only 1 letter allowed, please try again.")
     elif guessedLetter in guessedLetters:
       printNow('No duplicate letters allowed, please try again.')
      
     elif guessedLetter not in possibleLetters:
       printNow('Only letters are accepted, please try again.')
     else:
       printNow("Your guess: " + guessedLetter)
       guessedLetters = guessedLetter + guessedLetters
    
       # IF correct letter chosen: 
       if guessedLetter in secretWord:
         guessedLetters = guessedLetters + guessedLetter
         correctLetters =  correctLetters + 1
         printNow("Correct.")
         printNow("Choose another correct letter, that isn't: " + guessedLetters + " ")         

         for a in range(len(secretWord)):
           if guessedLetter in secretWord[a]:
             wordDashes = wordDashes[:a] + secretWord[a] + wordDashes[a+1:]   
                                                                            
         printNow(wordDashes)
      
       # IF letter not correct: 
       else:
           wrongAnswers = wrongAnswers + 1
           printNow("Wrong letter, please try again.")
           
           # The letters that have been guessed:
           printNow("The letters you've guessed so far: " + guessedLetters + " ")
           
           # Remaining chances to guess:
           printNow("Your remaining chances:  " + str(6 - wrongAnswers)) 
        
     # IF player has ran out of chances:
     if wrongAnswers >= 6:
       printNow("Game Over.")
       break                           
      
     # IF player has guessed the right word: 
     if correctLetters == len(secretWord):
       printNow("Winner! The word is:  " + secretWord)
       break
