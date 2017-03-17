# Steven Hunt - Logistic Solutions
# CST 205
# March 12 2017

# Lab # 6 - Changing Regions of Pictures

# Warmup - Remove red-eye from chosen pictures.

def redEye():
  pic = makePicture(pickAFile())
  newRed = makeColor(134,7,24)
  newBlue = makeColor(72,80,93)
  for x in range(107,277):
    for y in range (135,190):
       p = getPixel(pic, x, y)
       color = getColor(p)
       if distance(color, newRed) < 80.0:
         setColor(p, newBlue)
  show(pic)
  writePictureTo(pic,"/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 6/redGone.jpg")
      
# PROBLEM 1 - Sepia: Make a picture look old. 

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

def sepia():
    file = pickAFile()
    pic = makePicture(file)
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
    show(pic)
    writePictureTo(pic,"/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 6/sepia.jpg")
    
#Problem 2 - Artify: Artsy Modification
def artify():
    pic = makePicture(pickAFile())
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
    show(pic)
    writePictureTo(pic,"/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 6/artify.jpg")

#Problem 3 - Chromakey : Greenscreen an image. 

def chromakey():
  forground = makePicture(pickAFile())
  background = makePicture(pickAFile())
  newGreen = makeColor(88,222,78)
  for x in range(0 , getWidth(forground)):
    for y in range(0, getHeight(forground)):
      pix = getPixel(forground, x, y)
      newPix = getPixel(background, x, y)
      color = getColor(pix)
      if distance(color, newGreen) < 95.0:
        newColor = getColor(newPix)
        setColor(pix, newColor)
  show(forground)
  writePictureTo(forground,"/home/steven/Desktop/CSUMB Computer Sci Program/Courses/2 - CST 205 : Multimedia and Python/Module 2/Lab 6/greenScreened.jpg")