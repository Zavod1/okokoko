a=[[12, 34, 6, 5], [3,7,9], [67,3]]
d=0
for i in range (len(a)):
    print(a[i])
    s=1
    h = a[i]
    for k in range (len(h)):
        s=s*h[k]
        print(s)
    d+=s
print (d)
