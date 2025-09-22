print("Задание №1. Переписать первое задание использую генераторы списков")
x = int(input("Введите число от 1 до 9: "))
if 1 <= x <= 3:
    s = input("Введите строку: ")
    n = int(input("Введите количество повторов строки: "))
    res = [s for i in range(n)]
    print(*res, sep="\n")

elif 4 <= x <= 6:
    m = int(input("Введите степень, в которую нужно возвести число: "))
    result = [x ** (i + 1) for i in range(m)]
    print("Результат:", result[-1])

elif 7 <= x <= 9:
    res = [x + 1 + i for i in range(10)]
    print(res)

else:
    print("Ошибка ввода")
