#graphics for csc final project

from graphics import *
from time import sleep
from random import randint 

def graphics_for_game():
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

    #dustbunny
    dustbunnyImage = Image(Point(300,300),"dustbunny.png")
    dustbunnyImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #swarm_of_bats
    swarm_of_batsImage = Image(Point(300,300),"swarmofbats.png")
    swarm_of_batsImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #ghost
    ghostImage = Image(Point(300,300),"ghost.png")
    ghostImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #banshee
    bansheeImage = Image(Point(300,300),"banshee.png")
    bansheeImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #armor
    armorImage = Image(Point(300,300),"armor.png")
    armorImage.draw(win)
    sleep(1)
    win.close()

    #create a window
    win = GraphWin("Escape from Alabastor Manor", WIDTH, HEIGHT)

    #Manor Map
    ManorMapImage = Image(Point(300,300),"ManorMap.png")
    ManorMapImage.draw(win)


def main():
    graphics_for_game()


if __name__=="__main__":
    main()


#REFERENCES
#http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html

