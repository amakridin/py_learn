# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def max2(a, b, c):
    return a + b + c - min(a, b, c)

print(max2(1, 2, 3))