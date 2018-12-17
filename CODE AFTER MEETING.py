#NOTES: add the sleep back in
#change the armor power back
#add in the opening graphic

#ISSUES: 1. how to end the game 2. invalid room input calls empty rooms 

import random
from time import sleep
places = {}
inventory = []
from graphics import *

def opening_graphic():
    print("Welcome to Alabastor Manor")

    WIDTH = 600
    HEIGHT = 600 

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #title
    titleImage = Image(Point(300,300),"escapefromalabastormanor.png")
    titleImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)
    
    #juicebox  
    juiceboxImage = Image(Point(300,300),"juicebox.png")
    juiceboxImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #desdemona
    desdemonaImage = Image(Point(300,300),"desdemona.png")
    desdemonaImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #salem
    salemImage = Image(Point(300,300),"salem.png")
    salemImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #Manor Map
    ManorMapImage = Image(Point(300,300),"ManorMap.png")
    ManorMapImage.draw(win)

#opening_graphic()

################################################################################
#THIS IS WHERE THE PLAYER STARTS
player_location = 'frontlawn'

################################################################################
# CREATING A PLAYER CLASS
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
        if self.current_hp!=self.max_hp:
            self.current_hp += int(0.1*random.randint(0,self.defensive_power))

            

    def battle(self,opponent):
        '''Creates a battle function that allows the player to interact with an opponent.
        The opponent will automatically attack the Player. The Player can choose to attack or defend.
        Defending allows you to heal a random amount of health.'''

        print('A wild',opponent.name,'appeared')
        
        while self.current_hp>0 and opponent.current_hp>0:
            action = input('Enter \'A\' for attack or \'D\' for defend or \'HELP\' if you need help\n').upper()
            print('')
            if action == 'A':
                print('You attack',opponent.name)
                self.attack(opponent)
                print(opponent.name,'HP:', opponent.current_hp,'/',opponent.max_hp,'\n')
                sleep(0.5)
                if opponent.current_hp<=0:
                    print('You have defeated',opponent.name)
                    print()#add a line of space so that it is easier to read terminal
                elif opponent.current_hp <= 0 and opponent.name == 'Enchanted Suit of Armor':
                    print("You defeated the Boss Monster!")
                    print("You have won the game!")
                    game_over = True
                    return game_over 
                elif opponent.current_hp >0:
                    opponent.attack(self)
                    sleep(0.5)
                    print(opponent.name,'attacked you!')
                    print(self.name,'HP:', self.current_hp,'/',self.max_hp,'\n')
                    #sleep(0.5)
        
            elif action =='D':
                self.defend(opponent)
                print('You have defended against',opponent.name)
                print(self.name,'HP:', self.current_hp,'/',self.max_hp,'\n')

            elif action =='HELP':
                print('''You are now in combat. Your objective is to attack your opponent
until their HP (Hit Points) drop to zero. Be careful about your own
HP, because if it drops to zero, game over! Type 'A' and hit enter
to attack and type 'D' and hit enter to defend. If you defend, you
do not take damage and have a chance to heal, based on your
character's stats \n''')
                
            else:
                print('Invalid choice')


        #to end the game
        while self.current_hp <= 0 and opponent.current_hp >0:
            #you are dead and the opponent defeated you
            game_over = True
            return game_over 


