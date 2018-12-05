# Title: Gamerz (temporary)

# Contributors: Claire Picken, Iver (Sadie J. Warburton), Maura McGowan, Selah Finklestein
# Date: November 23, 2018
# Description: Group project for computer science.
import random
from time import sleep

# creating a Player class
class Player:
  def __init__(self, name):
    self.name = name
    
  def attack(self,opponent):
  '''Allows the player to attack an opponent'''
    self.opponent = opponent
    opponent.current_hp -=  int(0.5*random.randint(0,self.attack_power))
    
  def defend(self,opponent):
    '''Allows the player to defend against an opponent'''
    self.opponent = opponent
    #self.current_hp-=int(random.randint(1,opponent.attack_power)/self.defensive_power)
    self.current_hp += int(0.1*random.randint(0,self.defensive_power))

  def battle(self,opponent):
    '''Creates a battle function that allows the player to interact with an opponent. The opponent will automatically attack the Player.
    The Player can choose to attack or defend. Defending allows you to heal a random amount of health.'''
    print('A wild',opponent.name,'appeared')
    while self.current_hp>0 and opponent.current_hp>0:
        action = input('Enter \'A\' for attack or \'D\' for defend \n').upper()
        print('')
        if action == 'A':
            print('You attack',opponent.name)
            self.attack(opponent)
            print(opponent.name,'HP:', opponent.current_hp,'/',opponent.max_hp,'\n')
            sleep(1)
            if opponent.current_hp<=0:
                print('You have defeated',opponent.name)
            else:
                opponent.attack(self)
                sleep(1)
                print(opponent.name,'attacked you!')
                print(self.name,'HP:', self.current_hp,'/',self.max_hp,'\n')
                sleep(1)
            
        elif action =='D':
            self.defend(opponent)
            print('You have defended against',opponent.name)
            print(self.name,'HP:', self.current_hp,'/',self.max_hp,'\n')
            

        else:
            print('Invalid choice')
    
# Player subclasses    
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
    self.current_hp = 50
    self.attack_power = 20
    self.defensive_power = 30


class Bones(Player):
  def __init__(self, name):
    super().__init__(name)
    self.name = "Salem Bones"
    self.description = "An intimidating witch, though small in stature.  Dapper clothes."
    self.max_hp = 75
    self.current_hp = 75
    self.attack_power = 20
    self.defensive_power = 5


class Desdemona(Player):
  def __init__(self, name):
    super().__init__(name)
    self.name = "Desdemona Crowe"
    self.description = "A tall, thin, misty woman who almost seems to fade when you break focus on her."
    self.max_hp = 40
    self.current_hp = 40
    self.attack_power = 30
    self.defensive_power = 30

# Creating General Monster class
class Monster:
    def __init__(self, room):
      '''Initializing Monster object''''
        self.room = room
    def attack(self, player):
      '''Allows monster to attack the Player'''
        self.player = player
        player.current_hp -=  int(random.randint(1,self.attack_power) / (0.5*player.defensive_power))

# Monster subclasses
# Super Easy monster
class DustBunny(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Dust Bunny'
        self.attack_power = 10
        self.max_hp = random.randint(0,10)
        self.current_hp = self.max_hp
        
# Easy monster
class Ghost(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Ghost'
        self.attack_power=20
        self.max_hp = random.randint(0,10)
        self.current_hp = self.max_hp
        
# Medium monster
class BatSwarm(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Swarm of Bats'
        self.attack_power = 30
        self.max_hp = 20
        self.current_hp=self.max_hp

# Hard monster
class Banshee(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Banshee'
        self.attack_power = 40
        self.max_hp = 50
        self.current_hp=self.max_hp

# Final Boss
class Armor(Monster):
    def __init__(self, room):
        super().__init__(room)
        self.name = 'Enchanted Suit of Armor'
        self.attack_power = 50
        self.max_hp = 100
        self.current_hp=self.max_hp
        
def character_choose():
  '''Allows the Player to choose a character. Then prints the character's stats.'''
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
    player=character_choose()
    # A sample battle. Remove later
    armor = Armor('room')
    player.battle(armor)
    
    
  
if __name__ == "__main__":
  main()
