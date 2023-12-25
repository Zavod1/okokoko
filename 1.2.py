def a(b):
    l1 = b[0]
    l2 = b[len(b) - 1]
    b[len(b) -1 ] = l1
    b[0] = l2
    print(b)
    return b
a([1,2,3])   