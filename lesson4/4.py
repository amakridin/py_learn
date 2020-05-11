import random
lst = [random.randint(1, 10) for i in range(10)]
res = []
for elm in lst:
    if lst.count(elm) == 1:
        res.append(elm)
print(lst)
print(res)