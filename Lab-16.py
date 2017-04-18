# Logistic Solutions - Steven H, Brenna E, Lupe A
# CST 205 - Multimedia with Python
# 04.15.17

import urllib
import urllib2

#---------------------------------WARM UP-----------------------------------------
def makePage():
  folder = pickAFolder()
  file = open(folder + "myHTML.html", "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")
  
  file.close()

#---------------------------------PROBLEM #1--------------------------------------------
#********************************Load Information from website*************************  

# ORIGINAL WEBSITE: http://www.catbreedslist.com/

def getInfo():    
    
    site = urllib.urlopen("http://www.catbreedslist.com/")
    text = site.read()

    search = true                                   #Switch to stop searching html code
    bdFlag = '</a></p><span>Lifespan:'              #Identifies text where cat breed will display in original html
    lfFlag = 'Lifespan: '                           #Identifies text where lifespan will display in original html
    wtFlag = '</p><span>Pounds(Max)'                #Identifies text where weight will display in original html
    breed = ''                                      #Initiates variable to load key into dictionary (cat breed)          
    life = ''                                       #Initiates variable to load cat's lifespan into dictionary
    weight = ''                                     #Initiates variable to load cat's weight into dictionary
    catInfo = {}                                    #Creates empty dictionary to store cat info

    for i in range(0, len(text)-5):                 #Traverses original html code letter by letter
       if search == true:                           #  until the search switch is turned off
            b = i                                   #Initiates pointers to find beginning or end of text
            l = i
            w = i
            if text[i:i+23] == bdFlag:              #If the breed flag is found... 
                while text[b] <> '>':               #  Look for beginning char
                    b -= 1                          #  Update beginning character index
                breed = text[b+1:i]                 #  Store text betweeen beginning character and end character in breed

            if text[i:i+10] == lfFlag:              #If the lifespan flag is found...
                while text[l] <> '<':               #  Look for ending char
                    l += 1                          #  Update ending character index
                life = text[i+10:l]                 #  Store text between beginning character and end character in lifespan
                
            if text[i:i+21] == wtFlag:              #If the weight flag is found...
                while text[w] <> '>':               #  Look for beginning char
                    w -= 1                          #  Update beginning character index
                weight = text[w+1:i] + ' pounds'    #  Store text between beginning character and end character in weight
                
            if breed <> '':                         #If breed is not empty
                catInfo[breed] = [life, weight]     #  add a new record to the dictionary where breed is the key
                
       if text[i:i+7] == '<tbody>':                #Stop searching html when identifying text is reached
            search = false    
    site.close()                                    #Close connection
    printNow(catInfo)                               #View dictionary
    return catInfo                                  #Return dictionary

#********************************Make New HTML File************************* 

def newHTML():                                                         
    
    dict = getInfo()                                                                  #Get dictionary containing cat info
    folder = pickAFolder()                                                            #Pick a folder to store new html file
    file = open(folder + "catinfo.html", "wt")                                        #Make new html file
                                                                                      #Write html code to file
    file.write("""<!DOCTYPE HTML PUBLIC >\n
    <html>\n
    \t<head><title>Cat information chart...</title><h1>Information chart on cat breeds:</h1></head>\n
    \t\t<body>\n
    \t\t\t<table style="width:50%"><tr><th>BREED</th><th>LIFESPAN</th><th>WEIGHT</th></tr>\n""")
    
    for key in dict:                                                                  #Traverse dictionary and print info into HTML 
    
        file.write('\t\t\t\t<tr><td>'+key+'</td>')                                    
        file.write('<td>'+dict[key][0]+'</td>')
        file.write('<td>'+dict[key][1]+'</td></tr>\n')
    
    file.write('\t\t\t</table>\n\t\t</body>\n</html>')
    file.close()                                                                      #Close connection