# Steven Hunt - Logistic Solutions
# CST 205 - Mini Lab
# 04.17.17

#-----------------------------------------------------------------------------------------------------

import string, urllib, urllib2

def htmlEGGS(): 

  d = {}        
  wordsList = 0
  numWords = 0
  
  # Opening file:wordCounter 
  readFile = open('/home/steven/School/Module 8/Mini - Lab/eggs.txt','r')
  file = open('/home/steven/School/Module 8/Mini - Lab/wordOutput.html','wt')

  # For-loop: Traverse file and count number of total words: 
  for line in readFile:
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
        d[word] = 1  #Initiates pointers to find beginning or end of text
    
  html_string = ("""
  <!DOCTYPE HTML PUBLIC > \n
 
  <html>\n       
    \t<head>
        
        <meta name="Author" content="Stfoobar.htmleven Hunt">
        <meta name="Course" content="CST 205 - Mini Lab">
        <meta name="Date" content="04.17.2017">
        
        <style type="text/css">
        body {background-color:black}
        </style>
    
        <title> Green Eggs and Ham </title>
        <h2 style="color:white"> Green Eggs and Ham Words:</h2> 
    
    \t</head> \n
        
        <br>
        <br> \n
        
        <body> 
           
  """)
  
  file.write(html_string)      
               
  # For-Loop:    file = open('/home/steven/Desktop/foobar.html','wt')
  for k,v in d.iteritems(): 
    if v >= 50: 
      fifties = k
      file.write('<h1 style="color:#f44641; font-size:50px">' + fifties + '</h1>')
    elif ( v >= 40 and v < 50): 
      fourties = k
      file.write('<h2 style="color:#f4a341; font-family:arial; margin-left:100px ">' + fourties + '</h2>')
    elif ( v >= 30 and v < 40): 
      thirties = k
      file.write('<h3 style="color:#f4f141; margin-left:150px" >' + thirties + '</h3>')
    elif ( v >= 20 and v < 30): 
      twenties = k
      file.write('<h4 style="color:#6ef441; margin-left:200px" >' + twenties + '</h4>')
    elif ( v >= 10 and v < 20): 
      tens = k
      file.write('<h5 style="color:#42e8f4; margin-left:250px">' + tens + '</h5>')
    elif ( v >= 1 and v < 10): 
      ones = k
      file.write('<h6 style="color:#b279d8; margin-left:300">' + ones + '</h6>')
  
  file.write(""" 
  
       </body> \n
  </html>""")
  
  file.close()


  
 
  
  