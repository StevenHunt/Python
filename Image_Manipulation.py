# Steven Hunt - Logistic Solutions
# CST 205 - Multimedia Design and Programming with Python
# March 5, 2017

#Global Variable for Lab # 3
pic = makePicture(pickAFile())

# Lab 3 - Problem 1
# Write a new function called lessRed. This should work a lot like halfRed, but it should take a parameter that gives the percentage by which to reduce the red in the picture. 
# So, for example, the function call lessRed(75) would cause the function to reduce the red in the image by 75%.
# Rewrite halfRed so that it calls lessRed to do the red reduction for the image.

  
def halfRed1():    
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 0.5)  
  repaint(pic)
  lessRed(75)
  
def lessRed(percentage): 
  pixels = getPixels(pic)
  percentage = percentage / 100.0
  percentage = 1 - percentage
  
  for p in pixels:
    r = getRed(p)
    setRed(p, r * percentage) 
    
  repaint(pic)
    
    
 # Lab 3 - Problem 2
 # Now write a function called moreRed that increases the red in each pixel of an image the same way that lessRed decreased red. 
 # What might be a potential problem with increasing the red in a pixel? How could you mitigate this issue? Can you tell what JES is doing? 
 
 # The potential problem with increasing any pixel would be to make sure that it does not go over the highest RGB value of 255. Using a simple if/else statements could create boundries for the users input.  
  
def moreRed(percentage): 
  pic = get_pic()
  pixels = getPixels(pic)
  percentage = (100 - percentage) / 100.0
  
  for p in pixels:
    r = getRed(p)
    setRed(p, r * percentage)
    
  repaint(pic)
 

# Lab 3 - Problem 3
# Write a function called roseColoredGlasses that makes an image look pink. Think about how you can manipulate the RGB components of each pixel to accomplish this.

def roseColoredGlasses():    
  pic = get_pic()
  pixels = getPixels(pic)
  
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 1.5)
  
  repaint(pic)
  
# Lab 3 - Problem 4
# Write a function called lightenUp that uses a for loop to lighten each pixel in a picture. Remember that you can use getColor and setColor to access the color of a pixel.
  
def lightenUp(): 
  pic = get_pic()
  pixels = getPixels(pic)
  
  for p in pixels:
    c = getColor(p)
    c = makeLighter(c)
    setColor(p,c)
  repaint(pic)

# Lab 3 - Problem 5
# Write a function called makeNegative that creates the negative of an original picture. This means you will want to create the opposite value for the red, green and blue of that pixel. 
# How might you get the opposite?

def makeNegative():
  pic = get_pic()
  
  for p in getPixels(pic):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor(255 - red, 255 - green, 255 - blue)
    setColor(p, negColor)
  show(pic)
  repaint(pic)
  
# Lab 3 - Problem 6
# Create a function called BnW that converts each pixel to gray-scale by computing the average of the R G and B values for each pixel and then using that average as the new RGB values for that pixel.

def BnW():
  pic = get_pic()
  pixels = getPixels(pic)
  
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    lum = r*0.299 +b*0.114 + g*0.587
    bw = makeColor(lum,lum,lum)
    setColor(p, bw)
  repaint(pic)
    

