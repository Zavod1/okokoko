def f(a, b):
    g = a * b
    if float(g).is_integer():
        return int(g)
    return g
print(f(1.6,3))