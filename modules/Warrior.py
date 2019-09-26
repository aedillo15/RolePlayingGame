"This document is a Warrior module implements the data and logic associated with the first role (Warrior)"
class Warrior:
    #These member variables (attributes) here display the statistics of the Warrior class
    # Constructor for Warrior class when called user defines the name create name and assign stats accordingly
    def __init__ (self, Name):
        self.Name = Name 
        self.Strength = 2
        self.Vitality = 0
        self.Intelligence = -2
        self.HealthPoints = 100
        self.Health = 100
        self.itemBackpack = []
    #The vitalityHealth method results in health goes down accordingly to the attribute of Vitality
    def VitalityHealth(self, Vitality):
        if(Vitality == 1):
            TotalHealth = self.Health + 25
        elif(Vitality == 2):
            TotalHealth = self.Health + 50
        else:
            print("No changes to health")
        return TotalHealth
    #The criticalLoss() method results in the stat change when the Warrior loses the challenge critically rolling a number between 2-3
    def criticalLoss(self):
        Strength = self.Strength - 1
        HealthPoints = self.HealthPoints - 25
        Vitality = self.Vitality - 1
        Health = self.VitalityHealth(Vitality)
        ToString = "With your critical loss, attributes have gone down strength is now: " + str(Strength) + " vitality is now: " + str(Vitality) + " resulting in total Health now is: " + str(HealthPoints)+ "/" + str(Health)
        return ToString
    #The criticalWin() method results in the stat change when the Warrior wins the challenge critically rolling a number between 11-12
    def criticalWin(self):
        Strength = self.Strength + 1
        HealthPoints = self.HealthPoints + 25
        Vitality = self.Vitality + 1
        Health = self.VitalityHealth(Vitality)
        ToString = "With your critical win, attributes have gone up strength is now: " + str(Strength) + " vitality is now: " + str(Vitality) + " resulting in total Health now is: " + str(HealthPoints)+ "/" + str(Health)
        return ToString

