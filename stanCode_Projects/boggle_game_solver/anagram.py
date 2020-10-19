"""
File: anagram.py
Name: June-Yo Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

python_list = []              # 存字典裏面的字
all_anagrams = []             # 存有找到的字


def main():
    global python_list, all_anagrams
    # 開場白
    print(f'Welcome to stanCode \"Anagram Generator\" or ( {EXIT} to quit)')
    # 讀取字典
    read_dictionary()
    while True:
        s = input('Find anagrams for: ')  # 使用者輸入的單字
        if s == EXIT:                     # 終止指令
            break
        find_anagrams(s)
        print(f'{len(all_anagrams)} anagrams: {all_anagrams}')  # 最後統計幾個字，跟列出所有找到的字
        all_anagrams = []                 # 清空存單字的List


def read_dictionary():
    # 讀取字典
    with open(FILE, 'r') as line:
        for word in line:
            python_list.append(word.strip())


def find_anagrams(s):
    """
    :param s: 給定的單字
    :return: 一旦找到字，要印出來，並把字存起來
    """
    find_anagrams_helper(s, '')


def find_anagrams_helper(s, chosen):
    if len(chosen) == len(s):  # 當字串長度一樣時，可以檢查是否有這個字
        word = ''
        for j in chosen:       # index轉成英文字
            word += s[int(j)]
        if word in python_list and word not in all_anagrams:  # 看單字有沒有在字典中
            all_anagrams.append(word)
            print('Searching...')
            print(f'Found: {word}')

        else:
            pass
    else:
        if has_prefix(chosen, s):    # 檢查單字的開頭，是否存在字典中
            for i in range(len(s)):  # 用index去選字，避免同一個字中有重複字母時會出問題
                element = str(i)     # 串index
                if element not in chosen:
                    # choose
                    chosen += element
                    # explore
                    find_anagrams_helper(s, chosen)
                    # unchose
                    chosen = chosen[:len(chosen)-1]


def has_prefix(sub_s, s):
    """
    :param sub_s: 看字典內有沒有sub_s開頭的字
    :return: True or False, 可以用在加速字典查閱
    """
    word = ''
    for j in sub_s:  # 因為上述是用index去串，要轉成英文字母
        word += s[int(j)]

    for i in python_list:
        if i.startswith(word) is True:
            return True
    return False


if __name__ == '__main__':
    main()
