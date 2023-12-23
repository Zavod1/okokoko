b=0
m=0
a = input('введите пароль не больше 15 симвулов, имеет _ , имеет число в записи, без пробелов, последний знак * ' )

def g(a):
    b=0
    m=0
    for i in range (len(a)):
        if len(a) <= 15 :
            b=b+1
        else:
            m=m+1
        if a.count(" ")== 0:
            b=b+1
        else:
            m=m+1
        if '_' in a:
            b=b+1
        else:
            m=m+1
        if '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' in a:
            b=b+1
        else:
            m=m+1
        

    print(b, m)

g(a)


# здесь чтото пошло не так и это грустно 