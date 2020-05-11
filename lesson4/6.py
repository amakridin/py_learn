# 1
from itertools import count

for el in count(3):
    if el > 10: break
    else: print(el)

# 2
from itertools import cycle

с = 3
for el in cycle("hello"):
    if с > 10:
        break
    print(el)
    с += 1
