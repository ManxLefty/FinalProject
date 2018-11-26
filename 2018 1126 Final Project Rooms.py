places = {}
def make_place(name,description):
    #putting the room into the game
    #making the room:
    places[name] = {'id': name,
                    'exits': [],
                    'description': description}

def make_exit(from_room, to_room, description):
    places[from_room]['exits'].append({'target': to_room,
                                       'description': description})

#create rooms
make_place('frontlawn','You stare up at the creaky house.')
    
make_place('entrancehall', '')
make_place('pantry', '<blank>')
make_place('closet', '<blank>')
make_place('livingroom', '<blank>')
make_place('dininghall', '<blank>')
make_place('kitchen', '<blank>')
make_place('stairsnorth','The stairs creak with everystep you take.')
make_place('stairssouth','The stairs are covered with dust and the air is filled with cobwebs.')
make_place('garden', '')
make_place('outpowerbox','')

make_place('basementlanding', '')
make_place('cellar', '')
make_place('crypt', 'Why would anyone make something like this in a house? People are suppose to live here!')
make_place('furnaceroom', '')

make_place('generalbedroom', '')
make_place('masterbedroomnorth', '')
make_place('masterbedroomsouth', '')
make_place('childrenbedroom', '')
make_place('guestbedroom', '')
make_place('extrabedroom','')
make_place('masterbathroomnorth', '')
make_place('masterbathroomsouth', '')
make_place('bathroom3rd', '')
make_place('hallway3rd', 'Portraits line the walls and their eyes seem to follow you.')

make_place('library', '')
make_place('parlor', '')
make_place('study', '')
make_place('hallway2nd', '')

make_place('tower', '')
make_place('observatory', 'It is a quiet room with a telescope pointed up towards the sky.')
make_place('rooftop', 'Someone is waiting for you.')

#if else based on inventoery if you can enter the room (example Key or flashlight)


#create exits
make_exit('frontlawn', 'entrancehall', 'Knock on the door.')

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
make_exit('kitchen', 'entrancehall', 'Go in to foyer.')
make_exit('kitchen', 'basementlanding', 'Go down the trap door.')
make_exit('kitchen', 'dininghall', 'Go into the dining hall.')
make_exit('stairsnorth', 'livingroom', 'Go to the living room.')
make_exit('stairsnorth', 'parlor', 'Go to the parlor.')
make_exit('stairsnorth', 'hallway3rd', 'Go to the third floor.')
make_exit('stairsnorth', 'tower', 'Go to the tower.')
make_exit('stairssouth', 'dininghall', 'Go to the dining hall.')
make_exit('stairssouth', 'study', 'Go to the study.')
make_exit('stairssouth', 'hallway3rd', 'Go to the third floor.')
make_exit('stairssouth', 'observatory', 'Go to the observatory.')
make_exit('garden', 'livingroom', 'Go back inside.')
make_exit('garden', 'outpowerbox', 'Go check the power.')
make_exit('outpowerbox', 'garden', 'Go back outside.')

make_exit('study', 'hallway2nd', 'Go into the hallway.')
make_exit('study', 'stairssouth', 'Go to the stairs.')
make_exit('parlor', 'stairsnorth', 'Go to the stairs.')
make_exit('parlor', 'hallway2nd', 'Go into the hallway.')
make_exit('library', 'hallway2nd', 'Go into the hallway.')
make_exit('hallway2nd', 'library', 'Go into the library.')
make_exit('hallway2nd', 'study', 'Go into the study.')
make_exit('hallway2nd', 'parlor', 'Go into the parlor.')

make_exit('hallway3rd', 'masterbedroomnorth', 'Go into the master bedroom on the right.')
make_exit('hallway3rd', 'masterbedroomsouth', 'Go inot the master bedroom on the left.')
make_exit('hallway3rd', 'generalbedroom', 'Go into the bedroom down the hall.')
make_exit('hallway3rd', 'childrenbedroom', "Go into the children's bedroom.")
make_exit('hallway3rd', 'guestbedroom', 'Go into the guest bedroom.')
make_exit('hallway3rd', 'extrabedroom', 'Go into the extra bedroom.')
make_exit('hallway3rd', 'bathroom3rd', 'Go into the bathroom.')
make_exit('hallway3rd', 'stairsnorth', 'Go to the stairs.')
make_exit('hallway3rd', 'stairssouth', 'Go to the stairs.')
make_exit('masterbedroomnorth', 'hallway3rd', 'Go into the hallway.')
make_exit('masterbedroomnorth', 'masterbathroomnorth', 'Go into the bathroom.')
make_exit('masterbathroomnorth', 'masterbedroomnorth', 'Go into the bathroom.')
make_exit('masterbedroomsouth', 'hallway3rd', 'Go into the hallway.')
make_exit('masterbedroomsouth', 'masterbathroomsouth', 'Go into the master bedroom.')
make_exit('masterbathroomsouth', 'masterbedroomsouth', 'Go into the master bedroom.')
make_exit('generalbedroom', 'hallway3rd', 'Go into the hallway.')
make_exit('childrenbedroom', 'hallway3rd', 'Go into the hallway.')
make_exit('guestbedroom', 'hallway3rd', 'Go into the hallway.')
make_exit('extrabedroom', 'hallway3rd', 'Go into the hallway.')
make_exit('bathroom3rd', 'hallway3rd', 'Go into the hallway.')

make_exit('basementlanding', 'kitchen', 'Go back upstairs.')
make_exit('basementlanding', 'cellar', 'Go into the cellar.')
make_exit('basementlanding', 'crypt', 'Go inot the crypt.')
make_exit('basementlanding', 'furnaceroom', 'Go into the boiler room.')
make_exit('cellar', 'basementlanding', 'Leave the cellar.')
make_exit('crypt', 'basementlanding', 'Leave the crypt.')
make_exit('furnaceroom', 'basementlanding', 'Leave the boiler room.')

make_exit('observatory', 'rooftop', 'Go out onto the roof.')
make_exit('observatory', 'stairssouth', 'Go out onto the roof.')
make_exit('rooftop', 'observatory', 'Go to the observatory.')
make_exit('rooftop', 'tower', 'Go to the tower.')
make_exit('tower', 'rooftop', 'Go out onto the roof.')
make_exit('tower', 'stairsnorth', 'Go down the stairs.')

def ask_user_which_exit(exits):
    print('There are some exits')
    for i in range(len(exits)):
        print(i+1, exits[i]['description'])
    choice = eval(input('Choose:'))
    return exits[choice-1]['target']
        
#this is where the player starts
player_location = 'frontlawn'

def print_location_description():
    #print(player_location)
    room = places[player_location]
    print(room['description'])
    exits = room['exits']
    #print(exits)

game_over = False
while not game_over:
    print_location_description()
    player_location = ask_user_which_exit(places[player_location]['exits'])
    print_location_description()
