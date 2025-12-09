#Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами.
#Значения n и m программа должна запрашивать.
while True:
    try:
        n = int(input("Введите первое число (n): "))
        break
    except ValueError:
        print("Ошибка: введите целое число.")

while True:
    try:
        m = int(input("Введите второе число (m): "))
        break
    except ValueError:
        print("Ошибка: введите целое число.")

total = 0
current = n
while current <= m:
    total += current
    current += 1

print(f"Сумма всех чисел от {n} до {m} = {total}")
