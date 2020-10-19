"""
File: hangman.py
Name: June-Yo Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    這題也很謝謝助教幫忙，不然真的寫不出來
    這題有點複雜，我用中文寫註解
    想法如下:
    1. 先把 random 那個字存到 word 裡面
    2. 把 word 的長度，以'_' 存到 string1裡面，並把string1 印出來
    3. 把猜測次數存在 left_number 裡面
    """
    word = random_word()
    string1 = ''
    for i in range(len(word)):
        string1 += '_'
    left_number = N_TURNS
    #print(word) # 一開始寫程式時，檢查用的
    print('The word looks like: ' + string1)
    print('You have ' + str(left_number) + ' guesses left.')
    while left_number > 0:
        """
        1. 每次執行while loop時，先印出使用者還剩幾次猜測次數
        2. 排除不適當輸入值，像是 2 aa eee 等
        """
        guess = input('Your guess: ').upper()
        if not guess.isalpha() or len(guess) > 1:
            print('illegal format')
            """
            1. 當使用者輸入的英文字母可以在指定word中找到時，開始執行拼字串
            2. 由於一開始string1全部都是'_'，故如果有找到的英文字，再插入字串中即可
            3. 由於我這邊是以word字串當目標字串，故如果同一個英文字在word中重複出現，就必須將word中的字母改成小寫，以後續檢查
            4. 檢查完後，word全部變回大寫，以方便下一次檢查
            5. 如果string1 全部都是字母組成，則代表猜對了，印出特定句子，然後break
            6. 如果猜錯字，則扣一次猜測次數，扣到0，就輸了
            """
        elif word.find(guess) != -1:
            for j in word:
                if j == guess:
                    string1 = string1[:word.find(guess)] + guess + string1[word.find(guess)+1:]
                    word = word[:word.find(guess)] + guess.lower() + word[word.find(guess)+1:]
            word = word.upper()
            print('You are correct!!')
            if string1.isalpha():
                print('You win!!')
                print('The word was: ' + word.upper())
                break
            print('The word looks like: ' + string1)
            print('You have ' + str(left_number) + ' guesses left.')
            """
            如果使用者輸入的字母，在word中找不到，即扣一次left_number
            """
        elif word.upper().find(guess) == -1:
            left_number -= 1
            print('There is no ' + guess + '\'s in the word.')
            if left_number == 0:
                print('You are completely hung : (')
                print('The word was: ' + word)
                break
            print('You have ' + str(left_number) + ' guesses left.')


# def main():
#     """
#     這個是助教跟我分享的另一種寫法
#     想法是用字串指定串上指定值，比較精簡直觀
#     """
#     word = random_word()
#     current = ''
#     for i in range(len(word)):
#         current += '_'
#     lives = N_TURNS
#     print("The word looks like: " + current)
#     print("You have " + str(lives) + " guesses left.")
#
#     while True:
#         guess = input('Your guess: ')
#         guess = guess.upper()
#
#         if not guess.isalpha() or len(guess) > 1:
#             print('illegal format.')
#
#         elif guess in word:
#             temp = ''
#             for i in range(len(word)):
#                 if guess == word[i]:
#                     temp += guess
#                 else:
#                     temp += current[i]
#             current = temp
#             print('You are correct!!')
#             if '_' not in current:
#                 print('You win!')
#                 print('The word was: ' + word)
#                 break
#             print("The word looks like: " + current)
#             print("You have " + str(lives) + " guesses left.")
#
#         else:
#             lives -= 1
#             print('There is no ' + guess + '\'s in the word.')
#             if lives == 0:
#                 print('You are completely hung : (')
#                 print('The word was: '+ word)
#                 break
#             print("You have " + str(lives) + " guesses left.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
