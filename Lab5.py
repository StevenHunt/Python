# Steven Hunt - Logistic Solutions
# CST 205 
# March 11 2017

# Lab 5 - Advanced Image Manipulation

# Warm Up : Copy an image onto the middle of a larger canvas. 

def centerImage():
  pic = makePicture(pickAFile())
  w, h = getWidth(pic), getHeight(pic)
  copy = makeEmptyPicture(w*2,h*2)
  targetX = w/2 
  for sourceX in range(0, w): 
    targetY = h/2
    for sourceY in range(0, h):
      color = getColor(getPixel(pic, sourceX, sourceY))
      setColor(getPixel(copy, targetX, targetY), color)
      targetY = targetY + 1
    targetX = targetX + 1
  show(copy)
  writePictureTo(copy, "/home/steven/Desktop/centerImage.jpg")

# PROBLEM 1 - A function that copies an image (source) to another (target), in addition to using x & y locations as arguments (targetX & targetY). 

#Test files for problem 1 
# target = makePicture("/home/steven/Desktop/blank.jpg")
# source = makePicture("/home/steven/Desktop/1.jpg")

def pyCopy1(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     setColor(getPixel(target, targetX+x, targetY+y), color)  
  show(target)
  writePictureTo(target,"/home/steven/Desktop/blank.jpg")  

# PROBLEM 2 - 
  
# Image Modifiers:
      
# Saturn      
def mirror2(pic):
  w, h = getWidth(pic), getHeight(pic)
  mirror2 = makeEmptyPicture(w,h)
  for y in range(0, h/2):  
    for x in range(0, w):
      color=getColor(getPixel(pic, x, y))
      setColor(getPixel(mirror2, x, y), color)
      setColor(getPixel(mirror2, x, h-y-2),color)
  return mirror2  
  
# Jupiter  
def shrink(pic):
  w,h = getWidth(pic), getHeight(pic)
  canvas = makeEmptyPicture(w /4 , h /4)
  for x in range (0, getWidth(canvas)- 1): # Loop through all pixels of the canvas
    for y in range (0, getHeight(canvas)- 1):
      color = getColor(getPixel(pic, x * 4, y * 4)) # Grab every other pixel from the original picture (pic)
      setColor(getPixel(canvas, x, y), color) # Assign that color to the corresponding pixel on the new picture (canvas)
  return canvas
  
# Name
def makeNegative(pic):
  for p in getPixels(pic):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor(255 - red, 255 - green, 255 - blue)
    setColor(p, negColor)
  return pic

# Mars
def moreRed(pic,percentage): 
  pixels = getPixels(pic)
  percentage = (100 - percentage) / 100.0
  for p in pixels:
    r = getRed(p)
    setRed(p, r * percentage)
  return pic
  
# Uranus
  
def roseColoredGlasses(pic):    
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 1.5)
  return pic
  
# Collage Function
def makeCollage():

  # Creates target image, set to 8.5 x 11 with black background. 
  target = makeEmptyPicture(2550,3300,black)
  
  # Creating variables and assign pictures: 
  mercury = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/1-Mercury.jpg")
  venus = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/2-Venus.jpg")
  earth = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/3-Earth.jpg")  
  mars = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/4-Mars.jpg")
  jupiter = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/5-Jupiter.jpg")
  saturn = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/6-Saturn.jpg")
  uranus = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/7-Uranus.jpg")
  neptune = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/8-Neptune.jpg")
  name = makePicture("/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/Name.jpg")  
  
  # Calls function pyCopy to copy image to specific target file at specific x/y locations. 
  pyCopy(mirror2(saturn),target,500,1200) 
  pyCopy(shrink(jupiter),target,1500,300)
  pyCopy(mercury,target,20,20)
  pyCopy(moreRed(mars,75),target,120,120)
  pyCopy(venus,target,240,240)
  pyCopy(earth,target,390,390)
  pyCopy(neptune,target,540,540)
  pyCopy(roseColoredGlasses(uranus),target,970,950)
  pyCopy(makeNegative(name),target,600,2500)
  
  # Writes target picture to file : target.jpg
  writePictureTo(target,"/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 5/target.jpg")
  
def pyCopy(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     setColor(getPixel(target, targetX+x, targetY+y), color)


