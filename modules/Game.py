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
    AskRole = input('\n' + f'Well {Name}, you have just entered the school and you see this problem,' + '\n' + 
    'the dean of the school has allowed the special powers' + '\n' +
    'to be given to you to wake these teachers up.' + '\n' + '\n'
    + 'The dean gives you two options: ' + '\n' +  'Warrior or Wizard, in order to wake up these bad teachers. ')
    if (AskRole == 'Warrior' or 'warrior'):
        #When user input equals the role create an object of Warrior or Wizard accordingly to the user input
        Character = Warrior.Warrior(Name)
        #Once the role is assigned give the first challenge to the user
        resultFirstChallenge = firstChallenge(Character)
        #The first challenge will give a string that will result whether or not the user has loss or won, then make
        #the object adjustments on the member variables
        #If the firstChallege output is a, then the user critically lost, -1 from stats and -1 vitality which decreases health
        if(resultFirstChallenge == 'a'):
            #Subtracting 1 from the strength
            loss = Character.criticalLoss()
            print(str(loss))
            secondChallenge(Character)
        elif(resultFirstChallenge == 'b'):
            secondChallenge(Character)
        elif(resultFirstChallenge == 'c'):
            secondChallenge(Character)
        #If the firstChallege output is d, then the user critically won, +1 from stats and +1 vitality which increases health
        elif(resultFirstChallenge == 'd'):
            win = Character.criticalWin()
            print(str(win))
            secondChallenge(Character)
        #    elif(AskRole == 'Wizard' or 'wizard'):
        #        Character = Wizard
#This method will be the first challenge of entering  a room into 
def firstChallenge(Role):
    #Decision can be a bush (5 bandages), school directory(map), door(locked, unlock), Sheridan Sign (key)
    textLocation = ''
    key = False
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
                        if(pickUp.lower() == 'y' or pickUp.lower() == 'yes'): 
                            Role.itemBackpack.append(item)
                            print('You have now equipped the map...')
                        elif(pickUp.lower() == 'n' or pickUp.lower() == 'no'):
                            print('Back to the entrance')
                elif(decision.lower() == 'c' or decision.lower() == 'door'):
                    if(key == False):
                        textLocation = 'The door is locked and there is a lock' +'\n' + '...it seems like it can be locked by something'
                        print(textLocation)
                    elif(key == True):
                        textLocation = 'The door is locked and there is a lock' + '\n' + 'it seems like your key fits it ' + '\n' + '...' + '\n' + 'Door is now unlocked!' + '\n' + '\n' + 'You have now entered the campus. '
                        #The result outcome is equal to the dice roll from gamePlay()
                        resultOutcome = gamePlay()
                        print(textLocation)
                        lockUnlocked = True
                elif(decision.lower() == 'd' or decision.lower() == 'sign'):
                    item = 'Key'
                    textLocation = 'You check the sign and notice a ' + item
                    print(textLocation)
                    pickUp = ''
                    while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                        pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')
                        if (pickUp.lower() == 'y' or pickUp.lower() == 'yes'):
                            Role.itemBackpack.append(item)                        
                            print('You have now equipped the key...')
                            key = True
                        elif pickUp.lower() == 'no' or pickUp.lower() == 'n':
                            print('Back to the entrance')
                elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                    if not (Role.itemBackpack):
                        print ('Your bag is empty')
                    else:
                        print(*Role.itemBackpack, sep = '\n')  
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
    #lockUnlocked = False
    textQuestLine = '\n' + 'You are now inside of the campus and now you have to look for the teachers to wake up' + '\n' + 'since they have been asleep since the beginning of the summer from the previous semesters. ' + '\n'
    print(textQuestLine)
    questInput = input('Do you accept this quest?(Y/N)' + '\n')
    if(str(questInput) == 'y' or str(questInput) == 'yes'):
        try:
            while(powerOn != True):
                decision = input('There are three spots you can check in the school so far and the rest of the schools power is out, so it is dark: (E to check bag, F for Character Statistics)' + '\n' + 
                'A: Control Room' + '\n' +
                'B: Check Map' + '\n'
                'C: School Directory' + '\n'
                'Your Choice: ')
                if(decision.lower() == 'a' and mapChecked == True):
                    textLocation = 'After checking the map, you now know where the control room is and you enter this room and see a switch to turn the school power on' + '\n'
                    print(textLocation)
                    turnOnPower = ''
                    while(turnOnPower.lower() != 'y' and turnOnPower.lower() != 'yes' and turnOnPower.lower() != 'n' and turnOnPower.lower() != 'no'):
                        turnOnPower = input('Would you like to turn the power on?(Y/N)')   
                        if (turnOnPower.lower() == 'y' or turnOnPower.lower() == 'yes'): 
                            powerOn = True
                            print('You have now turned the power on!')
                            resultOutcome = gamePlay()
                        elif(turnOnPower.lower() == 'n' or turnOnPower.lower() == 'no'):
                            print('Back to the entrance')
                    print(textLocation)
                if(decision.lower() == 'a' and mapChecked == False):
                    textLocation = 'You do not know where the control room is, figure a way to know where the Control Room is' + '\n'
                    print(textLocation)   
                #Give the user this option when they have a map in their bag
                elif(decision.lower() == 'b' and 'Map' in Role.itemBackpack):
                    textLocation = 'You check the map and see that the control room is not too far down the hall way where you see the blue light' + '\n'
                    mapChecked = True
                    print(textLocation)
                #Give the user this option when they dont have a map in their bag
                elif(decision.lower() == 'b' and 'Map' not in Role.itemBackpack):
                    textLocation = 'You check your backpack and there is nothing for you see' + '\n'
                    print(textLocation)
                elif(decision.lower() == 'c' or decision.lower() == 'directory' and 'Map' not in Role.itemBackpack):
                    item = 'Map'
                    pickUp = ''
                    textLocation = 'You find a map in the school directory' + '\n'
                    print(textLocation)
                    while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                        pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')   
                        if (pickUp.lower() == 'y' or pickUp.lower() == 'yes'): 
                            Role.itemBackpack.append(item)
                            print('You have now equipped the map...')
                        elif(pickUp.lower() == 'n' or pickUp.lower() == 'no'):
                            print('Back to the entrance')
                elif(decision.lower() == 'e' or decision.lower() == 'bag'):
                    if not (Role.itemBackpack):
                        print ('Your bag is empty')
                    else:
                        print(*Role.itemBackpack, sep = '\n')  
                elif(decision.lower() == 'f' or 'stats'):
                    print(Role.Stats()) 
                return resultOutcome    
        except:
            print('An error has occured')
