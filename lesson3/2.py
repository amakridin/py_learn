# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_params(firstname, lastname, bornyear, city, email, phone):
    return f"Имя: {firstname}\nФамилия: {lastname}\nГод рождения: {bornyear}\nГород проживания: {city}\nemail: {email}\nТелефон{phone}"

print(user_params(firstname=input("Имя: "),
                  lastname=input("Фамилия: "),
                  bornyear=input("Год рождения: "),
                  city=input("Город проживания: "),
                  email=input("email: "),
                  phone=input("телефон: ")))