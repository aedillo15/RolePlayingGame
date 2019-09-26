#This python file is going to serve as the implementation of game data and logic and the interactivity with the user.
#Imported Modules including random, Warrior, Wizard
import random
import Warrior
import Wizard
#This GameMenu() method represents the introduction of the game, asking for users name and creating the Role object (Warrior and Wizard)
def GameMenu():
    Introduction = 'Welcome to the World of Sheridan.' + '\n' + 'The school has been infested with teachers that sleep,' + '\n' + 'when they teach and we want to get rid of them by the time the summer ends.'
    print(Introduction)
    Name = input('Before we begin what is your name? ')
    AskRole = input(f'Well {Name}, you have just entered the school and you see this problem,' + '\n' + 
    'the dean of the school has allowed the special powers' + '\n' +
    'to be given to you to wake these teachers up' + '\n'
    + 'The dean gives you two options: Warrior or Wizard, in order to wake up these bad teachers. ')
    if (AskRole == 'Warrior' or 'warrior'):
        #When user input equals the role create an object of Warrior or Wizard accordingly to the user input
        Character = Warrior.Warrior(Name)
        #Once the role is assigned give the first challenge to the user
        resultFirstChallenge = firstChallenge(Character)
        #The first challenge will give a string that will result whether or not the user has loss or won, then make
        #the object adjustments on the member variables
        #If the firstChallege output is a, then the user critically lost, -1 from stats and vitality which decreases health
        if(resultFirstChallenge == 'a'):
            #Subtracting 1 from the strength
            loss = Character.criticalLoss()
            print(str(loss))
            #Character.subStrength(1)
            #Decrease Vitality which then affects the health
        #If the firstChallege output is d, then the user critically won, +1 from stats and vitality which increases health
        elif(resultFirstChallenge == 'd'):
            win = Character.criticalWin()
            print(str(win))
            #Character.addStrength(1)
        #print(AskRole)
#    elif(AskRole == 'Wizard' or 'wizard'):
#        Character = Wizard
    #print(Introduction, AskRole)
#This method will be the first challenge of entering  a room into 
def firstChallenge(Role):
    #Decision can be a bush (5 bandages), school directory(map), door(locked, unlock), Sheridan Sign (key)
    textLocation = ''
    key = False
    resultOutcome = ''
    lockUnlocked = False
    textQuestLine = 'The dean has assigned you the ' + Role.__class__.__name__ + ' role and has given you the powers' + '\n' + 'to wake these teachers up' 
    'The dean has asked you to figure out a way to get inside of the campus because the teachers have locked them from the inside' + '\n'
    print(textQuestLine)
    questInput = input('Do you accept the quest?(Y/N)')
    if(questInput == str(questInput) == 'yes' or 'y'):
        try:
            while(lockUnlocked != True):
                decision = input('There are four spots to check in the front of the school and are as listed (E to check bag, F for Character Statistics):' + '\n' +
                'A: Stairs' + '\n' +
                'B: School Directory' + '\n' +
                'C: Door' + '\n' +
                'D: Sheridan School Sign' + '\n' +
                'Your choice: ' + '\n')
                if(decision.lower() == 'a' and 'bush'):
                    #behind the bush is a note that says in order to enter the school, check the door
                    textLocation = 'You find a note, you pick it up and read it reads:' +'\n' + 'Check the main entrance of the school(door)'
                    print(textLocation)
                # vv Get to the directory decision vv 
                elif(decision.lower() == 'b' and 'directory'):
                    #you check the school directory and see where the different spots are in the school, you put the map in your backpack
                    pickUp = ''
                    item = 'Map'
                    textLocation = 'You find a map'
                    print(textLocation)
                    while(pickUp != str.lower('y') and str.lower('yes') and str.lower('n') and str.lower('no')):
                        pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')   
                        if (pickUp.lower() == 'y' and 'yes'): 
                            Role.itemBackpack.append(item)
                            print("You have now equipped the map...")
                        elif(pickUp.lower() == 'n' and 'no'):
                            print("Back to the entrance")
                elif(decision.lower() == 'c' and 'door'):
                    if(key == False):
                        textLocation = 'The door is locked and there is a lock' +'\n' + '...it seems like it can be locked by something'
                        print(textLocation)
                    elif(key == True):
                        textLocation = 'The door is locked and there is a lock' + '\n' + 'it seems like your key fits it ' + '\n' + '...' + '\n' + 'Door is now unlocked!'
                        #The result outcome is equal to the dice roll from gamePlay()
                        resultOutcome = gamePlay()
                        print(textLocation)
                        lockUnlocked = True
                elif(decision.lower() == 'd' and 'sign'):
                    item = 'Key'
                    textLocation = 'You check the sign and notice a ' + item
                    print(textLocation)
                    pickUp = ''
                    while(pickUp != str.lower('y') and str.lower('yes') and str.lower('n') and str.lower('no')):
                        pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')
                        if (pickUp.lower() == 'y' and 'yes'):
                            Role.itemBackpack.append(item)                        
                            print("You have now equipped the key...")
                            key = True
                        elif pickUp.lower() == 'no' and 'n':
                            key = False
                elif(decision.lower() == 'e' and 'bag'):
                    if not (Role.itemBackpack):
                        print ("Your bag is empty")
                    else:
                        print(*Role.itemBackpack, sep = "\n")               
            return resultOutcome
        except:
            print('An error has occured')
        #elif(str(questInput) == 'no' or 'n'):
            #GameMenu()
#def pickUp(item, decision, roleBackpack):
def entranceOfSchoolDecision():
    decision = input('There are four spots to check in the front of the school and are as listed:' + '\n' +
                'A: Bush' + '\n' +
                'B: School Directory' + '\n' +
                'C: Door' + '\n' +
                'D: Sheridan School Sign' + '\n')
    return decision
def gamePlay():
    result = ''
    resultOutcome = ''
    diceOne = random.randrange(0,6)
    diceTwo = random.randrange(0,6)
    finalDice = diceOne + diceTwo
    #Critical Loss (e.g. 2 - 3): challenge is lost and the attribute that is based on is decreased
    if finalDice == 2 or 3:
        result = 'You rolled a ' + str(finalDice) + ' challenge is critically lost and the attribute that is based on is decreased'
        resultOutcome = 'a'
    #Loss (e.g. 4-7): challenge is lost, no change in the character’s attributes
    elif (finalDice == 4 or 5 or 6 or 7):
        result = 'You rolled a ' + str(finalDice) + ' challenge is lost, no change in the character’s attributes'
        resultOutcome = 'b'
    #Win (e.g. 8-10): challenge is won, no change in the character’s attributes
    elif (finalDice == 8 or 9 or 10):
        result = 'You rolled a ' + str(finalDice) + ' challenge is won, no change in the character’s attributes'
        resultOutcome = 'c'
    #Critical Win (e.g. 11-12): challenge is won and the attribute that is based on increases
    elif (finalDice == 11 or 12):
        result = 'You rolled a ' + str(finalDice) + ' challenge is critically won and the attribute that is based on increases'
        resultOutcome = 'd'
    else:
        result = 'Something went wrong here...'
    
    print(result)
    return resultOutcome

GameMenu()
