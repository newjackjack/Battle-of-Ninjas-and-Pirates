from classes.ninja import Ninja
from classes.pirate import Pirate
import random

#initiate a battle instance
#make a battlefield between two characters
class BattleField(Ninja,Pirate):
    def __init__(self, player_1, player_2):#addmore arguments here
        self.player_1 = player_1#ninja
        self.player_2 = player_2#pirate
    
    #create a method() that generate randon numbers for the attack
    def battle(self):
        #create a variable to store the random number of the attack for ninja
        # self.attack_num_ninja = random.randint(0,10)
        self.attack_num_ninja = 1
        #create a variable to store the random number of the attack for pirate
        # self.attack_num_pirate = random.randint(0,10)
        self.attack_num_pirate = 10

    #conditionals to fix the speed issue per attack
        #check the speed of attack
        if ( self.player_1.speed > self.player_2.speed):
            #player_1 attack first
            for i in range(self.attack_num_ninja):
            #player_1 is ninja attack*random number topirate
                #check the health before attack
                if(self.player_2.health <= 0):
                    return self
                else:
                    self.player_1.attack(self.player_2)
        else:
            #player_2 is pirate attack*random number to ninja
            for j in range(self.attack_num_pirate ):
                if(self.player_1.health <= 0):
                    return self
                else:
                    self.player_2.attack(self.player_1)
    #create method to show a status
    def final_status(self):
        #check both health
        if(self.player_1.health <= 0):
            #ninja is dead so pirate wins
            print(f"The winner is: {self.player_2.name}")
        
        if(self.player_2.health <= 0):
            #pirate is dead so ninja wins
            print(f"The winner is: {self.player_1.name}")




#player_1: ninja
michelangelo = Ninja("Michelanglo")
#player_2: pirate
jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
battle_of_ninja_pirate = BattleField(michelangelo, jack_sparrow)
battle_of_ninja_pirate.battle()
battle_of_ninja_pirate.final_status()

michelangelo.show_stats()
jack_sparrow.show_stats()
# battle_of_ninja_pirate.final_status()

# michelangelo.show_stats()
