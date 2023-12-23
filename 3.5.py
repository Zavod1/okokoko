a = '+a+d+f+v+g+j+h+t+'
d='True'
for i in range (len(a)):
    if i%2==0 and a[i]!='+':
        d='Folse'
        print(a[i],i)
print(d)