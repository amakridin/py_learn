# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

v = float(input("Введи значение выручки фирмы: "))
i = float(input("Введи значение издержек фирмы: "))
if v>i:
    print("Выручка больше издержек. Да мы в прибыли!!!")
    rent = (int(100*100*(v-i)/v))/100
    print(f"Рентабельность составила {str(rent)}%")
    s = int(input("А сколько сотрудников в фиирме?"))
    p1 = (int(100*(v-i)/s))/100
    print(f"В таком случае, прибыль фирмы в расчете на одного сотрудника составила {str(p1)} каких-то денежных единиц")
else:
    print("Издержки, к сожалению, больше прибыли. Дело дрянь (((")
