from classes.char import Char
class Orc(Char):

    def __init__( self , name ):
        super().__init__(name)
        self.strength = 20
        self.speed = 1
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self