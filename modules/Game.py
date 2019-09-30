#This python file is going to serve as the implementation of game data and logic and the interactivity with the user.
#Imported Modules including random, Warrior, Wizard
import random
import Warrior
import Wizard
#This GameMenu() method represents the introduction of the game, asking for users name and creating the Role object (Warrior and Wizard)
def GameMenu():
    Introduction = 'Welcome to the World of Sheridan.' + '\n' + '\n' + 'The school has been infested with teachers that sleep,' + '\n' + 'when they teach and we want to get rid of them by the time the summer ends.' + '\n'
    print(Introduction)
    Name = input('Before we begin what is your name? ' + '\n')
    NameCap = Name.capitalize()
    AskRoleConfirmation = ''
    Introduction = '\n' + f'Well {NameCap}, you have just entered the school and you see this problem,' 
    print(Introduction)
    #If the user input is the warrior then assign them the role of "Warrior" from the warrior module
    #Loop until the user has confirmed their choice if they end up saying no keep asking them what their role may be 
    while(AskRoleConfirmation.lower() != 'y' and AskRoleConfirmation.lower() != 'yes'):
        #When user input equals the role create an object of Warrior or Wizard accordingly to the user input
        AskRole = input('The dean gives you two options: ' + '\n' +  'Warrior or Wizard, in order to wake up these bad teachers. ')
        if (AskRole.lower() == 'warrior'):
            Character = Warrior.Warrior(NameCap)
            AskRoleConfirmation = input('Are you sure you would like to choose ' + Character.__class__.__name__ + ' (Y/N)?')
        elif(AskRole.lower() == 'wizard'):
            Character = Wizard.Wizard(NameCap)
            AskRoleConfirmation = input('Are you sure you would like to choose ' + Character.__class__.__name__ + ' (Y/N)?')
        #Once the role is assigned give the first challenge to the user
    resultFirstChallenge = firstChallenge(Character)
    #The first challenge will give a string that will result whether or not the user has loss or won, then make, the object adjustments on the member variables
    #If the firstChallege output is a, then the user critically lost, -1 from stats and -1 vitality which decreases health
    #Permuations of challenges shall report them to the next challenges ABCD, ABDC, ACBD, ACDB, ADBC, ADCB,
                                                                        #BACD, BADC, BCAD, BCDA, BDAC, BDCA,
                                                                        #CABD, CADB, CBAD, CBDA, CDAB, CDBA,
                                                                        #DABC, DACB, DBAC, DBCA, DCAB, DCBA
    if(resultFirstChallenge == 'a'):
        loss = Character.criticalLoss()
        print(str(loss))
        secondResultOutcome = secondChallenge(Character)
        if(secondResultOutcome == 'a'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'b'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'c'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'd'):
            thirdChallenge(Character)
    elif(resultFirstChallenge == 'b'):
        secondResultOutcome = secondChallenge(Character)
        if(secondResultOutcome == 'a'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'b'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'c'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'd'):
            thirdChallenge(Character)
    elif(resultFirstChallenge == 'c'):
        secondResultOutcome = secondChallenge(Character)
        if(secondResultOutcome == 'a'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'b'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'c'):
            thirdChallenge(Character)
        elif(secondResultOutcome == 'd'):
            thirdChallenge(Character)
    #If the firstChallege output is d, then the user critically won, +1 from stats and +1 vitality which increases health
    elif(resultFirstChallenge == 'd'):
        #TODO: figure out how to change attributes for Wizard when they win
        win = Character.criticalWin()
        print(str(win))
        resultOutcome = secondChallenge(Character)
        if(resultOutcome == 'd'):
            thirdChallenge(Character)