#Do not give the room information (A: Coffee Shop, B: Broadcasting Station, C: Library, D: Classroom) until the user has checked a two part menu where a note says to check the map 
def gamePlay():
    result = ''
    resultOutcome = ''
    diceOne = random.randrange(0,7)
    diceTwo = random.randrange(0,7)
    finalDice = diceOne + diceTwo
    #Critical Loss (e.g. 2 - 3): challenge is lost and the attribute that is based on is decreased
    if (finalDice == 2 or finalDice == 3):
        result = '\n' + 'You rolled a ' + str(finalDice) + ' challenge is critically lost and your attributes have decreased' + '\n'
        resultOutcome = 'a'
    #Loss (e.g. 4-7): challenge is lost, no change in the character’s attributes
    elif (finalDice == 4 or finalDice == 5 or finalDice == 6 or finalDice == 7):
        result = '\n' + 'You rolled a ' + str(finalDice) + ' challenge is lost, no change in the character’s attributes' + '\n'
        resultOutcome = 'b'
    #Win (e.g. 8-10): challenge is won, no change in the character’s attributes
    elif (finalDice == 8 or finalDice == 9 or finalDice == 10):
        result = '\n' + 'You rolled a ' + str(finalDice) + ' challenge is won, no change in the character’s attributes' + '\n'
        resultOutcome = 'c'
    #Critical Win (e.g. 11-12): challenge is won and the attribute that is based on increases
    elif (finalDice == 11 or finalDice == 12):
        result = '\n' + 'You rolled a ' + str(finalDice) + ' challenge is critically won and the attribute that is based on increases' + '\n'
        resultOutcome = 'd'
    else:
        result = 'Something went wrong here...'
    
    print(result)
    return resultOutcome

GameMenu()

