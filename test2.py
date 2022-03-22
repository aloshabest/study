# Задача Codewars: 5 kyu
# given the first few terms of a sequence, can you figure out the formula that was used to generate these numbers, so we can find any term in the sequence?
#
# Task
# write a function that accepts an array of number(the first few terms of a sequence)
# your function should return a mapping function that accepts an integer(n) and then return the nth term of the sequence, where zero is the first term.
# in practice a sequance can be completed in many ways, assume that the equation used is a Polynomial, and find the simplest(smallest degree) equation possible, that leaves you with a single unique solution.


seq = [6, 17, 88, 321, 866]
k = len(seq)
if len(seq) == 5:
    for p in range(-10, 21):
        for q in range(-10, 21):
            for z in range(-10, 21):
                for v in range(-10, 21):
                    if (p + q + z + v == seq[1]-seq[0]) and (p * 16 + q * 8 + z * 4 + v * 2 == seq[2]-seq[0]) and\
                        (p * 81 + q * 27 + z * 9 + v * 3 == seq[3]-seq[0]) and (p * 256 + q * 64 + z * 16 + v * 4 == seq[4]-seq[0]):
                            quest = [(p * i ** (k - 1)) + (q * i ** (k - 2)) + (z * i ** (k - 3)) + (v * i ** (k - 4)) + seq[0] for i in range(10)]
print(quest)


seq = [1, 1, 1, 7]
k = len(seq)
if len(seq) == 4:
    for q in range(-10, 21):
        for z in range(-10, 21):
            for v in range(-10, 21):
                if (q + z + v == seq[1]-seq[0]) and (q * 8 + z * 4 + v * 2 == seq[2]-seq[0]) and (q * 27 + z * 9 + v * 3 == seq[3]-seq[0]):
                    quest = [(q * i ** (k - 1)) + (z * i ** (k - 2)) + (v * i ** (k - 3)) + seq[0] for i in range(10)]
print(quest)



seq = [2, 4, 6]
if len(seq) <= 3:
    quest = [((seq[1] - seq[0]) * i) + seq[0] for i in range(10)]
print(quest)

seq = [5]
if len(seq) == 1:
    quest = [seq[0] for i in range(10)]
print(quest)

seq = []
if len(seq) == 0:
    quest = [0 for i in range(10)]
print(quest)