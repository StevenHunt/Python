# Steven Hunt - Logistic Solutions
# CST 205
# March 10 2017

# PROBLEM 1 - Use pixel manipulation to mirror a picture. 

# Verticle Mirror 
def mirror1():
  pic = makePicture(pickAFile()) # Creates a picture called 'pic', from path 'file'
  w=getWidth(pic) # Takes picture 'pic' as input and returns its length in the number of pixels left-to-right in the picture.
  h=getHeight(pic) # Take picture 'pic' as input and returns its length in the number of pixels from top-to-botton in the picture. 
  mirror1=makeEmptyPicture(w,h) # Creates a new empty picture called mirror1 with the width and height of 'pic'. 
  for x in range(0, w/2): # iterates through width/2
    for y in range(0, h): # iterates through the entire height
      color=getColor(getPixel(pic, x, y)) # Set color to the pixel at position x & y in pic. 
      setColor(getPixel(mirror1, x, y), color) # Takes in a pixel by getPixel and a color, and sets the pixel to the given color.
      setColor(getPixel(mirror1,w-x-2, y),color)
  show(mirror1)   # Show mirror1
  writePictureTo(mirror1, "/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 4/mirror1.jpg")  #Takes a picture and a file name, then writes the picture to the file. 

# Horizontal Mirror: top-to-bottom
def mirror2():
  pic = makePicture(pickAFile())
  w=getWidth(pic)
  h=getHeight(pic)
  mirror2=makeEmptyPicture(w,h)
  for y in range(0, h/2):  
    for x in range(0, w):
      color=getColor(getPixel(pic, x, y)) 
      setColor(getPixel(mirror2, x, y), color)
      setColor(getPixel(mirror2, x, h-y-2),color)
  show(mirror2)    
  writePictureTo(mirror2, "/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 4/mirror2.jpg")  
 
# Horizontal Mirror: bottom-to-top
def mirror3():
  pic = makePicture(pickAFile())
  w=getWidth(pic)
  h=getHeight(pic)
  mirror3=makeEmptyPicture(w,h)
  for y in range(0, h/2):  
    for x in range(0, w):
      color=getColor(getPixel(pic, x, h-y-1))
      setColor(getPixel(mirror3, x, y), color)      
      setColor(getPixel(mirror3, x, h-y-2),color)
  show(mirror3)
  writePictureTo(mirror3, "/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 4/mirror3.jpg") 
 
# Quadruple Mirror : Combination of mirror1() and mirror2()
def mirror4():
  pic = makePicture(pickAFile())
  for x in range(0, getWidth(pic)):
    for y in range(0, (getHeight(pic)/2)):
      px = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic, x, getHeight(pic)-y-1), px)
  for x in range((getWidth(pic)/2), getWidth(pic)):
    for y in range(0, getHeight(pic)):
      px = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic, getWidth(pic)-x-1, y), px)
  show(pic)
  writePictureTo(pic, "/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 4/mirror4.jpg") 
  
# PROBLEM 2 - Make a copy of a picture. 

def simpleCopy():
  pic = makePicture(pickAFile())
  w, h = getWidth(pic), getHeight(pic)
  copy = makeEmptyPicture(w,h)
  for x in range(0, w): 
    for y in range(0, h):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(copy, x, y), color)
      setColor(getPixel(copy,x, y),color)      
  show(copy)
  writePictureTo(copy, "/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 4/copy.jpg")
  
# PROBLEM 3 - Copy and rotate picture. 

def rotatePic():
  pic = makePicture(pickAFile())
  w,h = getWidth(pic), getHeight(pic)
  rotatedPic = makeEmptyPicture(h, w) # Rotating the new empty picture
  for y in range(h): # Loop through all the pixels in the picture
    for x in range(w): 
      color = getColor(getPixel(pic, x, y)) # Were getting all the pixels in picture, and the color. 
      targetPixel = getPixel(rotatedPic, y, x) # not x, y!
      setColor(targetPixel, color)
  show(rotatedPic)
  writePictureTo(rotatedPic, "/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 4/rotatedPic.jpg")

# PROBLEM 4 - Scale down a picture.
            
def shrink():
  pic = makePicture(pickAFile())
  w,h = getWidth(pic), getHeight(pic)
  canvas = makeEmptyPicture(w /2 , h /2)
  for x in range (0, getWidth(canvas)- 1): # Loop through all pixels of the canvas
    for y in range (0, getHeight(canvas)- 1):
      color = getColor(getPixel(pic, x * 2, y * 2)) # Grab every other pixel from the original picture (pic)
      setColor(getPixel(canvas, x, y), color) # Assign that color to the corresponding pixel on the new picture (canvas)
  show(pic)   
  show(canvas)
  writePictureTo(canvas, "/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 4/scaledImage.jpg")
          

                    



































        
