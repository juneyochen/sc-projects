"""
File: sierpinski.py
Name: June-Yo Chen
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 10                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: 畫出遞迴形狀的三角形
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: 畫到第幾層
	:param length: 每一層三角形的邊常
	:param upper_left_x: 每一層三角形的左上頂點的x座標
	:param upper_left_y: 每一層三角形的左上頂點的y座標
	:return: 畫好的遞迴三角形
	"""
	if order == 0:  # Base Case
		return
	else:  # Not Base Case
		# 左上三角形最左邊頂點
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# 右上三角形最左邊頂點
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		# 下方三角形最左邊頂點
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length / 2 * 0.866)
		# 畫三角形
		line_1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		line_2 = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.866)
		line_3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.866)
		window.add(line_1)
		window.add(line_2)
		window.add(line_3)


if __name__ == '__main__':
	main()