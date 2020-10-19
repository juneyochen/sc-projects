"""
File: 
Name: June-Yo Chen
-------------------------
This file create a ball and let it move with the gravity just like in the reality.
The ball will move from the left hand side to the right hand side with falling and reflecting behavior.
The function will move up to three times as the maximum number that user can operate.
During the the moving period, user cannot do other operation with the file.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3           # speed of the ball in x direction
DELAY = 50       # delay time between each move
GRAVITY = 1      # the acceleration speed in y direction
SIZE = 20        # the diameter of the ball
REDUCE = 0.9     # the reflecting ratio of the original height
START_X = 30     # the x position of the starting point
START_Y = 40     # the y position of the starting point

window = GWindow(800, 500, title='bouncing_ball.py')  # create a window for the function
life = 3         # the maximum number that user can operate
switch = 1       # the switch for letting user not operate during the ball moving


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)  # create a circle as the ball
    ball.filled = True                              # filled the ball with black color
    window.add(ball)                                # put the ball on the window
    onmouseclicked(move_function)                   # whenever the mouse clicks, the ball starts to move


def move_function(m):
    global life, switch                             # use the variables on the upper side of def main()
    while life > 0 and switch == 1:                 # the condition to determine whether the ball can move or not
        original_ball = window.get_object_at(x=START_X + SIZE/2, y=START_Y + SIZE/2)  # select the ball at the original position
        window.remove(original_ball)                # remove the ball at the original position
        life -= 1                                   # life number minus one
        switch *= -1                                # switch turns off, which let user not operate during the ball moving
        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)  # create the ball that will move later
        ball.filled = True                          # fill the ball with black color
        window.add(ball)                            # put the ball that will move later on the window
        x_speed = VX                                # control the speed of the ball at x direction
        y_speed = 0                                 # control the speed of the ball at y direction
        height = window.height - START_Y            # the height of the ball at the original position
        while True:
            y_speed += GRAVITY                      # speed at y direction will be changed due to the gravity
            height *= REDUCE                        # reflecting height will decrease when the ball touches to the ground
            ball.move(x_speed, y_speed)             # give the ball the speeds at x and y direction
            pause(DELAY)                            # give a delay time that human can see the moving of the ball
            if ball.y >= (window.height - SIZE) or ball.y <= height:  # the condition that ball will reflect
                y_speed = -1 * y_speed              # the speed of y direction will be changed at every reflection
            if ball.x >= window.width:              # if the ball moves out of the window.width, it will stop
                window.add(ball, x=START_X, y=START_Y)  # put a ball on the original position that will move next time
                switch *= -1                        # turn on the switch that user can operate
                break
        if switch == 1:                             # break the while loop and ready for the next move (next mouse click)
            break



if __name__ == "__main__":
    main()
