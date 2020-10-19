"""
File: 
Name:June-Yo Chen
-------------------------
This file help user draw lines on the window. When the mouse points at the window,
the point will be the first point of the line. Then, when the mouse points the second
time, the point will be the end point of the line.
Reminder:
As the first point is created, there will be a circle on the point.
Then when the second point was selected, the circle of the first point
will disappear.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 20           # the size of the circle of first point

window = GWindow()  # the window created for the drawing
x = 0               # X used for saving the X position of first point
y = 0               # y used for saving the Y position of first point
count = 0           # count used as the switch to distinguish the the first point or second point


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(point)           # the mouse clicked function


def point(mouse):
    global x, y, count                                  # the parameters are on the upper side of def main()
    count += 1                                          # count will record the how many times that user clicked the mouse
    if count % 2 != 0:                                  # if the count is odd, the point should be the first point
        hole1 = GOval(SIZE, SIZE)                       # create a hole on the first point. SIZE is the diameter of the circle
        hole1.filled = True                             # fill the hole with black color
        hole1.fill_color = 'white'                      # change the color into white like the topic
        x = mouse.x                                     # the x position of first point
        y = mouse.y                                     # the y position of second point
        window.add(hole1, x - SIZE / 2, y - SIZE / 2)   # put the hole on the window at the center of the first position
    else:                                               # if the count is even, the point should be second point
        hole = window.get_object_at(x, y)               # in order to remove the first hole, we need to choose it
        window.remove(hole)                             # remove the hole at first position
        line_final = GLine(x, y, mouse.x, mouse.y)      # create a line between first position and second position
        window.add(line_final)                          # put the line on the window


if __name__ == "__main__":
    main()
