# Steven Hunt - Logistic Solutions
# CST 205
# March 16, 2017
 
 
# Lab # 7

# Warm Up - Find an image of the desert and draw a snowman on it. 

def snowMan(): 
  pic = makePicture(pickAFile())
  w, h = getWidth(pic), getHeight(pic)
  addOvalFilled(pic,200,450,180,180,white)
  addOvalFilled(pic,218,350,140,140,white)
  addOvalFilled(pic,236,255,100,100,white)
  show(pic)
  writePictureTo(pic,"/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/Snowman.jpg")
  
# St. Patricks Day Greeting Card -  

# Darth
def betterBnW(pic): 
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = r * 0.299 + g * 0.587 + b * 0.114
    setRed(p, luminance)
    setGreen(p, luminance)
    setBlue(p, luminance)
  return(pic) 

# Background Image (target)
def sepia(pic):
    pic = betterBnW(pic)
    for x in range(0, getWidth(pic)):
        for y in range(0 , getHeight(pic)):
            p = getPixel(pic, x, y)
            r = getRed(p)
            b = getBlue(p)        
            if r < 63:
                setRed(p, r * 1.1)
                setBlue(p, b * 0.9)
            elif r < 192:
                setRed(p, r * 1.15)
                setBlue(p, b * 0.85)
            else:
                if (r * 1.08) > 255:
                    setRed(p, 255)
                else:
                    setRed(p, r * 1.08)
                setBlue(p, b * 0.93)
    return(pic)

# St.Patrick Stained Glass Window
def shrink(pic):
  w,h = getWidth(pic), getHeight(pic)
  canvas = makeEmptyPicture(w /6 , h /6)
  for x in range (0, getWidth(canvas)- 1): # Loop through all pixels of the canvas
    for y in range (0, getHeight(canvas)- 1):
      color = getColor(getPixel(pic, x * 6, y * 6)) # Grab every other pixel from the original picture (pic)
      setColor(getPixel(canvas, x, y), color) # Assign that color to the corresponding pixel on the new picture (canvas)
  return canvas

def darkenUp(pic): 
  pixels = getPixels(pic)
  
  for p in pixels:
    c = getColor(p)
    c = makeDarker(c)
    setColor(p,c)
  return(pic)

def lab7():

  # Target Photo
  target =  makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/Ireland.jpg") 
 
  background = target 
  
  # Creating variables and assigning pictures: 
  leprechaun_1 = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/Leprechaun_1.png")
  leprechaun_2 = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/Leprechaun_2.png")
  leprechaun_3 = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/Leprechaun_3.png")
  window = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/StPatrick.jpg")
  darth = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/DarthBeer.jpg")
  bubble = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/Bubble.jpg")
  wording = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/HSPD.png")
          
  # Images: 
  pyCopy(sepia(background),target,0,0)
  greenCopy(leprechaun_1,target,800,774)
  greenCopy(leprechaun_2,target,900,773)  
  greenCopy(leprechaun_3,target,80,770) 
  pyCopy(shrink(darkenUp(sepia(window))),target,564,274)
  grayCopy(betterBnW(darth),target,216,265)
  greenCopy(bubble,target,80,222)
  whiteCopy(wording,target,750,20)
  
  # Font: 
  myFont1 = makeStyle("Courier", bold, 13)
  fontColor = makeColor(24,126,24)
  str1 = "Don't fight!"
  str2 = "Have a beer!"
  addTextWithStyle(target, 110,270,str1,myFont1,fontColor)
  addTextWithStyle(target, 110,285,str2,myFont1,fontColor)
    
  # Helps define placement
  # explore(target)
  
  show(target)
  
  # Writes target picture to file : St-Patricks-Day.jpg
  writePictureTo(target,"/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 3/Lab 7/St-Patty-Day.jpg")

# For green screened images
def greenCopy(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     if distance(color, green) > 55.0:
       setColor(getPixel(target, targetX+x, targetY+y), color)

# For darth image (converted to black and white w/ betterBnW)
def grayCopy(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     if distance(color, gray) > 50.0:
       setColor(getPixel(target, targetX+x, targetY+y), color)

# For banner
def whiteCopy(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     if distance(color, white) > 50.0:
       setColor(getPixel(target, targetX+x, targetY+y), color)

def pyCopy(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     setColor(getPixel(target, targetX+x, targetY+y), color)
