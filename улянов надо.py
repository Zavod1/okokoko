a = []
def appending(a):
    while True:
        s = input('Что вы хотите добавить, число или слово? ')
        if   s == 'число':
             s = int (input('введите число '))
             a.append(s)
             print(a)
             i = input('ещё хочешь? ')
             if i == 'нет':
                 break
        elif s== 'слово':
             s = input('введите слово ')
             a.append(s)
             i = input('ещё хочешь? ')
             print(a)
             if i == 'нет':
                 break
        else:
            print()
            print('иди в пень')


def fen(a):
    d = int (input('введите ном '))
    print(a[d])
    
    
z=0
while z!=1:
    print("1.Дополнить массив")
    print("2.Поиск элемента")
    choose = int(input("введите цифру из тех, что выше "))
    if choose == 1:
        appending(a)
    if choose == 2:
        fen(a)
        z=1
    