"""This python file is going to serve as the implementation of game data and logic and the interactivity with the user."""
#Imported Modules including random, Warrior, Wizard
import random
import Warrior
import Wizard
#This GameMenu() method represents the introduction of the game, asking for users name and creating the Role object (Warrior and Wizard) accordingly to user input, in addition the outComes of the dice resulting in the attribute changes of Role
def GameMenu():
    #Introduction is the welcome prompt for the RPG Game.
    Introduction = 'Welcome to the World of Sheridan.' + '\n' + '\n' + 'The school has been infested with teachers that sleep,' + '\n' + 'when they teach and we want to get rid of them by the time the summer ends.' + '\n'
    #Printing the Introduction to the user.
    print(Introduction)
    #Input asking user what their name is.
    Name = input('Before we begin what is your name? ' + '\n')
    #Capitalizing the first letter of the name
    NameCap = Name.capitalize()
    #Declaring AskRoleConfirmation as an empty string
    AskRoleConfirmation = ''
    #A new Introduction variable, welcoming the user based and their name.
    Introduction = '\n' + f'Well {NameCap}, you have just entered the school property and you see this problem ' 
    #Printing the introduction with the users Name.
    print(Introduction)
    #Loop until the user has confirmed their choice if they end up saying no keep asking them what their role may be.
    while(AskRoleConfirmation.lower() != 'y' and AskRoleConfirmation.lower() != 'yes'):
        #When user input equals the role create an object of Warrior or Wizard accordingly to the user input
        AskRole = input('The dean gives you two options: ' + '\n' +  'Warrior or Wizard, in order to wake up these bad teachers. ')
        #If the user input is the warrior then assign them the role of "Warrior" from the warrior module
        if (AskRole.lower() == 'warrior'):
            #Character variable assigned to the Warrior module dot Warrior object(capitalizedName)
            Character = Warrior.Warrior(NameCap)
            #Input for user confirming that they would like to choose this class being Warrior
            AskRoleConfirmation = input('Are you sure you would like to choose ' + Character.__class__.__name__ + ' (Y/N)?')
        #If the user input is the wizard then assign them the role of "Wizard" from the wizard module            
        elif(AskRole.lower() == 'wizard'):
            #Character variable assigned to the Wizard module dot Wizard object(capitalizedName)
            Character = Wizard.Wizard(NameCap)
            #Input for user confirming that they would like to choose this class being Wizard
            AskRoleConfirmation = input('Are you sure you would like to choose ' + Character.__class__.__name__ + ' (Y/N)?')
    #Once the Character is assigned give the first challenge to the user and pass the Character through the FirstChallenge that returns a string either 'a','b','c','d' and this string will be equal to ResultFirstChallenge
    ResultFirstChallenge = FirstChallenge(Character)
    #The first challenge will give a string that will result whether or not the user has loss or won, then make, the object adjustments on the member variables
    #Permuations of challenges shall report them to the next challenges 
    #If the user has critically lost the FirstChallenge
    if(ResultFirstChallenge == 'a'):
        #If the firstChallege output is a, then the user critically lost, -1 from stats and -1 vitality which decreases health
        Loss = Character.criticalLoss()
        #Print the string that is returned from Character.criticalLoss() method in the Warrior and Wizard modules
        print(str(Loss))
        #Even if the user critical loss then provide the user with the second challenge.
        SecondResultOutcome = SecondChallenge(Character)
        #If the user has critically lost the SecondChallenge.
        if(SecondResultOutcome == 'a'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has lost the SecondChallenge.
        elif(SecondResultOutcome == 'b'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has won the SecondChallenge.
        elif(SecondResultOutcome == 'c'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has critically won the SecondChallenge.    
        elif(SecondResultOutcome == 'd'):
            #Give the user the third challenge
            ThirdChallenge(Character)
    #If the user has lost the FirstChallenge
    elif(ResultFirstChallenge == 'b'):
        #Even if the user critical loss then provide the user with the second challenge.
        SecondResultOutcome = SecondChallenge(Character)
        #If the user has critically lost the SecondChallenge.
        if(SecondResultOutcome == 'a'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has lost the SecondChallenge.
        elif(SecondResultOutcome == 'b'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has won the SecondChallenge.
        elif(SecondResultOutcome == 'c'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has critically won the SecondChallenge.
        elif(SecondResultOutcome == 'd'):
            #Give the user the third challenge
            ThirdChallenge(Character)
    #If the user has won the FirstChallenge
    elif(ResultFirstChallenge == 'c'):
        #Even if the user won then provide the user with the second challenge.
        SecondResultOutcome = SecondChallenge(Character)
        #If the user has critically lost the SecondChallenge.
        if(SecondResultOutcome == 'a'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has lost the SecondChallenge.
        elif(SecondResultOutcome == 'b'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has won the SecondChallenge.
        elif(SecondResultOutcome == 'c'):
            #Give the user the third challenge
            ThirdChallenge(Character)
        #If the user has critically won the SecondChallenge.
        elif(SecondResultOutcome == 'd'):
            #Give the user the third challenge
            ThirdChallenge(Character)
    #If the firstChallege output is d, then the user critically won, +1 from stats and +1 vitality which increases health
    elif(ResultFirstChallenge == 'd'):
        Win = Character.criticalWin()
        print(str(Win))
        ResultOutcome = SecondChallenge(Character)
        if(ResultOutcome == 'd'):
            ThirdChallenge(Character)
#This method will be the first challenge of entering  a room into 
def FirstChallenge(Role):
    #Decision can be a bush (5 bandages), school directory(map), door(locked, unlock), Sheridan Sign (FirstKey)
    TextLocation = ''
    FirstKey = False
    ResultOutcome = ''
    LockUnlocked = False
    TextQuestLine = '*****FIRST CHALLENGE*****' +  '\n' + 'The dean has assigned you the ' + Role.__class__.__name__ + ' role and has given you the powers' + '\n' + 'to wake these teachers up.' + '\n' + '\n' + 'The dean has asked you to figure out a way to get inside of the campus because the teachers have lock the doors from the inside.' + '\n'
    print(TextQuestLine)
    QuestInput = input('Do you accept the quest?(Y/N)')
    if(str(QuestInput) == 'y' or str(QuestInput) == 'yes'):
        try:
            while(LockUnlocked != True):
                decision = input('\n' + 'There are four spots to check in the front of the school and are as listed (E to check bag, F for Character Statistics):' + '\n' +
                'A: Stairs' + '\n' +
                'B: School Directory' + '\n' +
                'C: Door' + '\n' +
                'D: Sheridan School Sign' + '\n' +
                'Your choice: ')
                if(decision.lower() == 'a' or decision.lower() == 'bush'):
                    #behind the bush is a note that says in order to enter the school, check the door
                    TextLocation = 'You find a note, you pick it up and read it reads:' +'\n' + 'Check the main entrance of the school(door)'
                    print(TextLocation)
                elif(decision.lower() == 'b' or decision.lower() == 'directory'):
                    #you check the school directory and see where the different spots are in the school, you put the map in your backpack
                    Item = 'Map'
                    TextLocation = 'You find a map'
                    print(TextLocation)
                    PickUp = ''
                    while(PickUp.lower() != 'y' and PickUp.lower() != 'yes' and PickUp.lower() != 'n' and PickUp.lower() != 'no'):
                        PickUp = input('Would you like to pick up this ' + Item + ' up?(Y/N)')   
                        #Figure out how to get out of the loop once the Map is equippe and appended to the ItemBackpack
                        if(PickUp.lower() == 'y' or PickUp.lower() == 'yes' and 'Map' not in Role.ItemBackpack): 
                            Role.ItemBackpack.append(Item)
                            print("You have now equipped the map...")
                        elif(decision.lower() == 'y' or PickUp.lower() == 'yes' and 'Map' in Role.ItemBackpack):
                            print("There is nothing to found here anymore")
                        elif(PickUp.lower() == 'n' or PickUp.lower() == 'no'):
                            print("Back to the entrance")
                elif(decision.lower() == 'c' or decision.lower() == 'door'):
                    if(FirstKey == False):
                        TextLocation = 'There is a lock on the door and you see that the door is locked' +'\n' + '...it seems like it can be locked by an Item in your backpack'
                        print(TextLocation)
                    elif(FirstKey == True):
                        TextLocation = 'There is a lock on the door and you see that the door is locked' + '\n' + 'it seems like your FirstKey fits it ' + '\n' + '...' + '\n' + 'Door is now unlocked!' + '\n' + '\n' + 'You have now entered the campus. ' + '\n'
                        #The result outcome is equal to the dice roll from GamePlay()
                        print(TextLocation)
                        ResultOutcome = GamePlay()
                        LockUnlocked = True
                elif(decision.lower() == 'd' or decision.lower() == 'sign'):
                    Item = 'FirstKey'
                    TextLocation = 'You check the sign and notice a ' + Item
                    print(TextLocation)
                    PickUp = ''
                    while(PickUp.lower() != 'y' and PickUp.lower() != 'yes' and PickUp.lower() != 'n' and PickUp.lower() != 'no'):
                        PickUp = input('Would you like to pick up this ' + Item + ' up?(Y/N)')
                        if (PickUp.lower() == 'y' or PickUp.lower() == 'yes'):
                            Role.ItemBackpack.append(Item)                        
                            print("You have now equipped the FirstKey...")
                            FirstKey = True
                        elif PickUp.lower() == 'no' or PickUp.lower() == 'n':
                            print("Back to the entrance")
                elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                    if not (Role.ItemBackpack):
                        print ("Your bag is empty")
                    else:
                        print(*Role.ItemBackpack, sep = "\n") 
                #Find out why it gets here when the power is turned on, escape while loop before this vv         
                elif(decision.lower() == 'f' or 'stats'):
                    print(Role.Stats())                 
            return ResultOutcome
        except:
            print('An error has occured')
def SecondChallenge(Role):
    TextLocation = ''
    MapChecked = False
    PowerOn = False
    ResultOutcome = ''
    TextQuestLine = '\n' + '*****SECOND CHALLENGE*****' +'\n' + 'You are now inside of the campus and it is super dark, figure out a way to turn the power on.' + '\n'
    print(TextQuestLine)
    QuestInput = input('Do you accept this quest?(Y/N)' + '\n')
    if(str(QuestInput) == 'y' or str(QuestInput) == 'yes'):
        try:
            while(PowerOn != True):
                decision = input('There are three spots you can check in the school so far, it is dark: (E to check bag, F for Character Statistics)' + '\n' + 
                'A: Control Room' + '\n' +
                'B: Check Map' + '\n'
                'C: School Directory' + '\n'
                'Your Choice: ')
                if(decision.lower() == 'a' and MapChecked == True):
                    TextLocation = '\n' + 'After checking the map, you now know where the control room is.' + '\n' + 'You enter the Control Room and see a switch to turn the school power on' + '\n'
                    print(TextLocation)
                    turnOnPower = ''
                    while(turnOnPower.lower() != 'y' and turnOnPower.lower() != 'yes' and turnOnPower.lower() != 'n' and turnOnPower.lower() != 'no'):
                        turnOnPower = input('Would you like to turn the power on?(Y/N)')   
                        if (turnOnPower.lower() == 'y' or turnOnPower.lower() == 'yes'): 
                            PowerOn = True
                            print('\n' + "You have now turned the power on!")
                            ResultOutcome = GamePlay()
                            #Function that checks that the user health is not 0, if 0 then print (Game Over!) and break program
                            if(Role.Health == 0):
                                print('Game Over!')
                                break
                        elif(turnOnPower.lower() == 'n' or turnOnPower.lower() == 'no'):
                            print("Back to the Entrance" + '\n')
                if(decision.lower() == 'a' and MapChecked == False):
                    TextLocation = '\n' + 'You do not know where the Control Room is, figure a way to know where the Control Room is' + '\n'
                    print(TextLocation)   
                #Give the user this option when they have a map in their bag
                elif(decision.lower() == 'b' and 'Map' in Role.ItemBackpack):
                    TextLocation = '\n' + 'You check the Map. You see that the Control Room is not too far down the hall way where you see the blue light.' + '\n'
                    MapChecked = True
                    print(TextLocation)
                #Give the user this option when they dont have a map in their bag
                elif(decision.lower() == 'b' and 'Map' not in Role.ItemBackpack):
                    TextLocation = 'You check your backpack and there is nothing for you see' + '\n'
                    print(TextLocation)
                #If the user already has a map in their backpack don't allow them to pick another Map up
                elif(decision.lower() == 'c' or decision.lower() == 'directory' and 'Map' in Role.ItemBackpack):
                    TextLocation = 'You check the directory and see a map, you already have a map in your backpack. ' + '\n'
                    print(TextLocation)
                #If the user hasn't picked up a map from the first school directory from FirstChallenge(Role) then allow them pick it up so they can find the control room
                elif(decision.lower() == 'c' or decision.lower() == 'directory' and 'Map' not in Role.ItemBackpack):
                    Item = 'Map'
                    PickUp = ''
                    TextLocation = 'You find a map in the school directory' + '\n'
                    print(TextLocation)
                    while(PickUp.lower() != 'y' and PickUp.lower() != 'yes' and PickUp.lower() != 'n' and PickUp.lower() != 'no'):
                        PickUp = input('Would you like to pick up this ' + Item + ' up?(Y/N)')   
                        if (PickUp.lower() == 'y' or PickUp.lower() == 'yes'): 
                            Role.ItemBackpack.append(Item)
                            print("You have now equipped the map..." + '\n')
                        elif(PickUp.lower() == 'n' or PickUp.lower() == 'no'):
                            print("Back to the entrance" + '\n')
                elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                    if not (Role.ItemBackpack):
                        print ("Your bag is empty")
                    else:
                        print(*Role.ItemBackpack, sep = "\n")  
                elif(decision.lower() == 'f'):
                    print(Role.Stats()) 
            return ResultOutcome  
        except:
            print('An error has occured')
#The third challenge requires the user to use the PA system and find out there is teachers sleeping in the class room and then pick up a flashlight so the user knows how they see the coffee maker where user can pour coffee and put them in the bag
def ThirdChallenge(Role):
    TextLocation = ''
    ClassRoomUnlocked = False
    flashLight = False
    secondKey = False
    microphoneUsed = False
    ResultOutcome = ''
    PickUp = ''
    TextQuestLine = '*****THIRD CHALLENGE*****' + '\n' + 'You can now see more of the campus and but you dont hear any sounds or have a clue where these teachers are ' + '\n' + 'you have to look for where these teachers are sleeping' + '\n' + 'so you can wake them up!' + '\n'
    print(TextQuestLine)
    QuestInput = input('Do you accept this quest?(Y/N)' + '\n')
    #If N, prompt user to confirm quitting the game
    # The user can check broadcasting station (secondKey), library(flashlight), classroom(needs key) until  
    if(str(QuestInput) == 'y' or str(QuestInput) == 'yes'):
        # Do this until flashLight is in the bag and microphone is used in the broadcasting station then give them the classroom option; if A: Broadcasting Station flashlight and microPhone used; You already seen this room  
        while(flashLight != True or microphoneUsed != True):
            decision = input('\n' + 'There are two spots to check in the front of the school and are as listed (E to check bag, F for Character Statistics):' + '\n' +
                    'A: Broadcasting Station' + '\n' +
                    'B: Library' + '\n' +
                    'Your choice: ')
            #Decision A: Broadcasting Station
            if(decision.lower() == 'a' or decision.lower() == 'station'):
                TextLocation = '\n' + 'You enter the broadcasting station and you can use the microphone and see a flashlight you might need.' + '\n'
                print(TextLocation)   
                Item = 'Flashlight'
                while(microphoneUsed != True or flashLight != True):
                    decision = input('\n' + 'There are two spots to check in the broadcasting station and (E to check bag, F for Character Statistics):' + '\n' +
                        'A: [Place] Microphone' + '\n' +
                        'B: [Item] Flashlight' + '\n'
                        'Your choice: ')
                    if(decision.lower() == 'a' and microphoneUsed == True):
                        TextLocation = '\n' + 'You already made an annoucement and hear snoring coming from class SCAET 420.'
                        print(TextLocation)                        
                        #The logic behind the microphone which gives a boolean access to the class room option    
                    if(decision.lower() == 'a' and microphoneUsed == False):
                        TextLocation = '\n' + 'You try out the microphone and make an announcement asking if anyone is at the school,' + '\n' + 'you use the PA and hear that there is a ton of snoring going on in class SCAET 420'
                        print(TextLocation)
                        microphoneUsed = True
                    if(decision.lower() == 'b' or decision.lower() == 'flashlight'):
                        while(PickUp.lower() != 'y' and PickUp.lower() != 'yes' and PickUp.lower() != 'n' and PickUp.lower() != 'no'):
                            PickUp = input('Would you like to pick up this ' + Item + ' up?(Y/N)')   
                            if (PickUp.lower() == 'y' or PickUp.lower() == 'yes'): 
                                Role.ItemBackpack.append(Item)
                                print("You have now equipped the " + Item + "...")
                                flashLight = True
                                #flashLight = True
                            elif(PickUp.lower() == 'n' or PickUp.lower() == 'no'):
                                print("Back to the studio")
            #Give the user this option when they have a map in their bag
            elif(decision.lower() == 'b' or decision.lower() == 'library'):
                Item = 'secondKey'
                TextLocation = 'You check the library and find a key on the librarians table.' + '\n'
                print(TextLocation)
                while(PickUp.lower() != 'y' and PickUp.lower() != 'yes'):
                    PickUp = input('Would you like to pick up this ' + Item + ' up?(Y/N)')   
                    if (PickUp.lower() == 'y' or PickUp.lower() == 'yes'): 
                        Role.ItemBackpack.append(Item)
                        print("You have now equipped the " + Item + "...")
                        secondKey = True
                    elif(PickUp.lower() == 'n' or PickUp.lower() == 'no'):
                        print("Back to the school") 
            elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                if not (Role.ItemBackpack):
                    print ("Your bag is empty")
                else:
                    print(*Role.ItemBackpack, sep = "\n")  
            elif(decision.lower() == 'f' or 'stats'):
                print(Role.Stats()) 
        #While Loop that gives the user options A-D: resulting in Broadcasting Room, Library, Coffee Shop, Classroom (Coffee and Secondkey) not until Flashlight is true, Microphone used is true, Coffee in the backpack and the classroom is unlocked with Secondkey         
        while(flashLight != True or microphoneUsed != True or 'Coffee' in Role.ItemBackpack or ClassRoomUnlocked == True):   
            decision = input('\n' + 'There are four spots to check in the front of the school and are as listed (E to check bag, F for Character Statistics):' + '\n' +
                    'A: Broadcasting Station' + '\n' +
                    'B: Library' + '\n' +
                    'C: Coffee Shop' + '\n' +
                    'B: Classroom' + '\n' 
                    'Your choice: ')
            if(decision.lower() == 'c' and secondKey == False):
                TextLocation = 'You check the classroom and see that the class room is locked' + '\n'
                print(TextLocation)
        #TextLocation = 'You check the coffee shop and see that there is a fresh pot of coffee there' + '\n'
        #print(TextLocation)   
        return ResultOutcome
#(A: Coffee Shop, B: Broadcasting Station, C: Library, D: Classroom)
def GamePlay():
    result = ''
    ResultOutcome = ''
    DiceOne = random.randrange(1,7)
    DiceTwo = random.randrange(1,7)
    FinalDice = DiceOne + DiceTwo
    #Critical Loss (e.g. 2 - 3): challenge is lost and the attribute that is based on is decreased
    if (FinalDice == 1 or FinalDice == 2 or FinalDice == 3):
        result = '\n' + 'You rolled a ' + str(FinalDice) + ' challenge is critically lost and your attributes have decreased' + '\n'
        ResultOutcome = 'a'
    #Loss (e.g. 4-7): challenge is lost, no change in the character’s attributes
    elif (FinalDice == 4 or FinalDice == 5 or FinalDice == 6 or FinalDice == 7):
        result = '\n' + 'You rolled a ' + str(FinalDice) + ' challenge is lost, no change in the character’s attributes' + '\n'
        ResultOutcome = 'b'
    #Win (e.g. 8-10): challenge is won, no change in the character’s attributes
    elif (FinalDice == 8 or FinalDice == 9 or FinalDice == 10):
        result = '\n' + 'You rolled a(n) ' + str(FinalDice) + ' challenge is won, no change in the character’s attributes' + '\n'
        ResultOutcome = 'c'
    #Critical Win (e.g. 11-12): challenge is won and the attribute that is based on increases
    elif (FinalDice == 11 or FinalDice == 12):
        result = '\n' + 'You rolled a(n)' + str(FinalDice) + ' challenge is critically won and the attribute that is based on increases' + '\n'
        ResultOutcome = 'd'
    else:
        result = 'Something went wrong here...'
    
    print(result)
    return ResultOutcome

GameMenu()

