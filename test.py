import time
import random


def fuctorize():
    """Факторизация числа"""
    n = random.randint(90000000000, 1000000000000)
    print(f"Число: {n}")

    m = n
    i = 2
    lst_out = []

    while True:
        if i >= m**0.5:
            if n > 1:
                lst_out.append(n)
            break

        if n % i == 0:
            lst_out.append(i)
            n /= i
        else:
            i += 1

    return print("Делители:", *lst_out)



start_time = time.time()
fuctorize()
print('----------')
end_time = time.time()
print("Время выполнения кода: {0:.10f} секунд".format(end_time - start_time))
print('----------')


