a = [1, 2, 'dog']
b = {}
def to_dict():
    for i in range(len(a)):
        b[a[i]] = a[i]
    print(b)
to_dict()
    
    
