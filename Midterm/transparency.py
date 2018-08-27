# Steven Hunt - Logistic Solutions (Individual)
# CST 205 - Midterm Project
# 3.24.2017

# ********************** README *********************************

# An image filter that applies a transparent overlay of the iconic jellyfish from California's Monterey Bay Aquarium.

# DOWNLOAD AND SAVE TO YOUR LOCAL DRIVE BEFORE RUNNING FUNCTION:
# Jelly.jpg: https://drive.google.com/a/csumb.edu/file/d/0BzXx24QKHVk4V1NxbEwyMXU3Wjg/view?usp=sharing
# CSUMB.jpg: https://drive.google.com/a/csumb.edu/file/d/0BzXx24QKHVk4RTZVSDlIdWNycjA/view?usp=sharing

# The function first prompts the user for any picture they to apply filter(see image boundries). It then prompts the user to locate and choose the Jelly.jpg and CSUMB.jpg images downloaded from my Google Drive. 
# It then applies some modifications to lighten the image up and create an artistic effect to it. The image is then passed through the transparency function in which the pixel values change and the jellyfish
# image is "overlayed" ontop. CSUMB's school colors are then applied as a 20px border around the image. The function then uses chromakey to "greenscree" the logo onto the final image. 
# Lastly, the function prompts the use to choose a folder and filename in which to save the filtered image (see instructions on saving).  

# LOAD / RUN: Simply call the CSUMBY() function from the command line. 

# SAVING: When prompted, choose a folder in which to save the filtered image. The function will then prompt user to input a file name (DO NOT ADD EXTENSION, IT APPLIES .jpg AS EXTENSION). 

# IMAGE BOUNDRIES: I made this function scalable to take an image up to (3500 x 2200) due to the background image and no smaller than (275 x 86) due to the logo's size. 

# ****************************************************************

def csumby():
  
  # Prompts the user to choose an image of their choice as the background image (No larger than 3500 x 2200) 
  showInformation("Please choose an image no larger than (3500 x 2200) and no smaller than (275 x 86)")
  picture = makePicture(pickAFile())
  
  # Prompts user to choose the jellyfish background image saved on their local drive. 
  showInformation("Open Jelly.jpg downloaded from Google Drive.")
  transparentPic = makePicture(pickAFile())
  
  # Promps user to choose the CSUMB logo image saved on their local drive. 
  showInformation("Open CSUMB.jpg downloaded from Google Drive.")
  logo = makePicture(pickAFile())
  
  # Image modifications before adding the transparent overlay: 
  lightenUp(artify(picture))

  # Calling transparency:
  background =  transparency(picture, transparentPic)
  
  # Width and Height of picture:    
  w,h = getWidth(background),getHeight(background)
  
  # CSUMB Colored Border: 
  addRectFilled(background,20,0,w,20,blue)      # Top
  addRectFilled(background,w-20,20,20,h,green)  # Right
  addRectFilled(background,0,h-20,w-20,20,blue) # Bottom 
  addRectFilled(background,0,0,20,h-20,green)   # Left
  
  # CSUMB Logo:
  lightenUp(artify(logo))
  x = w/2-137
  y = h-160
  canvas = makeEmptyPicture(w,h,red)
  foreground = copyInto(logo,canvas,x,y) 
  
  # Calling chromakey to apply CSUMB logo at the bottle / middle of the image: 
  filtered = chromakey(foreground,background)
  
  show(filtered)
  
  folder = pickAFolder()
  file = requestString("Please enter filename you wish to save filtered image as:")
  path = folder + file + ".jpg"
  writePictureTo(filtered,path)
  
# Creates transparent overlay from the two images:
def transparency(picture, transparentPic):

  # Create a new image with the same width and height of picture. 
  w,h = getWidth(picture),getHeight(picture)
  canvas = makeEmptyPicture(w,h)

  # Iterate through all pixels:
  for x in range(0, w):
    for y in range(0, h):
 
      # Get all the pixels:
      picPx = getPixel(picture, x, y)
      tranPx = getPixel(transparentPic, x, y)

      # Get color values:
      picRed = getRed(picPx)
      tranRed = getRed(tranPx)
      picGreen = getGreen(picPx)
      tranGreen = getGreen(tranPx)
      picBlue = getBlue(picPx)
      tranBlue = getBlue(tranPx)
    
      # Darken pixel values: 
      newR = picRed - (255 - tranRed)
      newG = picGreen - (255 - tranGreen)
      newB = picBlue - (255 - tranBlue)

      # Creates new color and assigns them to pixels on canvas. 
      newColor = makeColor(newR,newG,newB)
      px = getPixel(canvas, x, y)      
      setColor(px, newColor)
  return canvas

# Lightens up the image, using the built in JES function makeLighter:
def lightenUp(pic): 

  px = getPixels(pic)
  for p in px:
    c = getColor(p)
    c = makeLighter(c)
    setColor(p,c)
  return(pic)
  
  
# Creates an artistic effect to the background image: 
def artify(pic):

  # Iterates through and gets all the pixels of pic
  w,h = getWidth(pic), getHeight(pic)
  for x in range(0,w):
    for y in range(0,h):
      p = getPixel(pic, x, y)
            
      # Gets the original pixel values of red and adjusts them to specifications. 
      r = getRed(p)
      if r < 64:
        setRed(p, 31)
      elif r < 128:
        setRed(p, 95)
      elif r < 192:
        setRed(p, 159)
      else:
        setRed(p, 223)
      
      # Gets the original pixel values of green and adjusts them to specifications.      
      g = getGreen(p)
      if g < 64:
        setGreen(p, 31)
      elif g < 128:
        setGreen(p, 95)
      elif g < 192:
        setGreen(p, 159)
      else:
        setGreen(p, 223)
      
      # Gets the original pixel values of blue and adjusts them to specifications.
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
  
# Uses the greenscreen concept to apply the CSUMB logo onto the filtered image:  
def chromakey(target,background):
  w,h = getWidth(target),getHeight(target)
  newRed = makeColor(255,0,0)
  for x in range(0 ,w):
    for y in range(0, h):
      pix = getPixel(target, x, y)
      newPix = getPixel(background, x, y)
      color = getColor(pix)
      if distance(color, newRed) < 95.0:
        newColor = getColor(newPix)
        setColor(pix, newColor)
  return target

# *******************************************************
