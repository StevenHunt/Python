# Steven  Hunt - Logistic Solutions (Lupe & Brenna)
# CST - 205
# 3.24.2017


# Bueller.wav : https://ilearn.csumb.edu/pluginfile.php/451674/mod_page/content/15/bueller.wav


# ------------- LAB 8 ------------------

# Now you try it: 

# Sample value of shirly.wav @ location 10,000: 50

# Increase the volume by two :

def increaseVolume(sound):

   for sample in range(0, getLength(sound)):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * 2)  
   return sound
   play(sound)
   writeSoundTo(sound, '/home/steven/Desktop/increaseClip.wav') 

# Using Bueller.wav: 
# Original @ 10730: 1
# Original @ 20350: 0
# After @ 10730: 2
# After @ 20350: 0
 
# ***************************************************************
      
# Decrease the volume by half: 

def decreaseVolume(sound):
   
   for sample in range(0, getLength(sound)):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value /2) 

# Using Bueller.wav
# Orignal @ 10730: 1
# After @ 10730: 0

# ***************************************************************

# Change the volume by a specific amount: 

def changeVolume(sound, amount):
  
  for sample in getSamples(sound):
    value =getSampleValue(sample)
    setSampleValue(sample, value*amount)

# Using Bueller.wav
# Original @ 10730: 1
# changeVolume(sd, 3) @ 10730: 3
# changeVolume(sd,.5) @ 10730: 0 

# ***************************************************************

# Create a maxSample function to find the maximum value in the sample. 
# Cratea a maxVolume function to increase the volume of each sample by the factor. 



def maxSample(sound):
  
  largest = 0                                       # Initialize larger to 0
  for s in getSamples(sound):                       # Get all sample values
    largest = max(largest, getSampleValue(s))       # max(x,y), checks larger vs all sample values (returns a value)
  return largest                                    # returns the largest value in the sample
  # Found largest sample value to be : 89
  
  
def maxVolume(sound):
  largest=0
  for s in getSamples(sound):
    largest=max(largest,getSampleValue(s))
  ratio=32767/largest
  print largest
  print ratio
  
  for s in getSamples(sound):                       # get all samples values 
    louder = ratio * getSampleValue(s)              # multiply all sample values by highest possible ratio
    setSampleValue(s, louder)                       # set all sample values to their relative highest value
  
  # Are all sample values supposed to be increased by 89? 
        
# Using Bueller.wav
# Original @ 80100: 12 
# maxVolume @ 80100: 66 

""" Why is this the factor that will give you the maximum increase?         

By finding the value of the highest sample value in the file and knowing the largest value a sample can have, 
we can find the highest possible multiplier for the remaining sample values that will increase the volume 
relatively, without exceeding the largest value. 
"""

# *************************************************************** 

# A function that sets all the sample values above 0 to the maximum value of 32767. Also, any values below 0 are set to the minimum value of -32768.

def goToEleven(sound):
  
  for s in range(0, getLength(sound)):
    if s > 0: 
      setSampleValueAt(sound, s,32767)
    elif s < 0: 
      setSampleValueAt(sound, s,-32768)
  return sound

""" What does the sound you generate in goToEleven sound like?  Why can you hear anything at all if everything has the same amplitude?

There is no sound when you play a sound after loading it through goToEleven. You cannot hear anything because everything has the same amplitude?

""" 
  
    
    
