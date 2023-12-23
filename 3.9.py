a = []
b = 0
r=[]
n= int(input('ввеите число билетов '))
while int(b) < n:
    a.append(b)
    b = int(b) + 1
a.append(n)
a.remove(0)
print (a)
for i in range (len(a)):
    q=[]
    k=a[i]
    while k >= 0:
      q.append(a[i] % 10)
      k = k // 10
    q = q[::-1]
    print(q)
    w=q[i]
    h=len(w)/2
    if w%2==1:
        h=h-0.5
        h=int(h)
        r.append(h)
        print (r[h])
        # здесь надо продолжить, что если сумма половин от середины числа равны то их надо добавить в отдельный масив
        # но программа уже на этом этапе не работает
    else:
        f=h-1
        f=int(f)
        h=int(h)
        r.append(h)
        r.append(f)
        print (r[f], r[h])
    # здесь надо продолжить, что если сумма половин от середины числа равны то их надо добавить в отдельный масив
       # но программа уже на этом этапе не работает
     
     
     
     
