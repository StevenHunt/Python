# File Information

# Steven Hunt - Logistist Solutions (Individual)
# CST 205 - Lab #9
# 03.25.17
# File: Lab9.py

# ----------------------------------------------------

# Problem 1: CLIP

# A function that will create a clipped wav file. 
# Parameters: source(.wav file), start(starting sample value), end(ending sample value

def clip(source, start, end):
  
  target = makeEmptySound(end - start)                      # 1.  Make new empty sound file. 
  targetIndex = 0 # Initializing targetIndex
  
  for sourceIndex in range(start, end):                     # 2.  Iterate through each index (start to end)
    sourceValue = getSampleValueAt(source, sourceIndex)     # 2a. Get value from specific source index. 
    setSampleValueAt(target, targetIndex, sourceValue)      # 2b. Copy value to target location. 
    targetIndex = targetIndex + 1 # Increment targetIndex 1 everytime we copy a sample from source to target.     
  return target
  writeSoundTo(target,"/home/steven/Desktop/clipped.wav")  
  

# ******************************************************************

# Problem 2: COPY

# A generic function that will let us splice smaller sounds into larger ones.
# Parameters: source(short .wav clip), target(sound being created from combining the clips), start(index in copy where source should begin) 

def copy(source, target, start):
  
  targetIndex = start                                        # Using start as the index for target.  
  
  for sourceIndex in range(0, getLength(source)):            # Iterating through all of source sound
    sourceValue = getSampleValueAt(source, sourceIndex)      # Get all the samples values of source
    setSampleValueAt(target, targetIndex, sourceValue)       # Set all of sources samples into target a targetIndex.
    targetIndex = targetIndex + 1                            # Increment targetIndex everytime we copy a sample from the source to target. 


# ******************************************************************

# Problem 3: Collage of Adam Sandler quotes

def collage():
  
  # Create sound using orignal files from their paths:
  littleNik = makeSound("/home/steven/Desktop/Link to: CST205/Sounds /11025/Adam Sandler/nicky.wav") 
  fiftyDates = makeSound("/home/steven/Desktop/Link to: CST205/Sounds /11025/Adam Sandler/50dates.wav")
  angerMan = makeSound("/home/steven/Desktop/Link to: CST205/Sounds /11025/Adam Sandler/anger.wav")
  billyMad = makeSound("/home/steven/Desktop/Link to: CST205/Sounds /11025/Adam Sandler/billy.wav")
  waterBoy= makeSound("/home/steven/Desktop/Link to: CST205/Sounds /11025/Adam Sandler/waterboy.wav")
  

  # Creating clips from the original sounds:
  angerClip = clip(angerMan,405678,521140)
  fiftyClip = clip(fiftyDates,64252,128229)
  
  # Finding lengths of each sound
  litLen = getLength(littleNik)
  fifLen = getLength(fiftyClip)
  angLen = getLength(angerClip)
  bilLen = getLength(billyMad)
  watLen = getLength(waterBoy)
  
  # Setting totalLen to the total length of the 5 sounds:
  totalLen = litLen + fifLen + angLen + bilLen + watLen

  # Finding sample rates for each sound:
  litRate = int(getSamplingRate(littleNik))
  fifRate = int(getSamplingRate(fiftyClip))
  angRate = int(getSamplingRate(angerClip))
  bilRate = int(getSamplingRate(billyMad))
  watRate = int(getSamplingRate(waterBoy))
  
  # Setting totalRate to average sample rate:
  totalRate = (litRate + fifRate + angRate + bilRate + watRate) / 5 
  print "The average sample rate is: " , totalRate
  
  # Creates new sound file set to the length of the 5 sounds: 
  newSound = makeEmptySound(totalLen, 11025)
  
  # Calling copy function to copy sounds to target locations in newSound: 
  copy(littleNik,newSound,0)
  copy(fiftyClip,newSound,litLen)
  copy(angerClip,newSound,litLen + fifLen)
  copy(billyMad,newSound,litLen + fifLen + angLen) 
  copy(waterBoy,newSound,litLen + fifLen + angLen + bilLen) 
  
  # Increase volume:
  increaseVolume(newSound)
 
  play(newSound)
  writeSoundTo(newSound,"/home/steven/Desktop/collage.wav")

def increaseVolume(sound):

  for sample in range(0, getLength(sound)):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(sound, sample, value * 4)  
    
# ******************************************************************

# Problem 4: RERVERSE

def reverse():
  
  # Creating sounds to use and store  
  source = makeSound(pickAFile())
  newSound = duplicateSound(source)
  
  # Assining index to the length of sound - 1 sample. 
  index = getLength(source)-1
  
  # i iterates through and gets all sample values of source sound and assigns them to variable sourceSample
  for i in range(1, getLength(source)) :
    sourceSample = getSampleValueAt(source, i)
    
    # Sets sourceSample to destination sound and copy in reverse order
    setSampleValueAt(newSound, index, sourceSample)
    index = index - 1
  
  writeSoundTo(newSound,"/home/steven/Desktop/destination.wav")
