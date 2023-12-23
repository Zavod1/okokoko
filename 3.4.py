a = 'a 56 m 7 g y r g 6 v r 44 y'
d=0
a=a.split()
summ = 0
for i in a:
    if i.isdigit():
        summ+=int(i)
print(summ)