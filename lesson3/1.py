# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "деление на 0"

print("В результате мы получаем - ", my_func(int(input("Введи числитель: ")), int(input("и знаменатель: "))))