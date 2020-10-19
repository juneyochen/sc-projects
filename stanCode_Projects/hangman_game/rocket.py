"""
File: rocket.py
Name: June-Yo Chen
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 1


def main():
	"""
	My idea is that:
	1. create the functions for head(), belt(), upper() and lower()
	2. arrange the sequence of these functions
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):
		space = ''  # ' '
		slope1 = ''  # /
		slope2 = ''  # \
		for j in range(i + 1):
			slope1 += '/'
			slope2 += '\\'
		for k in range(SIZE - i):
			space += ' '
		print(space + slope1 + slope2 + space)


def belt():
	str1 = ''
	str_equal = ''
	for i in range(SIZE):
		str_plus = '+'
		str_equal += "="
	str1 = str_plus + str_equal + str_equal + str_plus
	print(str1)


def upper():
	str_wall = '|'
	for i in range(SIZE):
		str_dot = ''
		str_slope_part = ''
		for j in range(i + 1):
			str_slope_part += '/\\'
		for k in range(SIZE - (i + 1)):
			str_dot += '.'
		print(str_wall + str_dot + str_slope_part + str_dot + str_wall)


def lower():
	str_wall = '|'
	for i in range(SIZE):
		str_dot = ''
		str_slope_part = ''
		for j in range(SIZE - i):
			str_slope_part += '\\/'
		for k in range(i):
			str_dot += '.'
		print(str_wall + str_dot + str_slope_part + str_dot + str_wall)



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()