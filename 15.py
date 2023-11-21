n=1
a = "2, 45, 35, 546, 231"
a="2, 45, 35, 546, 231".split(", ")
a=map(int,a)
a=list(a)
for i in a:
    n=n*i
print(n)