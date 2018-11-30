places = {}
inventory = []

################################################################################
#THIS IS WHERE THE PLAYER STARTS
player_location = 'frontlawn'

################################################################################
#CHARACTER INTERFACE- JUST FOR REFERENCE
def characterinterface():
    print('-'*len(player_location) + '-'*10)
    print('Location:', player_location)
    print('Inventory:', inventory)
    print('-'*len(player_location)+'-'*10)

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
#INVENTORY ADDITIONS
def inventory_add():
#find matches
    if player_location == 'kitchendrawer2':
        item = 'matches'
        if item in inventory:
            print('You already have this item.')
        else:
            inventory.append('matches')
            print('You have found matches!')
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
            print('You have found batteries!')

################################################################################
#LIST OF ROOMS
#OUTSIDE
make_place('frontlawn','I stare up at the creaky house.')
make_place('frontlawnlook','This street is dead and there is no one around. I wonder who lives in this house.')
#GROUND FLOOR
make_place('entrancehall', 'The door is locked and I do not have way out.')
make_place('entrancehalllook', 'The furniture is very out dated.')
make_place('pantry', 'Nothing but moldy food and a couple of mouse traps.')
make_place('pantrylook', 'Nothing of interest.')
make_place('closet', 'Mothballs fly around the closet.')
make_place('closetlook', 'Nothing of interest.')
make_place('livingroom', 'I guess you can not do much living in this room if you are dead. Haha. Get it? Because it is a living room?')
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
if 'flash light' and 'batteries' in inventory:
	make_place('basementlanding', 'This is the basement.')
else:
    make_place('basementlanding', 'I wish I had a light.')
make_place('cellar', 'Someone must have really liked wine.')
make_place('cellarlook', 'Does anyone really need all this wine? What are they doing to do with it? Drink it?')
make_place('cellarbottle1', 'California YEAR')
make_place('cellarbottle2', 'This one is from France!')
make_place('cellarbottle3', 'This one looks like it was opened recently...')
make_place('cellarbottle4', 'What is the harm in taking one?')
make_place('crypt', ' People are supposed to live here!')  
make_place('cryptlook', 'How many people are still in this house?')
make_place('cryptcoffin1', 'NAME YEAR')
make_place('cryptcoffin2', 'NAME YEAR')
make_place('cryptcoffin3', 'NAME YEAR')
make_place('cryptcoffin4', 'NAME YEAR')
make_place('furnaceroom', 'It is hot in here, I hope nothing blows up.')
make_place('furnaceroomlook', 'Nothing of interest.')
#3RD FLOOR
##make_place('generalbedroom', ' ')
##make_place('masterbedroomnorth', '')
##make_place('masterbedroomsouth', '')
##make_place('childrenbedroom', '')
##make_place('childrenbedroomlook', 'All of the old toys litter the floor.')
##make_place('guestbedroom', '')
##make_place('extrabedroom','')
##make_place('masterbathroomnorth', '')
##make_place('masterbathroomsouth', '')
##make_place('bathroom3rd', '')
##make_place('hallway3rd', '')
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

