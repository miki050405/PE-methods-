print("Задание №1")
s = input("Введите строку (слова должны быть разделены пробелами): ")
words = s.split() 
word = max(words, key=len)
print("Самое длинное слово:", word)

print("Задание №2")
s = input("Введите строку (слова должны быть разделены точкой с запятой): ")
words = s.split(";") 
word = max(words, key=len)
print("Самое длинное слово:", word)

print("Задание №3")
s = input("Введите строку: ")
sign = input("Введите знак: ")
w=s.split(sign)
word = min(w, key=len)
print("Самое короткое слово:", word)

print("Задание №4")
s = input("Введите строку: ")
w = input("Введите слово: ")
if w in s:
    ss=s.find(w)
    print("Слово ", w," было найдено на позиции:",ss)
else:
    print("Слово", w, "не было найдено.")
    
print("Задание №5")
s = input("Введите строку: ")
w = s.split("")
print("Количество слов в предложении:", len(w))

