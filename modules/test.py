import Warrior
import Wizard


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
            #Decision A: Broadcasting Station
            if(decision.lower() == 'a' or decision.lower() == 'station'):
                textLocation = 'You enter the broadcasting station and you can use the microphone and see a flashlight you might need.' + '\n'
                print(textLocation)   
                item = 'Flashlight'
                microphoneChecked = False
                flashLightEquip = False
                while(microphoneChecked != True and flashLightEquip != True):
                    decision = input('\n' + 'There are two spots to check in the broadcasting station and (E to check bag, F for Character Statistics):' + '\n' +
                        'A: [Place] Microphone' + '\n' +
                        'B: [Item] Flashlight' + '\n'
                        'Your choice: ')
                    if(decision.lower() == 'a' and microphoneChecked == True):
                        textLocation = 'You already made an annoucement and hear snoring coming from class SCAET 420.'
                        print(textLocation)                        
                        #The logic behind the microphone which gives a boolean access to the class room option    
                    if(decision.lower() == 'a' or decision.lower() == 'microphone' and microphoneChecked == False):
                        textLocation = '\n' + 'You try out the microphone and make an announcement asking if anyone is at the school,' + '\n' + 'you use the PA and hear that there is a ton of snoring going on in class SCAET 420'
                        print(textLocation)
                        microphoneChecked = True
                        #microphoneUsed = True
                    if(decision.lower() == 'b' or decision.lower() == 'flashlight'):
                        while(pickUp.lower() != 'y' and pickUp.lower() != 'yes' and pickUp.lower() != 'n' and pickUp.lower() != 'no'):
                            pickUp = input('Would you like to pick up this ' + item + ' up?(Y/N)')   
                            if (pickUp.lower() == 'y' or pickUp.lower() == 'yes'): 
                                Role.itemBackpack.append(item)
                                print("You have now equipped the " + item + "...")
                                flashLightEquip = True
                                #flashLight = True
                            elif(pickUp.lower() == 'n' or pickUp.lower() == 'no'):
                                print("Back to the studio")
            #Give the user this option when they have a map in their bag
            elif(decision.lower() == 'b' or decision.lower() == 'library'):
                item = 'secondKey'
                textLocation = 'You check the library and find a key on the librarians table.' + '\n'
                print(textLocation)
                while(pickUp.lower() != 'y' and pickUp.lower() != 'yes'):
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
        return resultOutcome

Character = Warrior.Warrior("Arzen")
thirdChallenge(Character)