#This method will be the first challenge of entering  a room into 
def firstChallenge(Role):
    #Decision can be a bush (5 bandages), school directory(map), door(locked, unlock), Sheridan Sign (firstKey)
    textLocation = ''
    firstKey = False
    resultOutcome = ''
    lockUnlocked = False
    textQuestLine = '\n' + 'The dean has assigned you the ' + Role.__class__.__name__ + ' role and has given you the powers' + '\n' + 'to wake these teachers up.' + '\n' + '\n' + 'The dean has asked you to figure out a way to get inside of the campus because the teachers have lock the doors from the inside.' + '\n'
    print(textQuestLine)
    questInput = input('Do you accept the quest?(Y/N)')
    if(str(questInput) == 'y' or str(questInput) == 'yes'):
        try:
            while(lockUnlocked != True):
                decision = input('\n' + 'There are four spots to check in the front of the school and are as listed (E to check bag, F for Character Statistics):' + '\n' +
                'A: Stairs' + '\n' +
                'B: School Directory' + '\n' +
                'C: Door' + '\n' +
                'D: Sheridan School Sign' + '\n' +
                'Your choice: ')
                if(decision.lower() == 'a' or decision.lower() == 'bush'):
                    #behind the bush is a note that says in order to enter the school, check the door
                    textLocation = 'You find a note, you pick it up and read it reads:' +'\n' + 'Check the main entrance of the school(door)'
                    print(textLocation)
                elif(decision.lower() == 'b' or decision.lower() == 'directory'):
                    #you check the school directory and see where the different spots are in the school, you put the map in your backpack
                    item = 'Map'
                    textLocation = 'You find a map'
                    print(textLocation)
                    pickUp = ''
                    while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                        pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')   
                        #Figure out how to get out of the loop once the Map is equippe and appended to the itemBackpack
                        if(pickUp.lower() == 'y' or pickUp.lower() == 'yes' and 'Map' not in Role.itemBackpack): 
                            Role.itemBackpack.append(item)
                            print("You have now equipped the map...")
                        elif(decision.lower() == 'y' or pickUp.lower() == 'yes' and 'Map' in Role.itemBackpack):
                            print("There is nothing to found here anymore")
                        elif(pickUp.lower() == 'n' or pickUp.lower() == 'no'):
                            print("Back to the entrance")
                elif(decision.lower() == 'c' or decision.lower() == 'door'):
                    if(firstKey == False):
                        textLocation = 'There is a lock on the door and you see that the door is locked' +'\n' + '...it seems like it can be locked by an item in your backpack'
                        print(textLocation)
                    elif(firstKey == True):
                        textLocation = 'There is a lock on the door and you see that the door is locked' + '\n' + 'it seems like your firstKey fits it ' + '\n' + '...' + '\n' + 'Door is now unlocked!' + '\n' + '\n' + 'You have now entered the campus. ' + '\n'
                        #The result outcome is equal to the dice roll from gamePlay()
                        print(textLocation)
                        resultOutcome = gamePlay()
                        lockUnlocked = True
                elif(decision.lower() == 'd' or decision.lower() == 'sign'):
                    item = 'firstKey'
                    textLocation = 'You check the sign and notice a ' + item
                    print(textLocation)
                    pickUp = ''
                    while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                        pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')
                        if (pickUp.lower() == 'y' or pickUp.lower() == 'yes'):
                            Role.itemBackpack.append(item)                        
                            print("You have now equipped the firstKey...")
                            firstKey = True
                        elif pickUp.lower() == 'no' or pickUp.lower() == 'n':
                            print("Back to the entrance")
                elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                    if not (Role.itemBackpack):
                        print ("Your bag is empty")
                    else:
                        print(*Role.itemBackpack, sep = "\n") 
                #Find out why it gets here when the power is turned on, escape while loop before this vv         
                elif(decision.lower() == 'f' or 'stats'):
                    print(Role.Stats())                 
            return resultOutcome
        except:
            print('An error has occured')
