# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

nn = 1
for w in input("Давай строку сюда: ").split(" "):
    print(nn, w[0:10])
    nn += 1

###or

lst = input("Давай еще строку сюда: ").split(" ")
for i in range(len(lst)):
    print(i + 1, lst[i])
