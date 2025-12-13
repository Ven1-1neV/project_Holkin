#даны 2 целых числа A и B  а меньше б вывести в порядек возрастания 
# все целые числа, расоложенные между а и б, включая A и B 
# а также количество этих чисел
a, b = input("введите число А"), input('введите число B > A')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('неправильно ввели')
        a = input('введите число')
        
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('неправильно ввели')
        b = input('введите число')
k = 1 
z = b - a + 1
x = a 
print('числа по возрастанию;')
print(a)
while z != k:
    x += 1
    k += 1
    print(x)

N = b - a + 1
print("всего чисел:", N)
