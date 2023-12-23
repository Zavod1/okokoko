a = ['пиво', 'селёдка', 'хлебушек']
b = ['пиво']
def f(a,b):
    for i in range(len(b)):
        if a.count(b[i])>0:
            a.remove(b[i])
f(a,b)
print(a)
