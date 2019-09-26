"""This python file implements the data and logic associated with the second role (Wizard)"""
"This document is a Warrior module implements the data and logic associated with the first role (Warrior)"
class Wizard:
    #These member variables (attributes) here display the statistics of the Warrior class
    # Constructor for Warrior class when called user defines the name create name and assign stats accordingly
    def __init__ (self, Name):
        self.Name = Name 
        self.Strength = -2
        self.Vitality = 0
        self.Intelligence = 2
        self.Health = 100