a=[1,2,3,4,5,6,7]
def b(a):
    if sum(a)>21:
        return(True)
    if sum(a)<=21:
        return(False)
print(b(a))