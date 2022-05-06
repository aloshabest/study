# Задача Codewars: 6 kyu
# Create a function that takes a string and separates it into a sequence of letters.
# The array will be formatted as so:
# [['J','L','L','M']
# ,['u','i','i','a']
# ,['s','v','f','n']
# ,['t','e','e','']]
# The function should separate each word into individual letters, with the first word in the sentence having its letters in the 0th index of each 2nd dimension array, and so on.
# Shorter words will have an empty string in the place once the word has already been mapped out. (See the last element in the last part of the array.)



# первое решение
def sep_str(st):
    if len(st) == 0:
        return []
    words = st.split()
    lst = []
    x = 0
    while True:
        ls = [i[x] if x < len(i) else '' for i in words]
        x += 1
        if len(set(ls)) == 1:
            break
        lst.append(ls)

    return lst


print(sep_str("Just Live Life Man"))
print(sep_str("The Mitochondria is the powerhouse of the cell"))
print(sep_str(""))



# второе решение
def sep_str(st):
    if len(st) == 0:
        return []
    word = st.split()
    word_list = [[] for _ in range(len(sorted(word, key=len)[-1]))]
    for i in range(len(word)):
        for j in range(len(word_list)):
            if j < len(word[i]):
                word_list[j].append(word[i][j])
            else:
                word_list[j].append('')

    return word_list



print(sep_str("The Mitochondria is the powerhouse of the cell"))
print(sep_str(""))