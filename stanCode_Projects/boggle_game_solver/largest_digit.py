"""
File: largest_digit.py
Name: June-Yo Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: 給定的一串數字
	:return: 找出這串數字中最大的數字
	"""
	max_num = 0
	return find_largest_digit_helper(n, max_num)


"""
想法如下:
1. 先把給定的數字，不論是否為正數還是負數，都先變成正數。
2. 把數字對10取餘數，存到"最大的整數"中，在把數字除以10，即可把數字中每個整數取出來，互相比較大小。
"""


def find_largest_digit_helper(n, max_num):
	if n == 0:
		return max_num
	else:
		if n * -1 > 0:   # 判斷正數或負數
			n = n * -1

		if n % 10 == 0:  # 對10取餘數
			n /= 10
		if True:
			if max_num < (n % 10):  # 如果餘數比原本的max_num還大，則把max_num取代掉
				max_num = n % 10
				return int(find_largest_digit_helper(n, max_num)) # 因為存"數字"，不是資料結構
			else:
				n = (n - (n%10)) / 10  # 數字扣掉餘數後，除以10，往下繼續找數字
				return int(find_largest_digit_helper(n, max_num))


if __name__ == '__main__':
	main()
