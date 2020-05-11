# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
if len(argv) != 5:
    print("Неверное число параметров")
else:
    fname, fio, hours, stavka, prem = argv
    if not hours.isdigit() or not stavka.isdigit() or not prem.isdigit():
        print("Ошибка, неверное число")
    else:
        print(f"ЗП {fio} составила: {float(hours) * float(stavka) + float(prem)}")
