# Logistic Solutions : Steven H.,Brenna E., Lupe A. 
# CST 205 - Text-based strategy game 
# Lab #11
# 03.30.17


# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def play():


  introduction()
  patientRoom()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def introduction(): 
  printNow("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n********************************************************************************************************************")
  printNow("************************************** WELCOME TO ZOMBIE HOSPITAL *******************************************")
  printNow("******************************************************************************************************************** \n \n"+
           "You were in a tragic car accident and have been in a coma for almost a year. \n"+
           "This is the first time you've opened your eyes, only to realize that you're alone in this strange room. \n"+
           "You try and call for help, but no body responds. You eventually get enough strength to get out of bed... \n") 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def patientRoom():
  printNow("************************************************** PATIENT ROOM ************************************************* \n")
  printNow("Location: You're standing just next to your hospital bed in a patient room. \n" +
           "To the left is a (window) that looks down to the parking lot. \n"+
           "Straight ahead is the nurse station, you can (enter) to try and find some help. \n")
  
  command = requestString("Where would you like to go?")
  if command == "enter":
    nurseStation()
    return 0
    
  elif command == "window":
    patientWindow()
    return 0

  elif command == "help":
    help()
    patientRoom()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    patientRoom()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
     
def patientWindow(): 
  printNow("*************************************** WINDOW IN PATIENT ROOM ************************************************ \n")
  printNow("You walk over and look out the window. As your eyes adjust to the sunlight, you realize the parking lot is littered \n"+
             "with bodies, burning cars, and no life in sight... ")  
  
  printNow("You should probably go search for some help, (enter) the nurse station to try and get some answers \n")
  
  command = requestString("Where to next?")
  if command == "enter":
    nurseStation()
    return 0

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def nurseStation():
  printNow("************************************************ NURSE STATION *************************************************\n")
  
  printNow("Location: You're standing near a desk to what appears to be the nurse station. \n"
           "The lights are dim and flickering off and on. You approach the desk in hopes of speaking with a nurse, but \n"+
           "all you see is an empty chair and a computer. There's a (message) on the cracked computer screen you can partially make out. \n"+
           "To the right is the (main) west-wing of the hospital which looks like it could lead to a way out and (behind) you \n"+
           "is the room in which you woke up in. \n")
  
  command = requestString("What would you like to do?")
  if command == "main":
    westWing()
    return 0

  elif command == "message":
    computer()
    
  elif command == "behind":
    patientRoom()
    return 0
    
  elif command == "help":
    help()
    patientRoom()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    nurseStation()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def computer():
    printNow("**************************************************** COMPUTER ****************************************************\n")
    
    printNow("On the screen is a message that says: \n" +
             "On March 15th 2017, CAL Hospital experienced a viral outbreak of an unknown virus. \n"+
             "The building has been quarantined, move with caution and stay alert, help is on the way.\n")
    
    computer = makeEmptyPicture(300, 300,black)   
    text = makeStyle("Comic Sans", bold, 20)
    addTextWithStyle(computer, 10, 230, 'The only way out is through...', text, red)  

    text = makeStyle("Comic Sans", bold, 20)
    text1 = makeStyle("Comic Sans", bold, 10)
    addOvalFilled(computer, 75, 50, 50, 50, gray)
    addOvalFilled(computer, 175, 50, 50, 50, gray)
    addOvalFilled(computer, 160, 125, 10, 15, gray)
    addOvalFilled(computer, 140, 125, 10, 15, gray)
    addLine(computer, 100, 180, 100, 160,gray)
    addLine(computer, 120, 180, 120, 160,gray)
    addLine(computer, 140, 180, 140, 160,gray)
    addLine(computer, 160, 180, 160, 160,gray)
    addLine(computer, 180, 180, 1890, 160,gray)
    addLine(computer, 200, 180, 0200, 160,gray)
    addLine(computer, 80, 170, 230, 170,gray)
    show (computer)
    
    nurseStation()
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def westWing():
  printNow("************************************************** WEST WING ***************************************************\n")
  printNow("Location: You're just outside of the nursing station, in the west-wing of the hospital. \n"+
           "There is a (door) to your left, which leads to a stairway, you can go (back) to the nurse station, \n"+
           " or you could proceed (east) down the dark corridor to the east-wing. \n")
  
  command = requestString("Where to next?")
  if command == "door":
    stairDoor()
    return 0
    
  elif command == "east":
    westCorridor()
    return 0
    
  elif command == "back":
    nurseStation()
    return 0
  
  elif command == "help":
    help()
    westWing()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    westWing()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def stairDoor():
  printNow("************************************************** STAIR DOOR **************************************************\n")
  printNow("Location: You're at at locked door that leads to a stairway. \n"+
           "You can try to (open) the door and head to a different floor, or you can head (back) to \n"+
           "the west-wing and go another route. \n")
  
  command = requestString("What would you like to do?")
  
  unlock = false
  
  if command == "open" and unlock == true:
    stairway()
    return 0
  
  elif command == "open" and unlock == false:
    showInformation("The door is locked.")
    stairDoor()
    return 0
    
  elif command == "back":
    westWing()
    return 0
    
  elif command == "help":
    help()
    stairDoor()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    stairDoor()  

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def stairway():
  printNow("************************************************** STAIRWELL **************************************************\n")
  printNow("Location: You're on the 2nd story landing in the hospitals stairwell. \n"+
           "The sign in front of you reads '1st floor: Morgue & 3rd floor: Rooftop' The stairway is completely blocked going up.\n"+ 
           "You could possibly (move) the debris, but it would be risky as it's a large pile of chairs and tables."+
           "If you choose to try your luck in the (morgue), you may find a way our down there. You can also go back into the \n"+
           "second floor (hallway).\n")
  
  if command == "move":
    printNow("A table broke loose from the pile and knocked you down the stairs. You split your head open and was \n"+
             "attacked and eaten by a hungry zombie. GAME OVER!")
    return 100
  
  elif command == "morgue":
    printNow("Morgue")
    #morgue()
    
  elif command == "hallway":
    stairDoor()
    return 0
    
  elif command == "help":
    help()
    stairway()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    stairway() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def westCorridor():
  printNow("************************************************ WEST-CORRIDOR ************************************************\n")
  printNow("Location: You're in the middle of a long corridor between the different hospital units.. \n"+
           "From here, you can walk (east) towards the east-wing or (back) towards the main west-wing. \n"
           "You are also next to a door labeled 'Operating Room', which you can (open): \n")  
  
  command = requestString("What would you like to do?")
  
  if command == "open":
    showInformation("The door is locked, try and find another way in...")
    westCorridor()
  
  elif command == "east":
    eastCorridor()
    
  elif command == "west":
    westWing()
    
  elif command == "help":
    help()
    westCorridor()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    westCorridor() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def eastCorridor():
  printNow("************************************************ EAST-CORRIDOR ************************************************\n")
  printNow("Location: You're in the middle of a long corridor between the different hospital units. \n"+
           "It's dark and eerie, and you can't hear much over the sound of the hospital's back up generator. The lights are dim \n"+
           "and flickering, but they give off just enough light to (read) a helpful sign on the wall. \n"+
           "From here, you can walk (east) towards two open doorways in the east-wing or (west) by the Operating Room. \n")
  
  command = requestString("What would you like to do?")
  if command == "read":
    map()
    
  elif command == "east":
    eastWing()
  
  elif command == "west":
    westCorridor()
    
    
  elif command == "help":
    help()
    eastCorridor()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    eastCorridor() 
    

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def map():
  printNow("*********************************************** EVACUATION MAP ************************************************\n")
  
  map = makeEmptyPicture(900,600,white)    
  
  #Rooftop:
  addLine(map,150,100,400,100,black) 
  addLine(map,400,100,400,225,black)
  addLine(map,190,225,400,225,black)
  addLine(map,150,100,150,140,black)
  
  #Morgue:
  addLine(map,10,140,155,140,black)
  addLine(map,180,140,190,140,black) 
  addLine(map,10,140,10,275,black)
  addLine(map,10,275,95,275,black)
  addLine(map,125,275,300,275,black)
  addLine(map,190,275,190,135,black)
  addLine(map,190,110,190,100,black)
  
  #stairwell: 
  addLine(map,90,310,265,310,black)
  addLine(map,90,310,90,275,black)
  
  #Nurse Station:
  addLine(map,150,310,150,500,black)
  addLine(map,255,310,255,400,black)
  
  #Patient Room:
  addLine(map,150,500,255,500,black)
  addLine(map,255,500,255,430,black)
  addLine(map,220,440,800,440,black)
  addLine(map,150,440,190,440,black)
  
  
  #Operating Room: 
  addLine(map,300,260,300,400,black)
  addLine(map,300,260,500,260,black)
  addLine(map,300,400,380,400,black)
  addLine(map,420,400,800,400,black)
  addLine(map,500,260,500,400,black)
  addLine(map,500,375,650,375,black)
  
  #Psych Ward:
  addLine(map,650,260,650,400,black)
  addLine(map,650,260,850,260,black)
  addLine(map,850,260,850,580,black)
  
  #Nursery:
  addLine(map,700,440,700,580,black)
  addLine(map,700,580,850,580,black)
  
  #Stairs:
  addLine(map,135,275,135,310,black)
  addLine(map,145,275,145,310,black)
  addLine(map,155,275,155,310,black)
  addLine(map,165,275,165,310,black)
  addLine(map,175,275,175,310,black)
  addLine(map,185,275,185,310,black)
  addLine(map,195,275,195,310,black)
  addLine(map,205, 275,205,310,black)
  addLine(map,215,275,215,310,black)
  addLine(map,225,275,225,310,black)
  addLine(map,235,275,235,310,black)
  addLine(map,245,275,245,310,black)
  
  
  #Text:
  text1 = makeStyle("Comic Sans", bold, 12) 
  addTextWithStyle(map, 500, 422, 'YOU ARE HERE.', text1, red)
  
  text2 = makeStyle("Comic Sans", bold,9)
  addTextWithStyle(map,222,115, 'Roof Top (Helicopter Pad)', text2, black)
  addTextWithStyle(map,65,215,'Morgue', text2, black)
  addTextWithStyle(map,160,472,'Patient Rooms', text2, black)
  addTextWithStyle(map,160,382,'Nurse \n Station', text2, black)
  addTextWithStyle(map,350 ,326 ,'Operating Room', text2, black)
  addTextWithStyle(map, 707,326 ,'Psych Ward', text2, black)
  addTextWithStyle(map,750,515 ,'Nursery', text2, black)
  addTextWithStyle(map,158,125 ,'Elevator', text2, black)
  
  text3 = makeStyle("Comic Sans",bold,40)
  addTextWithStyle(map,270,180,'H',text3,black)
  addOval(map,262,140,50,50,black)
 
  show(map)
  
  eastCorridor()  

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def eastWing():
  printNow("************************************************** EAST-WING **************************************************\n")
  printNow("Location: You're all the way on the other side of the hospital from where you woke up. Let's hope there is a way out on this side. \n"+
           "There are two sets of large swinging doors. The set on your (right) says  'Nursery' and the set on your (left) says \n"+
           "'Psych Ward'. You can check out either one or head back (west) towards the other wing of the hospital. \n")
  
  command = requestString("Where to?")
  if command == "left":
    psychWard()
  
  elif command == "right":
    nursery()   
    
  elif command == "help":
    help()
    eastWing()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    eastWing()     
            

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def psychWard():
  printNow("************************************************** PSYCH WARD **************************************************\n")
  printNow("Location:You just entered CAL Hospital's Psychiatric Ward. \n"+
           "You see a shadowy figure huddled down in the corner of the room, he hasn't spotted you yet so you have some options. \n"+
           "It looks as though this unit was under remodel as it's pretty empty, other than a ventilation duct and \n"+
           "a random (toolbox), the place is vacant. You can try to engage the mysterious man: (talk) or (attack), "+
           "or you can head back out into the (main) east wing. \n")
  
  if command == "toolbox":
    showInformation("The toolbox is empty")
    psychWard()
  
  elif command == "main":
    eastWing()  
    
  elif command == "talk":
    showInformation("The man's name is Geofery. He tells you that a helicopter will be arriving on the roof to rescue anyone who remains...")
    psychWard()
  
  elif command == "attack":
    showInformation("The man retaliates by attacking you with a screw driver. You wrestle the screw driver away and flee the room and run down the corridor.")
    tool = "true"
    westCorridor()
      
  elif command == "help":
    help()
    psychWard()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    psychWard() 
    

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def nursery():
  printNow("************************************************** NURSERY **************************************************\n")
  printNow("Location:You just entered CAL Hospital's nursery unit. \n"
           "There are rows of empty (cribs) to the right. Infront of you are (shelves), scattered with blankets and other \n"+
           "random infant essentials. Behind you is the (doorway) leading to the main east wing. \n")
  
  command = requestString("Where would you like to go?")
  if command == "doorway":
    eastWing()
  
  elif command == "shelves":
    showInformation("Nothing but linens here...")
    nursery()
    
  elif command == "cribs":
    showInformation("It looks like one of the mattresses is out of place")  
    nursery()
    
  elif command == "help":
    help()
    nursery()
    
  elif command == "exit":
    printNow("Goodbye")
    return 100
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    nursery() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def help():
  
  printNow("******************************************************* HELP *******************************************************\n")
  showInformation("STORY: As you awake from a year long coma, you realize the hospital you've been staying at has been abandoned"+
                  " due to a virus outbreak which started here at the hospital a week earlier. \n \n"+
                  "SOLANUM VIRUS: The virus travels through your bloodstream, from the initial point of entry, into the brain."+
                  " The virus ceases all bodily functions and mutates the brain into an organ that doesn't need oxygen. Once you've been"+
                  " infected, you only have a few hours before you turn. You will no longer have any thoughts or feelings, the body becomes"+
                  " a host for a blood thirsty, flesh eating being. \n \n"
                  "STRATEGY: You want to navigate through the hospital and try to escape alive."+
                  " You woke up in a 2nd floor patient room, your best chance to escape is to somehow get outside,"+
                  " try to make it to the ground floor or the rooftop to signal help.")  

  return 1
        
