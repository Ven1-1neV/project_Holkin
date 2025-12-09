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

if n > m:
    n, m = m, n

total = 0
current = n
while current <= m:
    total += current
    current += 1

print(f"Сумма всех чисел от {n} до {m} = {total}")