def secondChallenge(Role):
    textLocation = ''
    mapChecked = False
    powerOn = False
    resultOutcome = ''
    textQuestLine = '\n' + 'You are now inside of the campus and it is super dark, figure out a way to turn the power on.' + '\n'
    print(textQuestLine)
    questInput = input('Do you accept this quest?(Y/N)' + '\n')
    if(str(questInput) == 'y' or str(questInput) == 'yes'):
        try:
            while(powerOn != True):
                decision = input('There are three spots you can check in the school so far, it is dark: (E to check bag, F for Character Statistics)' + '\n' + 
                'A: Control Room' + '\n' +
                'B: Check Map' + '\n'
                'C: School Directory' + '\n'
                'Your Choice: ')
                if(decision.lower() == 'a' and mapChecked == True):
                    textLocation = '\n' + 'After checking the map, you now know where the control room is.' + '\n' + 'You enter the Control Room and see a switch to turn the school power on' + '\n'
                    print(textLocation)
                    turnOnPower = ''
                    while(turnOnPower.lower() != 'y' and turnOnPower.lower() != 'yes' and turnOnPower.lower() != 'n' and turnOnPower.lower() != 'no'):
                        turnOnPower = input('Would you like to turn the power on?(Y/N)')   
                        if (turnOnPower.lower() == 'y' or turnOnPower.lower() == 'yes'): 
                            powerOn = True
                            print('\n' + "You have now turned the power on!")
                            resultOutcome = gamePlay()
                            #Function that checks that the user health is not 0, if 0 then print (Game Over!) and break program
                            if(Role.Health == 0):
                                print('Game Over!')
                                break
                        elif(turnOnPower.lower() == 'n' or turnOnPower.lower() == 'no'):
                            print("Back to the Entrance" + '\n')
                if(decision.lower() == 'a' and mapChecked == False):
                    textLocation = '\n' + 'You do not know where the Control Room is, figure a way to know where the Control Room is' + '\n'
                    print(textLocation)   
                #Give the user this option when they have a map in their bag
                elif(decision.lower() == 'b' and 'Map' in Role.itemBackpack):
                    textLocation = '\n' + 'You check the Map. You see that the Control Room is not too far down the hall way where you see the blue light.' + '\n'
                    mapChecked = True
                    print(textLocation)
                #Give the user this option when they dont have a map in their bag
                elif(decision.lower() == 'b' and 'Map' not in Role.itemBackpack):
                    textLocation = 'You check your backpack and there is nothing for you see' + '\n'
                    print(textLocation)
                #If the user already has a map in their backpack don't allow them to pick another Map up
                elif(decision.lower() == 'c' or decision.lower() == 'directory' and 'Map' in Role.itemBackpack):
                    textLocation = 'You check the directory and see a map, you already have a map in your backpack. ' + '\n'
                    print(textLocation)
                #If the user hasn't picked up a map from the first school directory from firstChallenge(Role) then allow them pick it up so they can find the control room
                elif(decision.lower() == 'c' or decision.lower() == 'directory' and 'Map' not in Role.itemBackpack):
                    item = 'Map'
                    pickUp = ''
                    textLocation = 'You find a map in the school directory' + '\n'
                    print(textLocation)
                    while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                        pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')   
                        if (pickUp.lower() == 'y' or pickUp.lower() == 'yes'): 
                            Role.itemBackpack.append(item)
                            print("You have now equipped the map..." + '\n')
                        elif(pickUp.lower() == 'n' or pickUp.lower() == 'no'):
                            print("Back to the entrance" + '\n')
                elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                    if not (Role.itemBackpack):
                        print ("Your bag is empty")
                    else:
                        print(*Role.itemBackpack, sep = "\n")  
                elif(decision.lower() == 'f'):
                    print(Role.Stats()) 
            return resultOutcome  
        except:
            print('An error has occured')
