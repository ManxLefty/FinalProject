from graphics import *
import time

WIDTH = 300
HEIGHT = 300
RADIUS = 10
def main():
    # Create window
    win = GraphWin('Bouncing ball',WIDTH, HEIGHT)

    # Create ball
    ball = Circle(Point(10,10),RADIUS)
    ball.setFill('red')

    # Draw ball to window
    ball.draw(win)

    win.getMouse()

    #Delta variables
    dx = 3
    dy = 5
    # Animate the ball
    while (win.checkMouse()==None):
        ball.move(dx,dy)
        time.sleep(0.05)
        
        # Make sure the whole ball stays on the screen
        if (ball.getCenter().getX() > WIDTH-RADIUS
            or ball.getCenter().getX()< RADIUS):
            dx = -1*dx
        if( ball.getCenter().getY() > HEIGHT-RADIUS
            or ball.getCenter().getY() < RADIUS):
            dy = -1*dy


if __name__=='__main__':
    main()
