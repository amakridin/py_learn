# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

lst = []
to_pass = True
while to_pass:
    var1 = input('введи строку чисел через пробел, чтобы выйти - q:')
    ff = var1.find('q')
    if ff >= 0:
        to_pass = False
        var1 = var1[0: ff]
    for value in var1.split():
        lst.append(int(value))
    print(f'Сумма числел:{sum(lst)}')



