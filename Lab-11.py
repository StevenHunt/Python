# Logistic Solutions : Steven H., Brenna E., Lupe A.  
# CST 205 - Text-based strategy game 
# Lab #13 - Update game to include a list, input for players name, and use showInformation. 
# 03.30.17


# List to hold door key, antivirus, and screwdriver:  
theList = []

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def play():
 
  introduction()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Introduion: Background to the story.
def introduction(): 
  
  global playerName
  
  playerName = requestString("What is your name: ")
  
  showInformation("  ******************************** WELCOME TO ZOMBIE HOSPITAL ********************************\n"
                  "  **********************************************************************************************************  You were in a tragic car accident and have been in coma for almost a year. "
                  "This is the first time you've opened your eyes, only to realize that you're all alone. You call for help, but no body responds. You eventually get enough strength to get out of bed... ")
                  
  showInformation("The game requires the player to read through the storyline as the game plays out. Throughout your readings, you will find specific words in (parentheses), these words will be "
                  "movements or actions in which you can take by simplying typing them individually into the prompt box. Enjoy. ")
                 
  patientRoom()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Patient Room (STEVEN): Where the player wakes up. 
def patientRoom():
  printNow("************************************************** PATIENT ROOM ************************************************* \n")
  printNow("Location: You're standing just next to your hospital bed in a patient room. \n" +
           "To the left is a (window) that looks down to the parking lot. \n"+
           "Straight ahead is the nurse station, you can (enter) to try and find some help. \n")
  
  global playerName
  
  # Prompts the user to choose action: (enter) nurse station or look out (window).
  command = requestString("Where would you like to go?")
  if command == "enter":
    nurseStation()
    
  elif command == "window":
    patientWindow()

  elif command == "help":
    help()
    patientRoom()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    patientRoom()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Patient Room Window (STEVEN): Where the player can look outside the hospital.          
def patientWindow(): 
  printNow("*************************************** WINDOW IN PATIENT ROOM ************************************************ \n")
  printNow("You walk over and look out the window. As your eyes adjust to the sunlight, you realize the parking lot is littered \n"+
             "with bodies, burning cars, and no life in sight... ")  
  
  printNow("You should probably go search for some help, (enter) the nurse station to try and get some answers \n")
  
  global playerName
  
  # Prompts the user to choose action:(enter) nurse station 
  command = requestString("Where to next?")
  if command == "enter":
    nurseStation()

  elif command == "help":
    help()
    patientRoom()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    patientWindow()
   
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Nurse Station (LUPE): Where the player can encounter a message on a computer.
def nurseStation():
  printNow("************************************************ NURSE STATION *************************************************\n")
  
  printNow("Location: You're entering the nurse station. \n"+
           "You stumble into the nurse station, the lights are dim and flickering off and on, the power seems to be backed by the hospital's generator.\n"+
           "On the desk you see a computer still working, although you can't see the entire message on the screen.\n"+
           "The hospitals west wing is through the (hallway), and the room in which you woke up is (behind) you.\n"+
           "Do you wish to (examine) the message or explore the creepy (note)? \n")
  
  global playerName
  
  # Prompts the user to choose action: (hallway) to west wing, (examine) the computer, or back (behind) to the players starting point.                
  command = requestString("What would you like to do?")
  if command == "hallway":
    westWing()
  
  elif command == "note":
    printNow("You look around the desk and realize theres is a tattered note\n"+
             "next to a picture of a man in a hospital bed. He looked sickly\n"+
             "but magaged to crack a smile though the pain in his eyes was evident.\n"+
             "The glass on the frame is shattered and theres bloody fingerprints \n"
             "along the edges... The note reads:")
    note()
    
  elif command == "examine":
    skull()
        
  elif command == "behind":
    patientRoom()
    
  elif command == "help":
    help()
    nurseStation()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    nurseStation()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Skull (LUPE): A scary message about the hosptial. 
def skull():
  printNow("**************************************************** COMPUTER ****************************************************\n")
  
  comp = makeEmptyPicture(300,300,black)   
  text = makeStyle("Comic Sans",bold,20)
  addTextWithStyle(comp,10,275,'The only way out is through...',text,red)
    
  addOval(comp,55,0,185,185,white) 
  addOvalFilled(comp,95 ,100,105,105, black)
  addOvalFilled(comp,75 , 70, 50, 50, white)
  addOvalFilled(comp,175, 70, 50, 50, white)
  addOvalFilled(comp,95 , 5 ,110,110, black)
  addOvalFilled(comp,160,145, 10, 15, white)
  addOvalFilled(comp,140,145, 10, 15, white)
  addLine(comp, 100, 210, 100, 170,white)
  addLine(comp, 120, 210, 120, 190,white)
  addLine(comp, 140, 210, 140, 190,white)
  addLine(comp, 160, 210, 160, 190,white)
  addLine(comp, 180, 210, 180, 190,white)
  addLine(comp, 200, 210, 200, 170,white)
  addLine(comp, 100, 210, 200, 210,white)
  
  show (comp)
    
  showInformation("The screen turns bright read and dies out...")
  
  nurseStation()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Note (LUPE): Ties story together. 
