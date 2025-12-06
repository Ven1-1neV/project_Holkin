#даны координаты пол шахматной доски x,y (целые числа в диапазоне от 1 до 8) 
# учитывая что левое нижнее поле доски (1,1) 
# является черным поверить истинность высказывания:"данное поле является белым"
x, y = int(input('введите значение х(число)')), int(input('введите значение y(число)'))
if not ( 1<= x <= 8 and 1<= y <= 8):
    print('дфнной клетки не существует')
else:
    while type(x) != int:
        try:
            x = int(x)
        except ValueError:
            print('неправильно ввели')
            x = int(input('введите значение х'))

    while type(y) != int:
        try:
            y = int(y)
        except ValueError:
            print('неправильно ввели')
            y = int(input('введите значение х'))
        
    if y == 1 or y == 3 or y == 5 or y == 7:
        if x == 2 or x == 4 or x == 6 or x == 8:
            print("поле белое, ура победа")
    elif y == 2 or y == 4 or y == 6 or y == 8:
        if x == 1 or x == 3 or x == 5 or x == 7:
            print("поле белое, ура победа")
    elif y == 1 or y == 3 or y == 5 or y == 7:
        if x == 1 or x == 3 or x == 5 or x == 7:
            print("поле черное, не белое")
    elif  y == 2 or y == 4 or y == 6 or y == 8:
        if x == 2 or x == 4 or x == 6 or x == 8:
            print("поле черное, не белое")
