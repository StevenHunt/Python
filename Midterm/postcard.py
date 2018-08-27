# Steven Hunt - Logistic Solutions (Individual)
# CST 205 - Midterm Project
# 3.23.2017


# ***************************** README **************************************

# Image Specifications for filter:

# Part -------------- Width ----x---- Height -------------------------------- 

# CS                   133              62       
# UM                   268             324   
# B                    160             378    

# CSUMB                588             395  

#----------------------------------------------------------------------------

# DOWNLOAD AND SAVE TO YOUR LOCAL DRIVE BEFORE RUNNING FUNCTION: 
# FortOrd.jpg: https://drive.google.com/a/csumb.edu/file/d/0BzXx24QKHVk4aEFpa203Q05tUFU/view?usp=sharing
# Template.jpg: https://drive.google.com/a/csumb.edu/file/d/0BzXx24QKHVk4M2xpeFhqeWlxWGc/view?usp=sharing
# CSUMB.jpg: https://drive.google.com/a/csumb.edu/file/d/0BzXx24QKHVk4M1NlMGZ5WEpUV0E/view?usp=sharing

# Error: You will recieve an error if you do not comment out one of the sections below...
# Section A: Allows uer to choose 1 image as a filler for C S U M B
# Section B: Allows user to choose 3 specific images to use as a filler for CS - UM - B respectively. 

# LOAD / RUN: Simply call postcard() from the command line. 

# SAVING: When prompted, choose a folder in which to save the filtered image. The function will then prompt user to input a file name (DO NOT ADD EXTENSION, IT 
# APPLIES .jpg AS EXTENSION FOR YOU). 

# **************************************************************************

# Main function:  
def postcard():

  # Prompts user to load specific images downloaded from Google Drive: 
  showInformation("Please load FortOrd.jpg:")
  target = makePicture(pickAFile()) 
  
  showInformation("Please load Template.jpg:")     
  cardTemplate = makePicture(pickAFile())
  
  showInformation("Please load CSUMB.jpg:")  
  CSUMB = makePicture(pickAFile())
                  
  # Main image placement and modifications: 
  FortOrd = vignette(target) 
  pyCopy(artify(FortOrd),target,0,0)
  redCopy(CSUMB,target,0,0)
  redCopy(cardTemplate,target,0,0)
    
  # Fillers: 
  Filler = makeEmptyPicture(960,650)
  
  # **** SECTION A: Apply a single image to C S U M B **************************
  showInformation("Please load a .jpg file with size (588 x 395):")
  Image = makePicture(pickAFile())
 
   # Calls pyCopy to copy user selected image of size (588 x 395) into location (146,130)
  pyCopy(artify(Image),Filler,146,130)
  # ****************************************************************************
  
  
  """ *** SECTION B: Apply Images to CS - UM - B Individually ****************** 
  #Propts user to choose 3 images based on specific specifications to use for fillers for CS - UM - B respectively. 
  showInformation("Please load a .jpg file with size (133 x 62):")
  CS = makePicture(pickAFile())
  showInformation("Please load a .jpg file with size (268 x 324):")
  UM = makePicture(pickAFile())
  showInformation("Please load a .jpg file with size (160 x 378):")
  B = makePicture(pickAFile())
  
  # Calls pyCopy
  pyCopy(artify(CS),Filler,147,256)
  pyCopy(artify(UM),Filler,282,156)
  pyCopy(artify(B),Filler,582,140)
  ****************************************************************************"""
  
  # Chromakey to apply images as fill:
  Postcard = chromakey(target,Filler)
  
  # Save:
  folder = pickAFolder()
  file = requestString("Please enter filename you wish to save filtered image as:")
  path = folder + file + ".jpg"
  writePictureTo(Postcard,path)
 
 
# Green screen function: Takes the background parameter and fills in the target parameter wherever there is the specified green pixels.     
def chromakey(target,background):
  w,h = getWidth(target),getHeight(target)
  newGreen = makeColor(25,255,0)
  for x in range(0 ,w):
    for y in range(0, h):
      pix = getPixel(target, x, y)
      newPix = getPixel(background, x, y)
      color = getColor(pix)
      if distance(color, newGreen) < 95.0:
        newColor = getColor(newPix)
        setColor(pix, newColor)
  return target
           
def redCopy(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     if distance(color, red) > 50.0:
       setColor(getPixel(target, targetX+x, targetY+y), color)

def pyCopy(source, target, targetX, targetY):
  w, h = getWidth(source), getHeight(source)
  for x in range(0, w): 
    for y in range(0, h): 
     color = getColor(getPixel(source, x, y))
     setColor(getPixel(target, targetX+x, targetY+y), color)

# Creates an artistic effect to the background image:           
def artify(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0 , getHeight(pic)):
      p = getPixel(pic, x, y)
            
      r = getRed(p)
      if r < 64:
        setRed(p, 31)
      elif r < 128:
        setRed(p, 95)
      elif r < 192:
        setRed(p, 159)
      else:
        setRed(p, 223)
            
      g = getGreen(p)
      if g < 64:
        setGreen(p, 31)
      elif g < 128:
        setGreen(p, 95)
      elif g < 192:
        setGreen(p, 159)
      else:
        setGreen(p, 223)
                
      b = getBlue(p)
      if b < 64:
        setBlue(p, 31)
      elif b < 128:
        setBlue(p, 95)
      elif b < 192:
        setBlue(p, 159)
      else:
        setBlue(p, 223)            
  return(pic)
    
# Used for FortOrd image to make it look aged:
def vignette(pic):
  w,h = getWidth(pic), getHeight(pic)
  for x in range(0, w):
    for y in range(0, h):
      picPixel = getPixel(pic, x, y)
      
      picRed = getRed(picPixel)
      picGreen = getGreen(picPixel)
      picBlue = getBlue(picPixel)

      newR = picRed - (255 - picRed)
      newG = picGreen - (255 - picGreen)
      newB = picBlue - (255 - picBlue)
      
      newC = makeColor(newR, newG, newB)
      
      px = getPixel(pic, x, y)              
      setColor(px, newC)
  return pic

  
