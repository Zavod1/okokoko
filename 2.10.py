a= [12]
b= [44]
c=[]
d=[]
for i in range(len(max(a,b))):
    c.append(a[i])
    c.append(b[i])
    d.append(c)
    c=[]
print(d)     
    
