#даныдва списка А и Б одинакового размера N сформировать новый список такого же размера, каждый элемент которого равен
#макксимальному элементу из обеих списков А и Б.
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
        a = [int(x) for x in data]
        break
    except ValueError:
        print("введитее ровно" , n ,"целых чисел")

while True:
    try:
        data = input("введитее числа через пробел").split()
        if len(data) != n:
            raise ValueError
        b = [int(x) for x in data]
        break
    except ValueError:
        print("введитее ровно" , n ,"целых чисел")

c = []
i = 0 
while i < n:
    c.append(max(a[i], b[i]))
    i += 1

i = 0
while i < len(c):
    if i < len(c):
        print('', end='')
    print(c[i], end='')
    i += 1
print()


