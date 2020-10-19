"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

python_list = []  # 字典用的
current = []      # 使用者輸入的字母

used_position = []  # 用過的位置
number = 0           # 總共找到幾個單字


def main():
	"""
	TODO:
	"""
	global current
	count = 1
	# 先找到字典中的字
	read_dictionary()
	# 讓使用者輸入英文字母
	switch = 1  # 開關控制使用者輸入是否正確
	while True:
		if count == 5 or switch == -1:
			break
		else:
			enter = input(f'{count} row of letters: ')
			switch = check_enter(enter)
		count += 1

	if switch == 1:
		# 開始玩boggle
		play_boggle()
		# 最後印出結果
		print(f'There are {number} words in total.')


def check_enter(enter):  # 檢查輸入是否正確
	row = []
	enter = enter.lower()
	for i in range(len(enter)):
		if len(enter) > 8 or len(enter) < 7: # 有時候輸入者可能會多打一個空格，或者打完4個字直接按enter
			print('Illegal input')
			return -1
		else:
			if i % 2 == 0:                   # 把使用者輸入的英文字存在list中
				if enter[i].isalpha():
					row.append(enter[i])
				else:                        # 如果使用者不是輸入英文字，則print出Illegal input
					print('Illegal input')
					return -1
			if i % 2 == 1:                   # 基數格應該是輸入空白，如果不是空白，則print出Illegal input
				if enter[i] != ' ':
					print('Illegal input')
					return -1
	current.append(row)                      # 使用者輸入的字母組裝成一個大List
	return 1


def play_boggle():
	global used_position
	for k in range(4):
		for l in range(4):
			used_position = []
			word_test = ''
			word_test += current[k][l]
			used_position.append((k, l))
			found_word(word_test, [k, l], [k, l])


def found_word(word_test, start_position, now_position):
	global current, number, used_position
	start_position = now_position       # 新的位置
	if has_prefix(word_test):
		# Base case
		if word_test in python_list:
			if len(word_test) >= 4:
				print(f'Found: \"{word_test}\"')
				number += 1
				if has_prefix(word_test):
					python_list.remove(word_test)
					found_word(word_test, start_position, now_position)
		# Not base case
		else:
			for i in range(-1, 2, 1):            # 字串可以串每個位置的+-1
				for j in range(-1, 2, 1):        # 字串可以串每個位置的+-1
					x = i + start_position[0]    # 加上原本位置，確保不會串到空格或其他部分
					y = j + start_position[1]    # 加上原本位置，確保不會串到空格或其他部分
					if 0 <= x < 4:
						if 0 <= y < 4:
							if (i + start_position[0], j + start_position[1]) not in used_position:  # 確認用過的位置不能再用
								used_position.append((i + start_position[0], j + start_position[1]))
								# choose
								word_test += current[i + start_position[0]][j + start_position[1]]   # 串上新的字母
								now_position = [i + start_position[0], j + start_position[1]]        # 存下現在的位置
								# explore
								found_word(word_test, start_position, now_position)  # 往下去找其他字
								# unchose
								used_position.pop()      # 回到上一層，要把探索過的位置紀錄刪掉，才能串其他字
								word_test = word_test[:len(word_test)-1]   # 要把字串刪掉最後一個字
							else:
								pass


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global python_list
	with open(FILE, 'r') as line:
		for words in line:
			if len(words.strip()) >= 4:  # 題目要求只找長度大於4的字，所以先把長度4以下的字過濾掉
				python_list.append(words.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in python_list:      # 找開頭有沒有在字典中
		if i.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
