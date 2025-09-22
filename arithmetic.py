def check1():
    s = input("Введите строку: ")
    n = int(input("Введите количество повторов строки: "))
    for i in range(n):
        print(s)


def check2(x, m):
    return x**m


def check3(x):
    for i in range(10):
        x += 1
        print(x)
