# Steven Hunt - Logistic Solutions
# CST 205 - Lab 14.1
# 04.10.17

#------------------------------------------------------------------------------------------------------

import string

def wordCounter(): 
  
  # Variables: 
  maxVal = 0    # To compare and find highest value in d
  numWords = 0  # Keeps track of total words
  d = {}        # Empty dictionary
  
  # Opening file: 
  filename = open('/home/steven/Desktop/Link to: CST205/Module 6/Lab 14/1/eggs.txt','r')

  # For-loop: Traverse file and count number of total words: 
  for line in filename:
    wordsList = line.split()
    numWords += len(wordsList)
    
    
    line = line.lower() # Make all words lowercase (no difference between eggs and Eggs)
    
    # For-Loop: Split words and keep count of each word. 
    for word in line.split(): 
      word = word.translate(string.maketrans("",""), string.punctuation)
      
      # If word is already in dictionary, increment 1. 
      try:
        d[word] += 1
        
      # Else make count 1
      except:
        d[word] = 1
    
  # For-Loop: Checks dictionary's key/value pairs against each other to find most commonly occuring word. 
  for k,v in d.items(): 
    if v > maxVal: 
      maxVal = v
      maxKey = k
  
  # Outputs: 
  print "The total amount of words are: ", numWords
  print "The most commonly occuring word is:", maxKey, "@", maxVal, "times"
  print "The list of words and their count: \n", d
  
  