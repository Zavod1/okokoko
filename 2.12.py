a=input('введите слово ')
def f (a):
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            return (True)
print(f(a))