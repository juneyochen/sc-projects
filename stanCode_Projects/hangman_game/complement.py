"""
File: complement.py
Name: June-Yo Chen
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Basically, this question was taught in the class, so I just use the functions according to it
    My idea is that:
    1. let user enter a DNA
    2. transfer the DNA sequence
    3. return the answer
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    print('The complement of ' + dna + ' is ' + build_complement(dna))


def build_complement(dna):
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
