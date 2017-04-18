# Logistic Solutions - Steven H, Brenna E, Lupe A. 
# CST 205 - Lab 15
# 04.15.17

import random

def craps():

  Game = true
  AutoWin = [7, 11]
  AutoLose = [2, 3, 12]
  
  while Game == true:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    sum = die1 + die2
    
    showInformation("Press Enter to Roll:")
    if sum in AutoWin:
      showInformation("You rolled a " + str(sum) + ".  You win!")
      printNow("You rolled a " + str(sum) + ".  You win!")
      Game = false
    elif sum in AutoLose:
      showInformation("You rolled a " + str(sum) + ".  You lose!")
      printNow("You rolled a " + str(sum) + ".  You lose!")
      Game = false    
    else: 
      showInformation("You rolled a " + str(sum) + ".")
      printNow("You rolled a " + str(sum) + ".")
      point = sum
      sum = 0
      while sum != 7 and sum != point:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum = die1 + die2
        showInformation("You rolled a " + str(sum) + ".")
        printNow("You rolled a " + str(sum) + ".")
      if sum == 7:
        showInformation("You lose!")
        printNow("You lose!")
        Game = false
      else:
        showInformation("You hit your point, you win!")
        printNow("You hit your point, you win!")
        Game = false
  

