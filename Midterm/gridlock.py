# File Information:

# Steven Hunt - Logistic Solutions (Individual)
# CST 205 - Midterm Project 2
# 3.24.2017

# ************** FILTER OF YOUR CHOICE ( GRIDLOCK )

# ********************** README *********************************

# An image filter that copies the image into a 4 grid pattern, applies color enhancments on all 4 images (Red, Green, Blue Purple), and then creates a checkered grid over the top of the entire image. 

# The function first prompts the user to upload a picture of their choice. It then shrinks a copy of the original image, this is the image that will be copied 4 more times by my simple copy function. 
# Next, the function creates a blank canvas that is 4 times the size of the scaled down image. After, the function calls pyCopy to place the altered images into their specific locations on the empty canvas. 
# The borders and grid pattern are then applied via for-loops and the built in JES function, addRectFilled. 

# LOAD / RUN: Simply call the gridLock() function from the command line. 

# SAVING: When prompted, choose a folder in which to save the filtered image. The function will then prompt user to input a file name (DO NOT ADD EXTENSION, IT APPLIES .jpg AS EXTENSION). 

# IMAGE BOUNDRIES: The function is fully scalable to any sized image, although larger images may take a while to render filter. 

# ****************************************************************

def gridLock():
  
  # Choosing image to filter:
  showInformation("Please choose an image you wish to have filtered: ")
  original = makePicture(pickAFile())
  
  # Making copy of original image and calling shrink to scale down the image by 1/3: 
  makeCopy = copy(original)
  pic = shrink(makeCopy)
  
  # Calling copy to copy pic to 4 other identical images: 
  pic1 = copy(pic)
  pic2 = copy(pic)
  pic3 = copy(pic)
  pic4 = copy(pic)
  
  # Get width and height of scaled image:
  w,h = getWidth(pic),getHeight(pic)
  
  # Create new canvas (2x the size)
  canvas = makeEmptyPicture(w*2,h*2)
  
  # Get width and height of canvas image:
  w2,h2 = getWidth(canvas),getHeight(canvas)
  
  # Calling pyCopy: source, target, targetX, targetY
  
  pyCopy(reddify(pic1),canvas,0,0)   # 1.1    
  pyCopy(blueify(pic2),canvas,w,0)   # 1.2
  pyCopy(greenify(pic3),canvas,0,h)   # 2.1    
  pyCopy(purpleify(pic4),canvas,w,h)   # 2.2   
      
  # Border: picture, startX, startY, width, height,color
  addRectFilled(canvas,0,0,w2,10,black)       # Top
  addRectFilled(canvas,0,h2-10,w2,10,black)   # Bottom
  addRectFilled(canvas,0,0,10,h2,black)       # Left
  addRectFilled(canvas,w2-10,0,10,h2,black)   # Right  
  
  # Grid: start,stop,step 
  for l in range(w-5,w2,w):
    addRectFilled(canvas,l,0,10,h2,black)
  
  for m in range(h-5,h2,h):
    addRectFilled(canvas,0,m,w2,10,black)
    
  for i in range(10,w2,20):
    addRectFilled(canvas,i,0,2,h2,black)
  
  for j in range(10,h2,20):
    addRectFilled(canvas,0,j,w2,2,black)

  show(canvas)

  # Saving:
  folder = pickAFolder()
  file = requestString("Please enter filename you wish to save the image as:")
  path = folder + file + ".jpg"
  writePictureTo(canvas,path)

# Function that places an image, on a target image, at a specific x & y location:  
def pyCopy(source, target, targetX, targetY):

  w, h = getWidth(source), getHeight(source)
  
  for x in range(0, w): 
    for y in range(0, h): 
      color = getColor(getPixel(source, x, y))
      setColor(getPixel(target, targetX+x, targetY+y), color)  
  return target
 
# Function to scale the image down 1/2 the size:
def shrink(pic):
  
  w,h = getWidth(pic), getHeight(pic)
  canvas = makeEmptyPicture(w /2 , h /2)
  
  for x in range (0, getWidth(canvas)- 1):
    for y in range (0, getHeight(canvas)- 1):
      color = getColor(getPixel(pic, x * 2, y * 2))
      setColor(getPixel(canvas, x, y), color) 
  return(canvas)

# Function that creates an identical copy of an image:  
def copy(pic):
  
  w, h = getWidth(pic), getHeight(pic)
  copy = makeEmptyPicture(w,h)
  
  for x in range(0, w): 
    for y in range(0, h):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(copy, x, y), color)
      setColor(getPixel(copy,x, y),color)      
  return(copy)

# Functions to manipulate image colors:           
def reddify(pic): 
 
  pixels = getPixels(pic)
  
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 3.0)
  return(pic)
  
def blueify(pic):
    
  pixels = getPixels(pic)
  
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 0.05)  
  return(pic)
  
  
def greenify(pic):
    
  pixels = getPixels(pic)
  
  for p in pixels:
    g = getGreen(p)
    setGreen(p, g * 3.0)  
  return(pic)  
  
def purpleify(pic):
    
  pixels = getPixels(pic)
  
  for p in pixels:
    g = getGreen(p)
    setGreen(p, g * 0.015)  
  return(pic) 