def note():                 
  comp = makeEmptyPicture(635,180,white)   
  text = makeStyle("serif",plain, 20)
     
  addTextWithStyle(comp,10,40,'Im sorry I could not save you Geoffrey.',text,black)
  addTextWithStyle(comp,10,70,'The only way to help you was to keep you locked away.',text,black)
  addTextWithStyle(comp,10,100,'I did not want you to catch the infection like the rest of us.',text,black)
  addTextWithStyle(comp,10,130,'If you manage to survive and read this I left some supplies in...',text,black)
  printNow("***********Note***********")
  printNow("The note ends with an ink blot smeared across the paper. Suddely you hear\n"+
           "a growling sound from behind you! It's an undead patient in a straitjacket\n"+
           "heading towards you!.\n")
  
  show (comp)
  
  nurseStation()
     
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
     
# West Wing (TEAM): The main west side of the hospital. 
def westWing():
  printNow("************************************************** WEST WING ***************************************************\n")
  printNow("Location: You're just outside of the nursing station in the west-wing of the hospital.\n"+
           "There is a (door) to your left, which leads to a stairway, you could go (back) to the or you could \n"+
	 "go back to the nurse station, or proceed (east) down the dark corridor to the east-wing.\n")
  
  global playerName
  
  # Prompts the user to choose action: (door) to the strairwell or (east) down the corridor.
  command = requestString("Where to next?")
  if command == "door":
    stairDoor()
    return 0
    
  elif command == "east":
    westCorridor()
  
  elif command == "back":
    nurseStation()
  
  elif command == "help":
    help()
    westWing()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    westWing()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Stair Door (TEAM): The 2nd floor stairwell door. 