################################################################################
#LISTS OF EXITS
#OUTSIDE
make_exit('frontlawn', 'entrancehall', 'Enter the house.')
#make_exit('frontlawn', 'frontlawnlook', 'Look around.')
#GROUND FLOOR
make_exit('entrancehall', 'pantry', 'Go into the pantry on the right.')
make_exit('entrancehall', 'closet', 'Go into the closet on the left.')
make_exit('entrancehall', 'livingroom', 'Go into the living room.')
make_exit('entrancehall', 'dininghall', 'Go into the dining room.')
make_exit('entrancehall', 'kitchen', 'Go into the kitchen.')
make_exit('pantry', 'entrancehall', 'Go back to into the foyer.')
make_exit('closet', 'entrancehall', 'Go back to into the foyer.')
make_exit('livingroom', 'entrancehall', 'Go into the foyer.')
make_exit('livingroom', 'garden', 'Go into the garden.')
make_exit('livingroom', 'stairsnorth', 'Go up the stairs.')
make_exit('dininghall', 'entrancehall', 'Go into the foyer.')
make_exit('dininghall', 'kitchen', 'Go into the kitchen.')
make_exit('dininghall', 'stairssouth', 'Go up the stairs')
make_exit('kitchen', 'entrancehall', 'Go into the foyer.')
make_exit('kitchen', 'basementlanding', 'Go down the trap door.')
make_exit('kitchen', 'dininghall', 'Go to the dining hall.')
make_exit('stairsnorth', 'livingroom', 'Go to the living room.')
make_exit('stairsnorth', 'parlor', 'Go to the parlor.')
#make_exit('stairsnorth', 'hallway3rd', 'Go to the third floor.')
make_exit('stairsnorth', 'tower', 'Go to the tower.')
make_exit('stairssouth', 'dininghall', 'Go to the dining hall.')
make_exit('stairssouth', 'study', 'Go to the study.')
#make_exit('stairssouth', 'hallway3rd', 'Go to the third floor.')
make_exit('stairssouth', 'observatory', 'Go to the observatory.')
make_exit('garden', 'livingroom', 'Go back inside.')
make_exit('garden', 'outpowerbox', 'Go check the power.')
make_exit('outpowerbox', 'garden', 'Go back outside.')
#2ND FLOOR
make_exit('study', 'hallway2nd', 'Go into the hallway.')
make_exit('study', 'stairssouth', 'Go to the stairs.')
make_exit('parlor', 'stairsnorth', 'Go to the stairs.')
make_exit('parlor', 'hallway2nd', 'Go into the hallway.')
make_exit('library', 'hallway2nd', 'Go into the hallway.')
make_exit('hallway2nd', 'library', 'Go into the library.')
make_exit('hallway2nd', 'study', 'Go into the study.')
make_exit('hallway2nd', 'parlor', 'Go into the parlor.')
#3RD FLOOR
##make_exit('hallway3rd', 'masterbedroomnorth', 'Go into the master bedroom on the right.')
##make_exit('hallway3rd', 'masterbedroomsouth', 'Go into the master bedroom on the left.')
##make_exit('hallway3rd', 'generalbedroom', 'Go into the bedroom down the hall.')
##make_exit('hallway3rd', 'childrenbedroom', "Go into the children's bedroom.")
##make_exit('hallway3rd', 'guestbedroom', 'Go into the guest bedroom.')
##make_exit('hallway3rd', 'extrabedroom', 'Go into the extra bedroom.')
##make_exit('hallway3rd', 'bathroom3rd', 'Go into the bathroom.')
##make_exit('hallway3rd', 'stairsnorth', 'Go to the stairs.')
##make_exit('hallway3rd', 'stairssouth', 'Go to the stairs.')
##make_exit('masterbedroomnorth', 'hallway3rd', 'Go into the hallway.')
##make_exit('masterbedroomnorth', 'masterbathroomnorth', 'Go into the master bathroom.')
##make_exit('masterbathroomnorth', 'masterbedroomnorth', 'Go into the master bedroom.')
##make_exit('masterbedroomsouth', 'hallway3rd', 'Go into the hallway.')
##make_exit('masterbedroomsouth', 'masterbathroomsouth', 'Go into the master bathroom.')
##make_exit('masterbathroomsouth', 'masterbedroomsouth', 'Go into the master bedroom.')
##make_exit('generalbedroom', 'hallway3rd', 'Go into the hallway.')
##make_exit('childrenbedroom', 'hallway3rd', 'Go into the hallway.')
##make_exit('guestbedroom', 'hallway3rd', 'Go into the hallway.')
##make_exit('extrabedroom', 'hallway3rd', 'Go into the hallway.')
##make_exit('bathroom3rd', 'hallway3rd', 'Go into the hallway.')
#BASEMENT
make_exit('basementlanding', 'kitchen', 'Go back upstairs.')
make_exit('basementlanding', 'cellar', 'Go into the cellar.')
make_exit('basementlanding', 'crypt', 'Go into the crypt.')
make_exit('basementlanding', 'furnaceroom', 'Go into the boiler room.')
make_exit('cellar', 'basementlanding', 'Leave the cellar.')
make_exit('crypt', 'basementlanding', 'Leave the crypt.')
make_exit('furnaceroom', 'basementlanding', 'Leave the boiler room.')
#TOP FLOOR
make_exit('observatory', 'rooftop', 'Go out onto the roof.')
make_exit('observatory', 'stairssouth', 'Go down the stairs.')
make_exit('rooftop', 'observatory', 'Go into the observatory.')
make_exit('rooftop', 'tower', 'Go into the tower.')
make_exit('tower', 'rooftop', 'Go out onto the roof.')
make_exit('tower', 'stairsnorth', 'Go down the stairs.')

##HAVE TO FINISH GOING INTO ROOMS AND THE LOOK FUNCTION FOR ALMOST ALL

################################################################################
#GAMEPLAY- WHICH EXIT AND LOCATION DESCRIPTION
def ask_user_which_exit(exits):
    print('Options:')
    for i in range(len(exits)):
        print(i+1, exits[i]['description'])
    choice = eval(input('Choose:'))
    return exits[choice-1]['target']
    player_location = ['target']

def print_location_description():
    #print(player_location)
    room = places[player_location]
    print(room['description'])
    exits = room['exits']
    #print(exits)

################################################################################
#INVENTORY NEEDED TO ENTER ROOM
def room_rejection():
    if 'flash light' and 'batteries' not in inventory:
        #want to block certain exits (celler, crypt, furnaceroom)
    if 'key' not in inventory:
        #open the third floor? or opens onto the roof?
    
################################################################################
#END OF GAME - NOT SET YET
game_over = False
while not game_over:
    characterinterface()
    print_location_description()
    inventory_add()
    player_location = ask_user_which_exit(places[player_location]['exits'])
