"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120     # 120 frames per second.
NUM_LIVES = 3               # the life that user can play the game



def main():
    """
    set up the score label and how many life dose the user have.
    """
    graphics = BreakoutGraphics()
    life = NUM_LIVES
    score_label = GLabel('Score: ' + str(graphics.score) + ' and live: ' + str(life))
    score_label.font = '-20'
    graphics.window.add(score_label, 0, graphics.window.height)
    switch = 1  # a switch that prevents user to click while the ball is moving

    # Add animation loop here!
    while switch == 1 and life >= 0:
        # renew the score and life every time
        score_label.text = 'Score: ' + str(graphics.score) + ' and life: ' + str(life)
        # let the ball moves
        graphics.ball.move(graphics.get_vx(), graphics.get_vy())
        # check whether ball touches objects or not
        graphics.object_check()
        # when touching the bricks, the bricks should be eliminated
        graphics.eliminate_brick()
        # when touching the edge of the window, the ball should reflect
        graphics.edge_check()
        # when the ball touches to the bottom of the window, switch = -1 and the life should minus one
        switch = graphics.check_dead()
        if switch == -1:
            life -= 1
            switch = 1
            graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
            graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
            graphics.ball_restart()
        # if all the bricks are eliminated, the game should be ended
        if graphics.score == graphics.max_score:
            break
        pause(FRAME_RATE)  # prevent the ball move too fast


if __name__ == '__main__':
    main()
