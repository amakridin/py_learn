
nn = 1
nomen = []
answ = True
while answ:
    dic = {}
    dic["название"] = input("Введи название товара: ")
    dic["цена"] = float(input("Введи цену товара: "))
    dic["количество"] = float(input("Введи количество товара: "))
    dic["ед"] = input("Введи ед.изм товара: ")
    nomen.append((nn, dic))
    nn += 1
    answ = True if input("Продолжим (да/нет)?").lower() == "да" else False
print(nomen)
nomen_name, nomen_price, nomen_cnt, nomen_ed = [], [], [], []
for row in nomen:
    nomen_name.append(row[1]["название"])
    nomen_price.append(row[1]["цена"])
    nomen_cnt.append(row[1]["количество"])
    nomen_ed.append(row[1]["ед"])
rez = {"название": nomen_name, "цена": nomen_price, "количество": nomen_cnt, "ед": nomen_ed}
print(rez)
