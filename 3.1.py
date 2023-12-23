
a=input()
b=input()
if a==b:
    print('ничья')
else:
    if a=='бумага':
        if b=='камень':
            print('победил 1')
        else:
            print('победил 2')
    if a=='камень':
        if b=='бумага':
            print('победил 2')
        else:
            print('победил 1')
    if a=='ножницы':
        if b=='бумага':
            print('победил 1')
        else:
            print('победил 2')
