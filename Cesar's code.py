eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

print('Добро пожаловать в программу по созданию или дешифрованию Шфира Цезаря ')

language = input("Выберите язык шифровки: aнглийский - eng, русский - rus ")

while True:
    type_of_key = input("Выберите шифрование: шифрование - cipher (cip), дешифрование - decryption (dec) ")
    if type_of_key == 'cipher' or type_of_key == 'cip':
        key_d1 = int(input("Введите ключ шифрования "))
        key_d2 = key_d1 + 1
        break
    if type_of_key == 'dec' or type_of_key == 'decryption':
        quantity_key = input("У вас известен ключ шифрования или диапазон: введите 'key' или 'dia' ")
        if quantity_key == 'key':
            key_d1 = int(input("Введите ключ шифрования "))
            key_d2 = key_d1 + 1
            break
        elif quantity_key == 'dia':
            print("Введите диапазон шифрования ")
            key_d1 = int(input("Введите нижнюю границу ")) + 1
            key_d2 = int(input("Введите верхнюю границу "))
            break

phrase = input("Введите фразу ")

def chru(t_of_k, key_d1, key_d2, lan, ph):
    new_phrase = ''
    if lan == 'rus':
        length = 32
    if lan == 'eng':
        length = 26
    for k in range(key_d1, key_d2):
        if t_of_k == 'dec' or t_of_k == 'decryption':
            k = -k
        for i in range(len(ph)):
            if ph[i].isalpha():
                if ph[i] == ph[i].upper():
                    for j in range(length):
                        if length == 32:
                            if ph[i] == rus_upper[j]:
                                new_phrase += rus_upper[(j+k) % length]
                                break
                        if length == 26:
                            if ph[i] == eng_upper[j]:
                                new_phrase += eng_upper[(j+k) % length]
                                break
                elif ph[i] == ph[i].lower():
                    for j in range(length):
                        if length == 32:
                            if ph[i] == rus_lower[j]:
                                new_phrase += rus_lower[(j+k) % length]
                                break
                        if length == 26:
                            if ph[i] == eng_lower[j]:
                                new_phrase += eng_lower[(j+k) % length]
                                break
            else:
                new_phrase += ph[i]
        if key_d2 == key_d1 + 1:
            print(new_phrase)
        else:
            print('Вариант фразы №', k, '-', new_phrase)
            new_phrase = ''

chru(type_of_key, key_d1, key_d2, language, phrase)