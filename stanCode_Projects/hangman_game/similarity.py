"""
File: similarity.py
Name: June-Yo Chen
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    這題想法主要都是助教教我的，謝謝助教~
    My idea is that:
    1. let user enter a long DNA sequence and a short DNA sequence
    2. check the short DNA sequence in the long DNA sequence
    3. return the answer
    """
    dna_long = input('Please give me a DNA sequence to search: ')
    dna_short = input('What DNA sequence would you like to match? ')
    dna_long = dna_long.upper()
    dna_short = dna_short.upper()
    ans = check_dna(dna_long, dna_short)
    print('The best match is '+ str(ans))


def check_dna(dna_long, dna_short):
    """
    :param dna_long: the DNA sequence that should be checked
    :param dna_short: the targeted DNA sequence
    :return: the most similar part in the long DNA sequence
    My idea is that:
    1. use a max_number to load the most similar sequence
    2. compare the length of the long DNA and short DNA
    3. if there is a base in the long DNA as same as the short DNA, the number should add 1
    4. if the number is the maximum number, remember the position of the number as M
    5. print the position from M to the length of the short DNA
    """
    max_number = 0
    for i in range(len(dna_long)-len(dna_short)+1):
        number = 0
        for j in range(len(dna_short)):
            if dna_short[j] == dna_long[j+i]:
                number += 1
        if number > max_number:
            max_number = number
            M = i
    return dna_long[M:M + len(dna_short)]



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
