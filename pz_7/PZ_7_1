#дано целое число N >0  и строа S больше N.преобразовать стрроку длины N следующим образом: если дллина строки больше N то отбросить первые символы
#если длина строки меньше N то в ее начало добавить символы"." 


while True:
    try:
        n = int(input("ввеидте число символов в строке"))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("введите целое положительное число")

s = input("введите строку").strip()

if len(s) > n:
    res = s[-n:]
elif len(s) < n:
    tk = n - len(s)
    res = '.' * tk + s
else:
    res = s
print(res)
