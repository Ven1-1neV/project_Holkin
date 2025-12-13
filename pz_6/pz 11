#дан целочисленный списокразмера n.Проверить, чередуются ли в нем четныеи нечетне числа.
#если чередуются то вывести 0, если нет, то вывестипорядковый номерперввого жлемента нарушевшего закономерность
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
        lst = [int(x) for x in data]
        break
    except ValueError:
        print("введитее ровно" , n ,"целых чисел")

i = 1
result = False
while i < n:
    if (lst[i] % 2) == (lst[i - 1] %2):
       print(i)
       result = True
       break
    i += 1

if not result:
    print(0)
