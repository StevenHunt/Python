# Steven Hunt - Logistic Solutions
# CST 205 - Lab 14 #2
# 4.10.17

#---------------------------------------------------------------------------------------------------------------------------------------

# Pulls headlines from html file. 
def pullHeadlines():

  # Open file:
  file = open('/home/steven/Desktop/OtterRealm.html')
  
  # Variables: 
  string = file.read()                                      #Read all text into a string
  headlines = []                                            #Create an empty list to hold all headlines 
  startIndices = []                                         #Create an empty list to hold the starting index of each headline
  endIndices = []                                           #Create an empty list to hold the ending index of each headline
  start = string.find('pagination', 0, len(string))         #Variable to hold the starting index of the <div> element we're tracing through
  end = string.find('/article', 0, len(string))             #Variable to hold the ending index of the <div> element we're tracing through
  newString = string[start:end]                             #Create a new substring using those start and end
  
  # For-loop: 
  for x in range(0, 20):
    
    #Finds the start and end index of the first headline and stores it in the startIndices and endIndices lists
    if x == 0:
      startIndices.append(newString.find('</a>\'&gt;</span>', 0, len(newString)) + 16)
      endIndices.append(newString.find('<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/h1&gt;</span><span class="html-tag">&lt;p&gt;</span><span class="html-tag">&lt;p&gt;</span>', 0, len(newString)) + 16)
   
    #Finds the start and end index of each headline after the first headline and stores it in the startIndices and endIndices lists
    else:
      startIndices.append(newString.find('</a>\'&gt;</span>', startIndices[x - 1], len(newString)) + 16)
      endIndices.append(newString.find('<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/h1&gt;</span><span class="html-tag">&lt;p&gt;</span><span class="html-tag">&lt;p&gt;</span>', endIndices[x - 1], len(newString)) + 16)
      
  #Appends each headline using their start and end indices and prints them each out on a new line
  for x in range(0, 20):
    headlines.append(newString[startIndices[x]:endIndices[x] - 16])
    print headlines[x]