def stairDoor():
  printNow("************************************************** STAIR DOOR **************************************************\n")
  printNow("Location: You're at a locked door that leads to a stairway.\n"+
           "You can try to (open) the door and head to a different floor, or you can head (back) to \n"+
           "the west-wing and go another route. \n")
  
  global playerName
  
  # Prompts the user to choose action: (open) the door or (back) to main west wing. 
  # The door requires a key. The key is set to false at the beginning of gameplay, but can be triggered globally when found.
  # The key to the stairwell door is located in the operating room (secret room), in the corpse's body. 
  command = requestString("What would you like to do?")
  if command == "open" and 'key' not in theList:
    showInformation("The door is locked.")
    stairDoor()
    
  elif command == "open" and 'key' in theList:
    showInformation("You just unlocked the door... ")
    stairway()
  
  elif command == "back":
    westWing()
    
  elif command == "help":
    help()
    stairDoor()
    
  elif command == "exit":
    printNow("Goodbye " + playerName )
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    stairDoor()  

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Stairway (TEAM): The stairwell from floors 1 to 2. 
def stairway():
  printNow("************************************************** STAIRWELL **************************************************\n")
  printNow("Location: You're on the 2nd story landing in the hospitals stairwell. \n"+
           "The sign in front of you reads '1st floor: Morgue & 3rd floor: Rooftop' The stairway is completely blocked going up.\n"+ 
           "You could possibly (move) the debris, but it would be risky as it's a large pile of chairs and tables.\n"+
           "If you choose to try your luck in the (morgue), you may find a way our down there. You can also go back into the \n"+
           "second floor (hallway).\n")
  
  global playerName
  
  # Prompts the user to choose action:(move) a pile of stuff blocking roof access, (morgue) on the first floor, or back to the (hallway). 
  command = requestString("Where would you like to go?")
  
  if command == "morgue":
    morgue()
    
  # If move is chosen, player will die from collapsing objects knocking him down the stairs and eventually becoming zombie food. 
  elif command == "move":
    printNow("Test test... GAMEOVER")
    return 0
    
  elif command == "hallway":
    stairDoor()
    
  elif command == "help":
    help()
    stairway()
    
  elif command == "exit":
    printNow("Goodbye " + playerName )
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    stairway() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# West Corridor (TEAM): The west end of the hospitals main corridor between the east and west wings. 
def westCorridor():
  printNow("************************************************ WEST-CORRIDOR ************************************************\n")
  printNow("Location: You're in the middle of a long corridor between the different hospital units.. \n"+
           "From here, you can walk (east) towards the east-wing or (back) towards the main west-wing. \n"
           "You are also next to a door labeled 'Operating Room', which you can try to (open): \n")  
  
  global playerName
  
  # Prompts the user to choose action: (open) to try opening shut door, (east) to east corridor, and (west) to the west wing. 
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
    printNow("Goodbye " + playerName )
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    westCorridor() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# East Corridor (TEAM): The east end of the hospitals main corridor between the east and west wings. 
def eastCorridor():
  printNow("************************************************ EAST-CORRIDOR ************************************************\n")
  printNow("Location: You're in the middle of a long corridor between the different hospital units.\n"+
           "It's dark and eerie, and you can't hear much over the sound of the hospital's back up generator. The lights are dim \n"+
           "and flickering, but they give off just enough light to (read) a helpful sign on the wall. \n"+
           "From here, you can walk (east) towards two doorways in the east-wing or (west) by the Operating Room. \n")
  
  global playerName
  
  # Prompts the user to choose action: (read) the emergancy evaction map, (east) to the east wing, or (west) to the west corridor. 
  command = requestString("What would you like to do?")
  
  # If player choses read, a picture of a map of the hosptial will pop up via JES built in functions. 
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
    printNow("Goodbye " + playerName )
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    eastCorridor() 
    

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Map (STEVEN): Map of the hospital / game layout. 
def map():
  printNow("*********************************************** EVACUATION MAP ************************************************\n")
  
  # Creates an empty picture:
  map = makeEmptyPicture(900,600,white)    
  
  # Rooftop:
  addLine(map,150,100,400,100,black) 
  addLine(map,400,100,400,225,black)
  addLine(map,190,225,400,225,black)
  addLine(map,150,100,150,140,black)
  
  # Morgue:
  addLine(map,10,140,155,140,black)
  addLine(map,180,140,190,140,black) 
  addLine(map,10,140,10,275,black)
  addLine(map,10,275,95,275,black)
  addLine(map,125,275,300,275,black)
  addLine(map,190,275,190,135,black)
  addLine(map,190,110,190,100,black)
  
  # stairwell: 
  addLine(map,90,310,265,310,black)
  addLine(map,90,310,90,275,black)
  
  # Nurse Station:
  addLine(map,150,310,150,500,black)
  addLine(map,255,310,255,400,black)
  
  # Patient Room:
  addLine(map,150,500,255,500,black)
  addLine(map,255,500,255,430,black)
  addLine(map,220,440,800,440,black)
  addLine(map,150,440,190,440,black)
  
  
  # Operating Room: 
  addLine(map,300,260,300,400,black)
  addLine(map,300,260,500,260,black)
  addLine(map,300,400,380,400,black)
  addLine(map,420,400,800,400,black)
  addLine(map,500,260,500,400,black)
  addLine(map,500,375,650,375,black)
  
  # Psych Ward:
  addLine(map,650,260,650,400,black)
  addLine(map,650,260,850,260,black)
  addLine(map,850,260,850,580,black)
  
  # Nursery:
  addLine(map,700,440,700,580,black)
  addLine(map,700,580,850,580,black)
  
  # Stairs:
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
  
  # Text:
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
 
  # Display map: 
  show(map)
  
  # Return to east corridor location: 
  eastCorridor()  

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# East Wing (TEAM): The east part of the hospital. 
def eastWing():
  printNow("************************************************** EAST-WING **************************************************\n")
  printNow("Location: You're all the way on the other side of the hospital from where you woke up. Let's hope there is a way out on this side. \n"+
           "There are two sets of large swinging doors. The set on your (right) says  'Nursery' and the set on your (left) says \n"+
           "'Psych Ward'. You can check out either one or head back (west) towards the other wing of the hospital. \n")
  
  global playerName
  
  # Prompts the user to choose action: (left) to psychiatric ward, (right) to child nursery, (west) to go back down the hall. 
  command = requestString("Where to?")
  if command == "left":
    psychWard()
  
  # If player choses right, a message will be displayed with a code to the elvator in the morgue. If the player makes it to the morge without 
  # entering the nursery, they will lose due to getting locked in and being eaten by zombies. 
  elif command == "right":
    showInformation("Just before you open the door, you make out a small blood smear on the wall, you can't quite tell what it says,"+
    "but it looks like it reads 7812, I wonder why that's there... ")
    nursery()   
    
  elif command == "west":
    eastCorridor()
    
  elif command == "help":
    help()
    eastWing()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    eastWing()     
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Psychiatric Ward (BRENNA): The psych ward of the hospital. 
def psychWard():
  printNow("************************************************ PSYCH WARD **************************************************\n")
  printNow("Location:You just entered CAL Hospital's Psychiatric Ward. \n"+
  "You see a shadowy figure huddled down in the corner of the room, he hasn't spotted you yet and he could be dangerous. \n"+
  "It looks as though this unit was under remodel as it's pretty empty, other than a ventilation (duct) and \n"+
  "a random (toolbox), the place is vacant. You can try to engage the mysterious man: Say (hello) or (attack), "+
  "or you could (leave), and head back to the east wing. \n")
   
  global playerName
   
  # Prompts the user to choose action: (duct) will attempt you to crawl through the ventilation unit, (toolbox) will have you open an empty toolbox, (leave) will have you turn around to the east wing, (hello) will 
  # display a message from a man in the room, (attack) will attack the man in the room. 
  command = requestString("What would you like to do?")
   
  # The ventilation duct requires a tool to open. This tool can be retrieved from the drawers in the nursery. 
  if command == "duct" and 'tool' not in theList:
    showInformation("A tool is required to open the vent grate.")
    psychWard()
   
  elif command == "duct" and 'tool' in theList:
    vent()

  elif command == "attack":
    showInformation("The man retaliates, by throwing his shoe at you before retreating to the closet.")
    psychWard()
    
  elif command == "toolbox":
    showInformation("The toolbox is empty")
    psychWard()
   
  elif command == "leave":
    eastWing()  
   
  elif command == "hello":
    showInformation("After exchanging cautious glances, the man introduces himself as Geofery. It is difficult"+
                    "to understand him at times. He rambles on, something about a helicopter...Probably nothing. He excitedly offers "+
                    "you a vile of something and a shot. It's best not to ask questions.")
    theList.append('antivirus')
    printNow("Added: Antivirus")
    psychWard()
  
  elif command == "help":
    help()
    psychWard()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    psychWard()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Nursery (BRENNA): The child nursery of the hospital. 
