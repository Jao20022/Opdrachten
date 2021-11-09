import random


def monopolyworp():
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    return a, b


def again(count):
    a, b = monopolyworp()
    if count >= 3:
        print("Go to Jail")
        return lis
    lis.append([a, b])
    if a == b:
        count += 1
        again(count)
    return lis


for i in range(2000):
    lis = []
    c = 0
    print(again(c))
