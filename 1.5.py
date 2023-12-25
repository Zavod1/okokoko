def a(v):
    v.sort(key=lambda x: abs(x), reverse=True)
    return v
print(a([65, 23, 350]))