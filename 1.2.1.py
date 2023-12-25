def a(b):
    if isinstance(b, (int, float)):
        return float(b)
    return "Невозможно преобразовать"
print(a(764))