def nursery():
  printNow("************************************************ NURSERY **************************************************\n")
  printNow("Location:You just entered CAL Hospital's nursery unit. \n"
  "There are rows of empty (cribs) to the right. Infront of you are shelves, scattered with blankets and other \n"+
  "random infant essentials. Behind you is the (doorway) leading to the main part of the east wing. As you enter, you "+
  "hear the sound of an infant crying. \n")
  
  global playerName
    
  # Prompts the user to choose action: (doorway) takes you back to the east wing, inspect (drawers) or insepct the (cribs).
  # If the player chooses pick up without having the antivirus (player loses). 
  # The player must go to the crib and look in the drawers to get the screwdriver in order to get the vent open in the psychward. 
  command = requestString("Where would you like to go?")
  
  if command == "doorway":
    eastWing()
   
  elif command == "cribs":
    command = requestString("In the second crib you find the distressed child. Maybe if you (pick up) the baby he will stop crying."+
    "There might be something in the (drawers) to sooth him.")
   
  if command == "pick up":
    printNow("You pick up the baby and he bites you. You are now infected with the zombie virus!")
   
    if 'antivirus' in theList:
      printNow("Thankfully, you have a vile of the antivirus. You narrowly escaped that one!")
      nursery()
   
    else:
      printNow("Oh no, you are now a brain eating zombie! GAME OVER!")
      return 0
   
  elif command == "drawers":
    showInformation("There doesn't seem to be much there. But you did find a (screwdriver) that may be useful later.")
    theList.append('tool')
    printNow("Added: Screwdriver")
    nursery()
 
  elif command == "help":
    help()
    nursery()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    nursery()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Ventilation Unit (TEAM): The ventilation unit between the psych ward and operating room. (The only way into the operating room). 
def vent():
  printNow("********************************************** VENTILATION UNIT ************************************************\n")
  printNow("Location: In the psych ward, at the entrance to a vent duct, this could be your way out.\n"+
           "You can (unscrew) the vent grate and crawl through, or step (back) into the vacant psychward.\n")
  
  global playerName
  
  # Prompts the user to choose action:(unscrew) to get into the vents, or (back) to the psych ward. 
  command = requestString("What would you like to do?")
  if command == "unscrew":
    operatingRoom()
    
  elif command == "back":
    psychWard()
    
  elif command == "help":
    help()
    vent()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    vent() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Operating Room (STEVEN): The operating room / secret room. 