#The third challenge requires the user to use the PA system and find out there is teachers sleeping in the class room and then pick up a flashlight so the user knows how they see the coffee maker where user can pour coffee and put them in the bag
def thirdChallenge(Role):
    textLocation = ''
    ClassRoomUnlocked = False
    flashLight = False
    secondKey = False
    microphoneUsed = False
    resultOutcome = ''
    pickUp = ''
    textQuestLine = '\n' + 'You can now see more of the campus and but you dont hear any sounds or have a clue where these teachers are ' + '\n' + 'you have to look for where these teachers are sleeping' + '\n' + 'so you can wake them up!' + '\n'
    print(textQuestLine)
    questInput = input('Do you accept this quest?(Y/N)' + '\n')
    #If N, prompt user to confirm quitting the game
    # The user can check broadcasting station (secondKey), library(flashlight), classroom(needs key) until  
    if(str(questInput) == 'y' or str(questInput) == 'yes'):
        # Do this until flashLight is in the bag and microphone is used in the broadcasting station then give them the classroom option; if A: Broadcasting Station flashlight and microPhone used; You already seen this room  
        while(flashLight != True and microphoneUsed != True):
            decision = input('\n' + 'There are two spots to check in the front of the school and are as listed (E to check bag, F for Character Statistics):' + '\n' +
                    'A: Broadcasting Station' + '\n' +
                    'B: Library' + '\n' +
                    'Your choice: ')
            #Broadcasting Station
            if(decision.lower() == 'a' or decision.lower() == 'station'):
                textLocation = 'You enter the broadcasting station and you can use the microphone and see a flashlight you might need.' + '\n'
                print(textLocation)   
                item = 'Flashlight'
                microphoneChecked = False
                flashLightEquip = False
                while(microphoneChecked != True and flashLightEquip != True):
                    decision = input('\n' + 'There are two spots to check in the broadcasting station and (E to check bag, F for Character Statistics):' + '\n' +
                        'A: Microphone' + '\n' +
                        'B: Flashlight' + '\n'
                        'Your choice: ')
                    if(decision.lower() == 'a' and microphoneChecked == True):
                        textLocation = 'You already made an annoucement and hear snoring coming from class SCAET 420.'
                        print(textLocation)                        
                    #The logic behind the microphone which gives a boolean access to the class room option    
                    if(decision.lower() == 'a' or decision.lower() == 'microphone' and microphoneChecked == False):
                        textLocation = 'You try out the microphone and make an announcement asking if anyone is at the school,' + '\n' + 'you use the PA and hear that there is a ton of snoring going on in class SCAET 420'
                        print(textLocation)
                        microphoneChecked = True
                        microphoneUsed = True
                    if(decision.lower() == 'b' or decision.lower() == 'flashlight'):
                        while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                            pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')   
                            if (pickUp.lower() == 'y' or pickUp.lower() == 'yes'): 
                                Role.itemBackpack.append(item)
                                print("You have now equipped the " + item + "...")
                                flashLightEquip = True
                                flashLight = True
                            elif(pickUp.lower() == 'n' or pickUp.lower() == 'no'):
                                print("Back to the studio")
                    #Give the user this option when they have a map in their bag
                    elif(decision.lower() == 'b' or decision.lower() == 'library'):
                        item = 'secondKey'
                        textLocation = 'You check the library and find a key on the librarians table.' + '\n'
                        print(textLocation)
                        while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                            pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')   
                            if (pickUp.lower() == 'y' or pickUp.lower() == 'yes'): 
                                Role.itemBackpack.append(item)
                                print("You have now equipped the " + item + "...")
                                secondKey = True
                            elif(pickUp.lower() == 'n' or pickUp.lower() == 'no'):
                                print("Back to the school") 
                    elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                        if not (Role.itemBackpack):
                            print ("Your bag is empty")
                        else:
                            print(*Role.itemBackpack, sep = "\n")  
                    elif(decision.lower() == 'f' or 'stats'):
                        print(Role.Stats()) 
        #While Loop that gives the user options A-D: resulting in Broadcasting Room, Library, Coffee Shop, Classroom (Coffee and Secondkey) not until Flashlight is true, Microphone used is true, Coffee in the backpack and the classroom is unlocked with Secondkey         
        while(flashLight != True and microphoneUsed != True and 'Coffee' in Role.itemBackpack and ClassRoomUnlocked == True):   
            decision = input('\n' + 'There are four spots to check in the front of the school and are as listed (E to check bag, F for Character Statistics):' + '\n' +
                    'A: Broadcasting Station' + '\n' +
                    'B: Library' + '\n' +
                    'C: Coffee Shop' + '\n' +
                    'B: Classroom' + '\n' 
                    'Your choice: ')
            if(decision.lower() == 'c' and secondKey == False):
                textLocation = 'You check the classroom and see that the class room is locked' + '\n'
                print(textLocation)
        #textLocation = 'You check the coffee shop and see that there is a fresh pot of coffee there' + '\n'
        #print(textLocation)   
        #return resultOutcome    
#(A: Coffee Shop, B: Broadcasting Station, C: Library, D: Classroom)
def gamePlay():
    result = ''
    resultOutcome = ''
    diceOne = random.randrange(0,7)
    diceTwo = random.randrange(0,7)
    finalDice = diceOne + diceTwo
    print(finalDice)
    #Critical Loss (e.g. 2 - 3): challenge is lost and the attribute that is based on is decreased
    if (finalDice == 1 or finalDice == 2 or finalDice == 3):
        result = '\n' + 'You rolled a ' + str(finalDice) + ' challenge is critically lost and your attributes have decreased' + '\n'
        resultOutcome = 'a'
    #Loss (e.g. 4-7): challenge is lost, no change in the character’s attributes
    elif (finalDice == 4 or finalDice == 5 or finalDice == 6 or finalDice == 7):
        result = '\n' + 'You rolled a ' + str(finalDice) + ' challenge is lost, no change in the character’s attributes' + '\n'
        resultOutcome = 'b'
    #Win (e.g. 8-10): challenge is won, no change in the character’s attributes
    elif (finalDice == 8 or finalDice == 9 or finalDice == 10):
        result = '\n' + 'You rolled a(n) ' + str(finalDice) + ' challenge is won, no change in the character’s attributes' + '\n'
        resultOutcome = 'c'
    #Critical Win (e.g. 11-12): challenge is won and the attribute that is based on increases
    elif (finalDice == 11 or finalDice == 12):
        result = '\n' + 'You rolled a(n)' + str(finalDice) + ' challenge is critically won and the attribute that is based on increases' + '\n'
        resultOutcome = 'd'
    else:
        result = 'Something went wrong here...'
    
    print(result)
    return resultOutcome

GameMenu()

