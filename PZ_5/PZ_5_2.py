def digitCountSum(K):
    temp = K
    C = 0  
    S = 0  
    while temp > 0:
        S += temp % 10
        C += 1
        temp //= 10
    return C, S

print("Введите 5 целых положительных чисел:")
i = 0
while i < 5:
    try:
        K = int(input(f"Число {i + 1}: "))
        if K <= 0:
            print("Число должно быть положительным.")
            continue
    except ValueError:
        print("Ошибка: введите целое положительное число.")
        continue

    C, S = digitCountSum(K)
    print(f"Число {K}: количество цифр = {C}, сумма цифр = {S}")
    i += 1