def operatingRoom():
  printNow("********************************************** OPERATING ROOM ************************************************\n")
  printNow("Location: You just crawled out of the air conditioning vents and into what appears to be an operating room. \n"+
           "You scan the room for threats, once you realize there is no movement, you start looking for a way out.\n"+ 
           "The (door) that leads to the west corridor is jammed, so your only way out is back through the vents.\n"+
           "With only a single way in, it looks like a safe place to recollect yourself and figure a way out.\n"+
           "You walk over to a body laying on the operating table, the lights flicker, and something catches your eye \."+
           "in the dead man's open incision.\n"+
           "You can (inspect) the strang object or head back out through the (vent)...\n") 
           
  global playerName
  
  # Prompts the user to choose action: (inspect) the dead body or go back through the (vents)
  command = requestString("Now what?")
  
  # If player chooses inspect, the key to the stairwell door will be acquired. Key will be triggered from false to true. 
  if command == "inspect":
    theList.append('key')
    printNow("Added: Key")
    showInformation("You slowly peel back the mans scalp. As the lights start flickering faster, you realize what it is "+
    "and reach in to grab a single key.")
    operatingRoom()
    
  elif command == "door":
    showInformation("The door is jammed shut...")
    operatingRoom()
    
  elif command == "vent":
    vent() 
    
  elif command == "help":
    help()
    operatingRoom()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    operatingRoom() 
           
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Morgue (LUPE): Hosptials morgue
def morgue():
  printNow("********************************************** MORGUE ************************************************\n\n"+
           "The room is dark and cold as ice, with a strong smell of chemicals.\n"+
           "There is a wall lined with sliding metal drawers and autopsy tables in the center of the room. There \n"+ 
           "are cadavers on top of the autopsy tables and a on one of the tables catches your eye...\n")

  selection = requestString("Do you wish to examine the bag or continue?\n"
                          "Enter E to examine or C to continue")                       
  global playerName
  
  # Prompts the user to choose action: (E) looks inside a bag and (C) has the player continue to walk around the morgue. 
  selection= selection.upper()
  
  if selection == ("E"):
    printNow("Inside the bag are various surgical instruments, scalpels, carankclamps, and at the very bottom there is \n"+
             "a mysterious lever labeled 'Elevators Deadmans Crank'...\n"+
             "Wait.. theres an elevator? You quickly scan the room and notice at the far corner\n"+
             "amidst the darkness an old-fashioned birdcage elevator. You proceed towards the elevator with\n"+ 
             "the lever and connect it to the control. The doors creak open...\n")
    elevator()   
              
             
  elif selection == ("C"):
    printNow("You continue walking cautiously through the room and as you make your way around the cadavers \n"+ 
             "you hear a harsh rumbling sound coming from the corner of the room. From the darkness emerges an\n"+
             "infected coroner covered in old black rotten blood. You see a crack of light coming from the stairwell \n"+
             "behind him and make a run for it... \n")
    stairway()
    
  elif command == "help":
    help()
    morgue()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    morgue() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Elevator (TEAM): The player must make it onto the elevator and type in the security code before the zombie coroner gets him. 
def elevator():
  printNow("************************************************ ELEVATOR ***************************************************\n")
  printNow("Location: You step into the elevator and you see the 'rooftop' button. As you take a long deep breath,\n"+
  "you see this shadowy figure coming from out of the stair well and straight towards you...")
  
  global playerName
  
  command = requestString("Press (up) button: ")
  
  if command == "up":
    printNow("The elevator starts to beep... You expect the doors to be closing, but they aren't.")
    printNow("The little screen flashes 'security code invalid: * * * *' \n"+
             "You start to panic, and your mind starts going back through everything you saw while roaming the hospital... \n"+
             "That's right, you saw a 4 digit code near the nursery, it was 7 ......8.......")
    
    code = requestString("Security Code: __ __ __ __" )
    
    if code == "7812":
      roofTop()
      
    elif code != "7812":
      printNow("Wrong Code! The zombie coroner attacked you! GAME OVER!" )
      return 0
    
  elif command == "help":
    help()
    elevator()
    
  elif command == "exit":
    printNow("Goodbye " + playerName)
    return 0
    
  elif command != "help" and command != "exit":
    printNow("I did not understand that command.")
    elevator() 
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Rooftop: Where the patient is rescued. 
def roofTop(): 
  printNow("************************************************ ROOFTOP ***************************************************\n")
  showInformation("As the elevator slows down, you see the sun's rays piercing through the crack of the doors. \n"+
                  "You step out onto the concrete rooftop and drop to your knees as search and rescue helicopters \n"+
                  "circle above you!")
  return 0
  
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Help: Can be called at any time. 
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
        
