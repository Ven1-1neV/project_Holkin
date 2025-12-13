#дано целое число N больше нуля , если оно является степенью 
# числа 3 то выести TRUE в проивном случае FALSE
N = input('введите число больше нуля')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('неправильно ввели')
        N = input('введите число')
        
zov = N

while zov > 1:
    if zov % 3 != 0:
        break
    zov //= 3

if zov == 1:
    print("true")
else:
    print("false")
