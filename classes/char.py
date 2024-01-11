

#This is our character object

class Char:
    def __init__( self , name ):
        self.name = name
        self.strength = 0
        self.speed = 0
        self.health = 0

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self