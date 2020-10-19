"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.



class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        # set the dimension of the paddle and fill the color of the paddle.
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-PADDLE_WIDTH)/2, window_height-PADDLE_HEIGHT-PADDLE_OFFSET)
        # Center a filled ball in the graphical window.
        # set the dimension of the ball and fill the color of the ball
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.window.add(self.ball, window_width / 2 - BALL_RADIUS, window_height / 2 - BALL_RADIUS)
        # Default initial velocity for the ball.
        # Initialize our mouse listeners.
        # set the mouse function and the velocities of x-direction and y-direction
        onmouseclicked(self.start)
        onmousemoved(self.reset)
        self.__dx = 0
        self.__dy = 0
        # set the score for counting how many bricks does the user break
        self.score = 0
        # set the max score for ending the game
        self.max_score = BRICK_COLS * BRICK_COLS

        # Draw bricks.
        # use the row and column to draw the bricks. With different rows, the colors are different.
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.bricks.filled = True
                if 0 <= j < 2:
                    self.bricks.fill_color = 'red'
                elif 2 <= j < 4:
                    self.bricks.fill_color = 'orange'
                elif 4 <= j < 6:
                    self.bricks.fill_color = 'yellow'
                elif 6 <= j < 8:
                    self.bricks.fill_color = 'green'
                elif 8 <= j < 10:
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, 0+(BRICK_SPACING+BRICK_WIDTH)*i, 0+(BRICK_SPACING+BRICK_HEIGHT)*j)

    def reset(self, mouse):
        """
        let the paddle is controlled by the mouse.
        only the x-direction will move.
        the paddle cannot move out side of the window.
        """
        self.paddle.x = mouse.x - PADDLE_WIDTH / 2
        if self.paddle.x >= (self.window.width - PADDLE_WIDTH):
            self.paddle.x = self.window.width - PADDLE_WIDTH
        if self.paddle.x <= 0:
            self.paddle.x = 0

    def start(self, mouse):
        """
        when the mouse is clicked, give the ball velocities of x direction and y direction.
        also, let the velocity of x-direction change randomly.
        users cannot directly get the velocities of x-direction and y-direction.
        """
        random_x = random.randint(1, MAX_X_SPEED)
        self.__dx = random_x
        if (random.random() > 0.5):
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED

    def get_vx(self):
        """
        let user can get the velocity of x-direction.
        """
        return self.__dx

    def get_vy(self):
        """
        let user can get the velocity of y-direction.
        """
        return self.__dy

    def object_check(self):
        """
        set the reflection of the ball.
        when there are something touched to the four points of the ball, the ball will reflect.
        """
        if self.ball.y <= (self.window.height - PADDLE_OFFSET):  # prevention of the ball touching to the label
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self.__dy = -self.__dy
            elif self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y) is not None:
                self.__dy = -self.__dy
            elif self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS*2) is not None:
                self.__dy = -self.__dy
            elif self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y + BALL_RADIUS*2) is not None:
                self.__dy = -self.__dy

    def eliminate_brick(self):
        """
        when the ball touches bricks, eliminate the bricks
        """
        # bricks are on the top side of the window.
        # the paddle cannot be eliminated
        if self.ball.y <= (self.window.height - PADDLE_OFFSET - PADDLE_HEIGHT - BALL_RADIUS * 2):
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                a = self.window.get_object_at(self.ball.x, self.ball.y)
                self.window.remove(a)
                self.score += 1  # when the bricks are eliminated, get one point.
            elif self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y) is not None:
                a = self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y)
                self.window.remove(a)
                self.score += 1
            elif self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2) is not None:
                a = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2)
                self.window.remove(a)
                self.score += 1
            elif self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2) is not None:
                a = self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y + BALL_RADIUS * 2)
                self.window.remove(a)
                self.score += 1

    def edge_check(self):
        """
        do not let the ball go out side of the window, except the bottom side
        """
        if self.ball.x <= 0:
            self.__dx = -self.__dx
        if self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def check_dead(self):
        """
        if the ball go to the bottom side, the function should be stopped
        """
        if self.ball.y >= (self.window.height - BALL_RADIUS * 2):
            return -1
        else:
            return 1

    def ball_restart(self):
        """
        after stopped, the velocity should be zero in x and y directions
        """
        self.__dx = 0
        self.__dy = 0

