import math

while True:
    try:
        n = int(input("введите количество чисел в списке"))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("введите целое положительное число!")

while True:
    try:
        data = input("введитее числа через пробел").split()
        if len(data) != n:
            raise ValueError
        ax = [int(x) for x in data]
        break
    except ValueError:
        print("введитее ровно" , n ,"целых чисел")

while True:
    try:
        data = input("введитее числа через пробел").split()
        if len(data) != n:
            raise ValueError
        ay = [int(x) for x in data]
        break
    except ValueError:
        print("введитее ровно" , n ,"целых чисел")

while True:
    try:
        nt = int(input("введите количество чисел в списке"))
        if nt <= 0:
            raise ValueError
        break
    except ValueError:
        print("введите целое положительное число!")

while True:
    try:
        data = input("введитее числа через пробел").split()
        if len(data) != nt:
            raise ValueError
        bx = [int(x) for x in data]
        break
    except ValueError:
        print("введитее ровно" , nt ,"целых чисел")

while True:
    try:
        data = input("введитее числа через пробел").split()
        if len(data) != nt:
            raise ValueError
        by = [int(x) for x in data]
        break
    except ValueError:
        print("введитее ровно" , nt ,"целых чисел")

mind = float('inf')
resax = resay = resbx = resby = None

i = 0
while i < n:
    t = 0
    while t < nt:
        rx = bx[t] - ax[i]
        ry = by[t] - ay[i]
        dist = math.sqrt(rx * rx + ry *ry)
