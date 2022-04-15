# Задача Codewars: 6 kyu
# given the first few terms of a sequence, can you figure out the formula that was used to generate these numbers, so we can find any term in the sequence?
# Task
# Create a function that takes a string as a parameter and does the following, in this order:
# Replaces every letter with the letter following it in the alphabet (see note below)
# Makes any vowels capital
# Makes any consonants lower case
# Note:
# the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.


def changer(s):
    c = ''
    for i in s:
        if i.isalpha():
            num = ord(i.lower())
            if num == 122:
                letter = chr(97)
            else:
                letter = chr(num + 1)
            if letter in 'aeiou':
                c += letter.upper()
            else:
                c += letter
        else:
            c += i
    return c


print(changer('Hello World'))
