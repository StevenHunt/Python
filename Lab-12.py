# Steven Hunt, and Brenna Eckel, Guadalupe Alejo 
# CST205 - Lab 12
# 4.10.17

#==========================================PROBLEM 1:  MAD LIB GAME======================================================
def madLibs(): 
    origString = """Theres many an anecdote about babies who wont fall asleep unless jostled to rest by a car ride. 
                 Trying to drive a car inside a house is very difficult, so Ford whipped up a more elegant solution. 
                 Its called Max-Motor-Dreams, and it brings the car to the cot. A phone app records a nighttime drive,
                 and once everybodys back home, it tries to reproduce the experience of the drive using the cot. Theres 
                 a small speaker underneath the cot thats meant to provide the muffled sound of an engine. Mechanicals 
                 underneath the cot produce gentle movement, simulating a car trip. The whole thing is capped off with a 
                 set of LED-lights that provide the same warm glow that streetlights do. Its all in the hopes of getting 
                 the little one to sleep faster."""
   
    wordType = { 'jostled':'verb', 
                 'difficult':'adjective', 
                 'elegant':'adjective',
                 'Max-Motor-Dreams':'name',
                 'reproduce':'verb',
                 'cot':'noun (object)',
                 'engine':'noun (object)',
                 'LED-lights':'plural noun',
                 'streetlights':'plural noun',
                 'sleep':'verb',
                 'buy':'verb',
                 'demand':'verb'}        
             
    newWord = wordType 
    words = []
    words = origString.split()
    madString = ''
    
    for key in newWord:
        wordChoice = requestString(key + '  ' + wordType[key] + ': ')
        newWord[key] = wordChoice

    for i in range(0, len(words)):
        word = words[i]
        if word[len(word)-1].isalpha() == false:
            punct = word[len(word)-1]
            word = word[0:len(word)-1]
         
        if word in newWord:
            words[i] = newWord[word]
            leftBrace = '['
            rightBrace = ']'
        else:
            leftBrace = ''
            rightBrace = ''
            punct = ''
            
        madString += leftBrace + words[i] + rightBrace + punct + ' '
        
    printNow(madString) 