# PLAYER SUBCLASS    
class Juicebox(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Timmy a.k.a. 'Juicebox'"
        self.description = ('''Timmy was given the nickname 'Juicebox' at school for
his perpetual possession of a juicebox, typically of grape flavor.
Timmy was dared by his friends to enter this spooky house. They
sent him with a flashlight, thank goodness. He hopes it will come
in handy later. He can't wait for all the other kids to ask him
about how he escaped Alabastor Manor... he just hopes he can make
it out.5''')
        self.max_hp = 50
        self.current_hp = 50
        self.attack_power = 20
        self.defensive_power = 30


class Bones(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Salem Bones"
        self.description = ('''Salem is an intimidating witch, though small in stature.
They regularly dress in a casual wool suit when the weather
permits. Their familiar, a leopard gecko named Cliffton, clings
to their lapel. Salem has sensed a strong field of arcane magic
coming from the mansion ever since they were a k
id. Now, with
wand in hand and Cliffton hanging on for dear life, they feel
strong enough to defeat the magic that has been in control of the
manor all these years.''')
        self.max_hp = 75
        self.current_hp = 75
        self.attack_power = 20
        self.defensive_power = 20


class Desdemona(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Desdemona Crowe"
        self.description = ('''Desdemona had worked as the Alabastor governess for as
long as she could remember. A freak accident took her life many
years ago, and she only recently decided to revisit her home
for so many years, even if its inhabitants are long gone.
At least she can reconvene with the ghosts of all the people
she cared for when they were young.''' )
        self.max_hp = 40
        self.current_hp = 40
        self.attack_power = 30
        self.defensive_power = 30

# Creating General Monster class
class Monster:
    def __init__(self, room):
    #'''Initializing Monster object''''
        self.room = room
    def attack(self, player):
    #'''Allows monster to attack the Player'''
        self.player = player
        player.current_hp -=  int(random.randint(1,self.attack_power) / (0.5*player.defensive_power))

################################################################################
# Creating General Monster class
class Monster:
    def __init__(self, room):
    #'''Initializing Monster object''''
        self.room = room
    def attack(self, player):
    #'''Allows monster to attack the Player'''
        self.player = player
        player.current_hp -=  int(random.randint(1,self.attack_power) / (0.5*player.defensive_power))

#MONSTER SUBCLASSES
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

################################################################################
#CHARACTER CHOICE
def character_choose():
#'''Allows the Player to choose a character. Then prints the character's stats.'''
    print("Choose a character!\n"
          "Your choices are:\n"
          "A. Desdemona Crowe\n"
          "B. Salem Bones\n"
          "C. Timmy a.k.a. 'Juicebox'")

    try: 

        choice = input("Type 'A', 'B', 'C', or 'HELP' and hit enter: ").upper()
        while choice:    
            if choice == "A":
                  player = Desdemona(Player)
                  print("\nYou chose Desdemona!")
                  break
            if choice == "B":
                  player = Bones(Player)
                  print("\nYou chose Salem!")
                  break
            if choice == "C":
                  player = Juicebox(Player)
                  print("\nYou chose Timmy!")
                  break
            if choice == 'HELP':
                  print('''Welcome to the game! Choose a character by typing the corresponding
letter and hitting enter. Once you choose a character, you will be immersed
in the world of 'ESCAPE FROM ALABASTOR MANOR,' where you will be faced with
many life-and-death decisions.\n
NAVIGATION\n
When navigating through the mansion, a list of
exits from the room you are currently in will appear in a numbered list. Type
the number of the exit you would like to go through and hit enter. Some rooms
require you to answer a riddle to move into the room, and others put you
against an enemy that calls the mansion home.\n
RIDDLES\n
Type your guess and hit enter.Beware: you only have 3 tries per riddle to
get it right, otherwise it's game over!\n
BATTLING\n
You have the choice to attack your opponent or defend against your opponent's
attack. If you attack, you deal a random fraction of your character's Attack
Power in damage. If you defend, you regain a random fraction of your
character's Defensive Power back as HP.\n
Attack = Deal damage
Defend = Heal yourself''')
                  break
            else:
                break 
        print('')
        print("Name:", player.name)
        print("Description:", player.description)
        print("Current HP:", player.max_hp)
        print("Attack Power:", player.attack_power)
        print("Defensive Power:", player.defensive_power)
        print('')

        return player


    #if the user enters something that is not A, B, or C,
    #then they will be asked for another input
    except UnboundLocalError:
        print()
        print("Not a valid input.")
        print()
        character_choose()
        


################################################################################
#CHARACTER INTERFACE- JUST FOR REFERENCE
def characterinterface():
    print('-'*31)
    print('Location:', player_location)
    print('Inventory:', inventory)
    #I don't think we will have time to add the inventory code
    print('-'*31)

################################################################################
#MAKING A ROOM AND PUTTING IT IN THE GAME
def make_place(name,description):
    places[name] = {'id': name,
                    'exits': [],
                    'description': description}
################################################################################
#MAKING EXITS BETWEEN ROOMS
def make_exit(from_room, to_room, description):
    places[from_room]['exits'].append({'target': to_room,
                                       'description': description})


################################################################################
#LIST OF ROOMS
#OUTSIDE
make_place('frontlawn','I stare up at the creaky house.')
make_place('frontlawnlook','This street is dead and there is no one around. I wonder who lives in this house.')

#GROUND FLOOR
make_place('entrancehall', 'The door is locked and I don\'t have way out.')
make_place('entrancehalllook', 'The furniture is very out dated.')
make_place('pantry', 'Nothing but moldy food and a couple of mouse traps.')
make_place('pantrylook', 'Nothing of interest.')
make_place('closet', 'Mothballs fly around the closet.')
make_place('closetlook', 'Nothing of interest.')
make_place('livingroom', 'I guess you can\'t do much living in this room if you are dead. Haha. Get it? Because it is a living room?')
make_place('livingroomlook', 'Nothing of interest.')
make_place('dininghall', 'The table is already preset.')
make_place('dininghalllook', 'Nothing of interest.')
make_place('kitchen', 'Why does it smell like food?')
make_place('kitchenlook', 'The oven is on and some of the drawers are open.')
make_place('kitchendrawer1', 'Empty.')
make_place('kitchendrawer2', 'There are matches that might be useful.')
make_place('kitchendrawer3', 'What is in this drawer? A knife! No!')
make_place('kitchenoven', 'Yum. I love eating rocks for dinner.')
make_place('stairsnorth','The stairs creak with every step I take.')
make_place('stairssouth','The stairs are covered with dust and the air is filled with cobwebs.')
make_place('garden', 'It is probably really pretty out here, when it is not the middle of the winter.')
make_place('gardenlook', 'Nothing of interest.')
make_place('outpowerbox', 'Someone left some batteries!')

#BASEMENT
make_place('basementlanding', 'This is the basement.')
make_place('basementlanding', 'I wish I had a light.')
make_place('cellar', 'Someone must have really liked wine.')
make_place('cellarlook', 'Does anyone really need all this wine? What are they doing to do with it? Drink it?')
make_place('cellarbottle1', 'California YEAR')
make_place('cellarbottle2', 'This one is from France!')
make_place('cellarbottle3', 'This one looks like it was opened recently...')
make_place('cellarbottle4', 'What is the harm in taking one?')
make_place('crypt', ' People are supposed to live here!')  
make_place('cryptlook', 'How many people are still in this house?')
make_place('cryptcoffin1', 'Dr. Lawrence Alabaster 1885')
make_place('cryptcoffin2', 'Countess Katrina Zatara 1912')
make_place('cryptcoffin3', 'Doris Alabaster 1878')
make_place('cryptcoffin4', 'Ronald Alabaster 1912')
make_place('furnaceroom', 'It is hot in here, I hope nothing blows up.')
make_place('furnaceroomlook', 'Nothing of interest.')

#2ND FLOOR
make_place('library', 'Wow! This is so big!')
make_place('librarylook', 'There are a bunch of books on the table.')
make_place('librarybook1', 'This book is about plants.')
make_place('librarybook2', 'This book is about ghosts.')
make_place('librarybook3', 'This book is about the stars.')
make_place('parlor', 'The parlor looks a bit messy.')
make_place('parlorlook', 'Nothing of interest.')
make_place('study', 'What important information is in the desk.')
make_place('studylook', 'Nothing of interest.')
make_place('hallway2nd', 'There are portraits lining the walls and their eyes seem to follow me. ')

#TOP FLOOR
make_place('tower', 'Wow, I feel like royalty.')
make_place('towerlook', 'There are a lot of spider webs in here…')
make_place('observatory', 'This room is cluttered but it looks cozy.')
make_place('observatorylook', 'Oh! A Telescope!')
make_place('telescope', 'Look! It is Mars! ')
make_place('rooftop', 'Don’t look down. Don’t look down.')
make_place('rooftoplook', 'Someone is waiting for you.')

###############################################################################################
#LISTS OF EXITS

#OUTSIDE
make_exit('frontlawn', 'entrancehall', 'Enter the house.')
make_exit('frontlawn', 'frontlawnlook', 'Look around.')
make_exit('frontlawnlook', 'frontlawn', 'I\'m done looking around.')

#GROUND FLOOR
make_exit('entrancehall', 'pantry', 'Go into the pantry on the right.')
make_exit('entrancehall', 'closet', 'Go into the closet on the left.')
make_exit('entrancehall', 'livingroom', 'Go into the living room.')
make_exit('entrancehall', 'dininghall', 'Go into the dining room.')
make_exit('entrancehall', 'kitchen', 'Go into the kitchen.')
make_exit('entrancehall', 'entrancehalllook', 'Look around.')
make_exit('entrancehalllook', 'entrancehall', 'I\'m done looking around.')
make_exit('pantry', 'entrancehall', 'Go back to into the foyer.')
make_exit('pantry', 'pantrylook', 'Look around.')
make_exit('pantrylook', 'pantry', 'I\'m done looking around.')
make_exit('closet', 'entrancehall', 'Go back to into the foyer.')
make_exit('closet', 'closetlook', 'Look around.')
make_exit('closetlook', 'closet', 'I\'m done looking around. In other words, come out of the closet ;)')
make_exit('livingroom', 'entrancehall', 'Go into the foyer.')
make_exit('livingroom', 'garden', 'Go into the garden.')
make_exit('livingroom', 'stairsnorth', 'Go up the stairs.')
make_exit('livingroom', 'livingroomlook', 'Look around.')
make_exit('livingroomlook', 'livingroom', 'I\'m done looking around.')
make_exit('dininghall', 'entrancehall', 'Go into the foyer.')
make_exit('dininghall', 'kitchen', 'Go into the kitchen.')
make_exit('dininghall', 'stairssouth', 'Go up the stairs')
make_exit('dininghall', 'dininghalllook', 'Look around.')
make_exit('dininghalllook', 'dininghall', 'I\'m done looking around.')
make_exit('kitchen', 'entrancehall', 'Go into the foyer.')
make_exit('kitchen', 'basementlanding', 'Go down the trap door.')
make_exit('kitchen', 'dininghall', 'Go to the dining hall.')
make_exit('kitchen', 'kitchenlook', 'Look around.')
make_exit('kitchenlook', 'kitchen', 'I\'m done looking around.')
make_exit('kitchenlook', 'kitchendrawer1', 'Drawer 1.')
make_exit('kitchendrawer1', 'kitchenlook', 'Look at something else.')
make_exit('kitchenlook', 'kitchendrawer2', 'Drawer 2.')
make_exit('kitchendrawer2', 'kitchenlook', 'Look at something else.')
make_exit('kitchenlook', 'kitchendrawer3', 'Drawer 3.')
make_exit('kitchendrawer3', 'kitchenlook', 'Look at something else.')
make_exit('kitchenlook', 'kitchenoven', 'Oven.')
make_exit('kitchenoven', 'kitchenlook', 'Look at something else.')
make_exit('stairsnorth', 'livingroom', 'Go to the living room.')
make_exit('stairsnorth', 'parlor', 'Go to the parlor.')
make_exit('stairsnorth', 'tower', 'Go to the tower.')
make_exit('stairssouth', 'dininghall', 'Go to the dining hall.')
make_exit('stairssouth', 'study', 'Go to the study.')
make_exit('stairssouth', 'observatory', 'Go to the observatory.')
make_exit('garden', 'livingroom', 'Go back inside.')
make_exit('garden', 'outpowerbox', 'Go check the power.')
make_exit('garden', 'gardenlook', 'Look around.')
make_exit('gardenlook', 'garden', 'I\'m done looking around.')
make_exit('outpowerbox', 'garden', 'Go back outside.')

#2ND FLOOR
make_exit('study', 'hallway2nd', 'Go into the hallway.')
make_exit('study', 'stairssouth', 'Go to the stairs.')
make_exit('parlor', 'stairsnorth', 'Go to the stairs.')
make_exit('parlor', 'hallway2nd', 'Go into the hallway.')
make_exit('parlor', 'parlorlook', 'Look around.')
make_exit('parlorlook', 'parlor', 'I\'m done looking around.')
make_exit('library', 'hallway2nd', 'Go into the hallway.')
make_exit('library', 'librarylook', 'Look around.')
make_exit('librarylook', 'library', 'I\'m done looking around.')
make_exit('librarylook', 'librarybook1', 'Book 1.')
make_exit('librarybook1', 'librarylook', 'Look at something else.')
make_exit('librarylook', 'librarybook2', 'Book 2.')
make_exit('librarybook2', 'librarylook', 'Look at something else.')
make_exit('librarylook', 'librarybook3', 'Book 3.')
make_exit('librarybook3', 'librarylook', 'Look at something else.')
make_exit('hallway2nd', 'library', 'Go into the library.')
make_exit('hallway2nd', 'study', 'Go into the study.')
make_exit('hallway2nd', 'parlor', 'Go into the parlor.')
#BASEMENT
make_exit('basementlanding', 'kitchen', 'Go back upstairs.')
make_exit('basementlanding', 'cellar', 'Go into the cellar.')
make_exit('basementlanding', 'crypt', 'Go into the crypt.')
make_exit('basementlanding', 'furnaceroom', 'Go into the boiler room.')
make_exit('cellar', 'basementlanding', 'Leave the cellar.')
make_exit('crypt', 'basementlanding', 'Leave the crypt.')
make_exit('furnaceroom', 'basementlanding', 'Leave the boiler room.')
make_exit('cellar', 'cellarlook', 'Look around.')
make_exit('cellarlook', 'cellar', 'I\'m done looking around.')
make_exit('cellarlook', 'cellarbottle1', 'Bottle 1.')
make_exit('cellarbottle1', 'cellarlook', 'Look at something else.')
make_exit('cellarlook', 'cellarbottle2', 'Bottle 2.')
make_exit('cellarbottle2', 'cellarlook', 'Look at something else.')
make_exit('cellarlook', 'cellarbottle3', 'Bottle 3')
make_exit('cellarbottle3', 'cellarlook', 'Look at something else.')
make_exit('cellarlook', 'cellarbottle4', 'Bottle 4.')
make_exit('cellarbottle4', 'cellarlook', 'Look at something else.')
make_exit('crypt', 'cryptlook', 'Look around.')
make_exit('cryptlook', 'crypt', 'I\'m done looking around.')
make_exit('cryptlook', 'cryptcoffin1', 'Coffin 1.')
make_exit('cryptcoffin1', 'cryptlook', 'Look at something else.')
make_exit('cryptlook', 'cryptcoffin2', 'Coffin 2.')
make_exit('cryptcoffin2', 'cryptlook', 'Look at something else.')
make_exit('cryptlook', 'cryptcoffin3', 'Coffin 3.')
make_exit('cryptcoffin3', 'cryptlook', 'Look at something else.')
make_exit('cryptlook', 'cryptcoffin4', 'Coffin 4.')
make_exit('cryptcoffin4', 'cryptlook', 'Look at something else.')
make_exit('furnaceroom', 'furnaceroomlook', 'Look around.')
make_exit('furnaceroomlook', 'furnaceroom', 'I\'m done looking around.')

#TOP FLOOR
make_exit('observatory', 'stairssouth', 'Go down the stairs.')
make_exit('observatory', 'observatorylook', 'Look around.')
make_exit('observatorylook', 'observatory', 'I\'m done looking around.')
make_exit('observatorylook', 'telescope', 'Oh!')
make_exit('telescope', 'observatorylook', '')
make_exit('tower', 'stairsnorth', 'Go down the stairs.')
make_exit('tower', 'towerlook', 'Look around.')
make_exit('towerlook', 'tower', 'I\'m done looking around.')
make_exit('rooftop', 'observatory', 'Go into the observatory.')
make_exit('rooftop', 'tower', 'Go into the tower.')
make_exit('tower', 'rooftop', 'Go out onto the roof.')
make_exit('observatory', 'rooftop', 'Go out onto the roof.')
make_exit('tower', 'rooftop', 'Go out onto the roof.')
make_exit('observatory', 'rooftop', 'Go out onto the roof.')

################################################################################
#INVENTORY ADDITIONS
def inventory_add():
#find matches
    if player_location == 'kitchendrawer2':
        item = 'matches'
        if item in inventory:
            print('You already have this item.')
        else:
            inventory.append('matches')
            print('You have found a matches!')
#find winebottle
    if player_location == 'cellerbottle4':
        item = 'wine bottle'
        if item in inventory:
            print('You already have this item.')
        else:
            inventory.append('wine bottle')
            print('You have found a wine bottle!')
#find flash light
    if player_location == 'closet':
        item = 'flash light'
        if item in inventory:
            print('You already have this item.')
        else:
            inventory.append('flash light')
            print('You have found a flashlight!')
#find batteries
    if player_location == 'outpowerbox':
        item = 'batteries'
        if item in inventory:
            print('You already have this item.')
        else:
            inventory.append('batteries')
            print('You have found some batteries!')
#find key
    if player_location == 'librarybook3':
        item = 'key'
        if item in inventory:
            print('You already have this item.')
        else:
            inventory.append('key')
            print('You have found a key!')

################################################################################
#GAMEPLAY - EXIT AND LOCATION DESCRIPTION
def ask_user_which_exit(exits,inventory):
        
    try:
        print('Options:')
        for i in range(len(exits)):
            print(i+1, exits[i]['description'])
        choice = eval(input('Choose:'))
        if exits[choice-1]['target'] == 'basementlanding' and ('batteries' not in inventory or 'flash light' not in inventory):
            print('''It\'s too dark to see anything. Maybe I should find a flashlight
and some batteries...''')
            return ask_user_which_exit(exits,inventory)
        if exits[choice-1]['target'] == 'tower' and ('key' not in inventory):
            print('It\'s locked. I should find a key.')
            return ask_user_which_exit(exits,inventory)
        if exits[choice-1]['target'] == 'observatory' and ('key' not in inventory):
            print('It\'s locked. I should find a key.')
            return ask_user_which_exit(exits,inventory)
        return exits[choice-1]['target']
        #player_location = ['target']
        

    except TypeError:
        print()
        print("Not a valid input. Try again.")
        print()
        return ask_user_which_exit(exits,inventory)
        print_location_description()

    #exception if player enters a number out of range     
    except IndexError:
        print()
        print("Not a valid input. Try again.")
        print()
        return ask_user_which_exit(exits,inventory)
        print_location_description()

    #exception if player enters a letter instead of a number
    except NameError:
        print()
        print("Not a valid input. Try again.")
        print()
        return ask_user_which_exit(exits,inventory)
        print_location_description()

    #exception if player presses enter without writing anything first 
    except SyntaxError:
        print()
        print("Not a valid input. Try again.")
        print()
        return ask_user_which_exit(exits,inventory)
        print_location_description()

def print_location_description():

     
    #print(player_location)
    room = places[player_location]
    print(room['description'])
    exits = room['exits']
    #print(exits)


    #gives a KeyError: None - not sure how to fix this one 
    

#RIDDLE
def riddle():
    complete_riddle = {'riddle':'answer'}
    riddles = {"What word begins and ends in E but only has one letter?" : "envelope",
               "I’m tall when I’m young and I’m short when I’m old. What am I?" : "candle",
               "What has hands but can’t clap?" : "clock",
               "What starts with the letter T, is full of T and ends with the letter T?" : "teapot",
               "What goes up but never goes down?" : "age",
               "What has one eye but cannot see?" : "needle",
               "The more you take, the more you leave behind, what am I?" : "footprints",
               "What is so delicate that saying its name breaks it?" : "silcence",
               "Where there is light is the only place I can live. Yet if light shines on me I die." : "shadow"}
    riddle = random.choice(list(riddles.keys()))
    answer = riddles[riddle]
    print ("Riddle Rules: You have 3 tries to solve this riddle, all solutions are one word, enter answers in lowercase")
    print()
    print ("Here is your riddle: ", riddle)
    print()
    user_answer = input("Your answer: ")

    counter = 0
    while user_answer: 
        if user_answer == answer:
            print ("You may continue...")
            break
        elif user_answer != answer and counter < 2:
            print("Wrong Answer, try again.")
            user_answer = input("Your answer: ")
            counter += 1
        elif user_answer != answer and counter >= 2:
            print("Wrong answer and you are out of tries... \n")
            return True

################################################################################
#MONSTER AND RIDDLE ROOMS
def monster_rooms():
    if player_location == 'entrancehall' or 'crypt' or 'parlor' or 'stairssouth' 'cryptcoffin4' or 'tower':
        if player_location == 'entrancehall':
            dustbunny = DustBunny('room')
            player.battle(dustbunny)
        if player_location == 'crypt':
            ghost = Ghost('room')
            player.battle(ghost)
        if player_location == 'parlor':
            batswarm = BatSwarm('room')
            player.battle(batswarm)
        if player_location == 'stairssouth':
            dustbunny = DustBunny('room')
            player.battle(dustbunny)
        if player_location == 'cryptcoffin4':
            banshee = Banshee('room')
            player.battle(banshee)
        if player_location == 'rooftop':
            armor = Armor('room')
            player.battle(armor)
            if player.current_hp<=0:
                    return True
            if armor.current_hp<=0:
                print('''The Suit of Armor crashes to the ground. A gust of wind almost pushes you over
as you hear all the doors swing wide open. It appears that the armor has been
the guardian of the manor for quite some time. You make your way back downstairs
and make your way to the front door. You leave the manor victorious.''')
                return True
                
def riddle_rooms(riddle_wrong):
    riddle_wrong = riddle_wrong
    if player_location == 'cellar' or 'library' or 'observatory':
        counter = 0
        if player_location == 'cellar':
            counter =+ 1
            if counter > 1:
                print("You have already defeated this challenge.")
            else:
                riddle_wrong=riddle()
                if riddle_wrong==True:
                    print('''You feel a phantasmal force push you over and you are quickly
consumed by a swarm of rats.
                            GAME OVER''')
                    return riddle_wrong
        counter = 0
        if player_location == 'library':
            counter =+ 1
            if counter > 1:
                print("You have already defeated this challenge.")
            else:
                riddle_wrong=riddle()
                if riddle_wrong==True:
                    print('''You head a loud crack and piles of books fall on you.
GAME OVER''')
                    return riddle_wrong
        counter = 0
        if player_location == 'observatory':
            counter =+ 1
            if counter > 1:
                print("You have already defeated this challenge.")
            else:
                riddle_wrong=riddle()
                if riddle_wrong == True:
                    print('''In a freak accident a meteor hits the observatory.
GAME OVER''')
                    return riddle_wrong
################################################################################
#END OF GAME
#initializing gameover variables
game_over = False
monsters = False
riddle_wrong = False

opening_graphic()
player=character_choose()
#sleep(12)
print('''You are walking along a winding path in the woods and hear a clamor
to the west. You walk in its direction and find a mansion. You realize
you have finally found Alabastor Manor. For all the rumors, it looks
warm and friendly, but you know it to be neither of those things. You
swallow your fear and walk up to the front door.''')
#sleep(10)

while game_over !=True and monsters != True and riddle_wrong != True :
    characterinterface()
    riddle_wrong = riddle_rooms(riddle_wrong)
    if riddle_wrong == True:
        break
    monsters = monster_rooms()
    if monsters == True:
        break
    print_location_description()
    inventory_add()
    #room_rejection()
    player_location = ask_user_which_exit(places[player_location]['exits'], inventory)
