#graphics for csc final project

from graphics import *
import time
from random import randint 

def graphics_for_game():
    print("Welcome to Alabastor Manor")

    WIDTH = 600
    HEIGHT = 600 

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #drawing lines - http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html
    vertical_line = Line(Point(300,0), Point(300,400))
    vertical_line.draw(win)

    horizontal_line = Line(Point(0,400), Point(600,400))
    horizontal_line.draw(win)

    #choosing a character 
    character_selection = input("Which character would you like to be? Options: Juicebox, Desdemona, Salem: ")
        
    if character_selection == "Juicebox":
        #juicebox  
        juiceboxImage = Image(Point(150,200),"juicebox.png")
        juiceboxImage.draw(win)

    elif character_selection == "Desdemona":
        #desdemona
        desdemonaImage = Image(Point(100,200),"desdemona.png")
        desdemonaImage.draw(win)

    elif character_selection == "Salem":
        #salem
        salemImage = Image(Point(100,200),"salem.png")
        salemImage.draw(win)
    else:
        print("Not a valid character please try again.")
        character_selection = input("Which character would you like to be? Options: Juicebox, Desdemona, Salem: ")

    #monster to fight
    #I would like to randomly generate a monster - is there a random monster generator somewhere else in the code?

    monster_to_face = input("Who do you want to battle? dustbunny, swarm of bats, ghost, banshee, armor: ")

    if monster_to_face == "dustbunny":
        #dustbunny
        dustbunnyImage = Image(Point(450,200),"dustbunny.png")
        dustbunnyImage.draw(win)
        
    elif monster_to_face == "swarm of bats":
        #swarm_of_bats
        swarm_of_batsImage = Image(Point(450,200),"swarmofbats.png")
        swarm_of_batsImage.draw(win)

    elif monster_to_face == "ghost":
        #ghost
        ghostImage = Image(Point(450,200),"ghost.png")
        ghostImage.draw(win)

    elif monster_to_face == "banshee":
        #banshee
        bansheeImage = Image(Point(450,200),"banshee.png")
        bansheeImage.draw(win)

    elif monster_to_face == "armor":
        #armor
        armorImage = Image(Point(450,200),"armor.png")
        armorImage.draw(win)
    
    #graphics for the map
    #first_floor_map
    ##first_floor_map = Image(Point(x,y),"")
    ##first_floor_map.draw(win)
    ##
    ###second_floor_map
    ##second_floor_map = Image(Point(x,y),"")
    ##second_floor_map.draw(win)

def main():
    graphics_for_game()


if __name__=="__main__":
    main()


#when you click
#clickedPt = win.getMouse()

#REFERENCES
#http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html

