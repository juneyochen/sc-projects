"""
File: caesar.py
Name: June-Yo Chen
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    My idea is that:
    1. let user enter a number
    2. let user enter the ciphered string
    3. start the function for deciphering
    4. return the actual word
    """
    number = input('Secret number: ')
    string = input('What\'s the ciphered string? ')
    string = string.upper()
    ans = decipher(string, number)
    print('The deciphered string is: '+ans)


def decipher(string, number):
    """
    :param string: the string that will be deciphered
    :param number: the number for transfer the position of ALPHABET
    :return: deciphered string
    My idea is that:
    1. find the position of the word in the ALPHABET
    2. transfer a certain number of the position
    3. if the number of the position is larger than 26, the number should minus 26
    4. return the actual word
    """
    string_out = ''
    for i in string:
        j = ALPHABET.find(i)
        if j == -1:
            l = i
        else:
            k = j + int(number)
            if k > 25:
                k = k - 26
                l = ALPHABET[k]
            else:
                l = ALPHABET[k]
        string_out += l
    return string_out





#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
