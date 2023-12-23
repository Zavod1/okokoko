a=input("утро или вечер? ")
b = float(input('ведите время в 12ти часовой системе '))
if a=='утро':
    print(b)
if a=='вечер':
    b=b+12
    print(b)

