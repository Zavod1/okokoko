a = "2, 45, 35, 546, 231"
a="2, 45, 35, 546, 231".split(", ")
a=map(int,a)
a=list(a)
g=0
for i in range (len(a)):
    print (a)
    n=a[i]
    g+=n
print(g)
