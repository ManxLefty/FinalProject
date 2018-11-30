# Title: Gamerz (temporary)

# Contributors: Claire Picken, Iver (Sadie J. Warburton), Maura McGowan, Selah Finklestein
# Date: November 23, 2018
# Description: Group project for computer science.

from random import randint
# from graphics import *

class Player:
  def __init__(self, name):
    self.name = name
  def attack(self,opponent)
    self.opponent = opponent
    opponent.current_hp -=  0.5*self.attack_power
    
    
class Juicebox(Player):
  def __init__(self, name):
    super().__init__(name)
    self.name = "Timmy a.k.a. 'Juicebox'"
    self.description = ("Timmy, nicknamed 'Juicebox' at school for his perpetual possession of a juicebox, "
    "typically of grape flavour.  Timmy was dared by his friends to enter this spooky house.  They sent him "
    "with a flashlight, thank goodness.  However, to Timmy's great dismay, he flips the switch as the door slams " 
    "behind him and the flashlight hardly flickers before burning out.  Timmy feels panic rise up in his throat " 
    "but he swallows it with the conviction that this will impress other kids enough that they might want to be friends with him.")
    self.max_hp = 50
 #   self.current_hp = 
    self.attack_power = 20
    self.defensive_power = 30
    self.fainted = False
#    self.num_revives = 0


class Bones(Player):
  def __init__(self, name):
    super().__init__(name)
    self.name = "Salem Bones"
    self.description = "An intimidating witch, though small in stature.  Dapper clothes."
    self.max_hp = 75
    self.attack_power = 20
    self.defensive_power = 5
    self.fainted = False
#    self.num_revives = 0


class Desdemona(Player):
  def __init__(self, name):
    super().__init__(name)
    self.name = "Desdemona Crowe"
    self.description = "A tall, thin, misty woman who almost seems to fade when you break focus on her."
    self.max_hp = 40
    self.attack_power = 30
    self.defensive_power = 30
    self.fainted = False
#    self.num_revives = 0


##class Floor:
##  def __init__(self):
##
##class Room:
##  def __init__(self):
###    size = (LENGTH, WIDTH)
##
##class Library(Room):
##  def __init__(self):
##
##class Study(Room):
##  def __init__(self):
##
##class Observatory(Room):
##  def __init__(self):
##


# Creating General Monster class
class Monster:
    def __init__(self, room):

    def attack(self, player):
        self.player = player
        player.current_hp -=  self.attack_power - 0.5*player.defensive_power

# Super Easy monster
class DustBunny(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Dust Bunny'
        self.attack_power = 1
        self.hp = 5
        
# Easy monster
class Ghost(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Ghost'
        self.attack_power=2
        self.hp = 10
# Medium monster
class BatSwarm(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Swarm of Bats'
        self.attack_power = 3
        self.hp = 20

# Hard monster
class Banshee(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Banshee'
        self.attack_power = 4
        self.hp = 50

# Final Boss
class Armor(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Enchanted Suit of Armor'
        self.attack_power = 5
        self.hp = 100
        
def character_choose():
    print("Choose a character!\n"
          "Your choices are:\n"
          "A. Desdemona Crowe\n"
          "B. Salem Bones\n"
          "C. Timmy a.k.a. 'Juicebox'")
    choice = input("Choose A, B, or C: ").upper()
    if choice == "A":
          player = Desdemona(Player)
          print("\nYou chose Desdemona Crowe!\n")
    if choice == "B":
          player = Bones(Player)
          print("\nYou chose Salem Bones!\n")
    if choice == "C":
          player = Juicebox(Player)
          print("\nYou chose Timmy!\n")
          
    print("Name:", player.name)
    print("Description:", player.description)
    print("Current HP:", player.max_hp)
    print("Attack Power:", player.attack_power)
    print("Defensive Power:", player.defensive_power)

    return player


def main():
    character_choose()
    
    
  
if __name__ == "__main__":
  main()
