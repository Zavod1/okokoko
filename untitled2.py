d=[]
a='rrogao'
b='o'
def search_substr(a,b):
    f= a.find(b)
    g= a.rfind(b)
    print(f,g)
search_substr(a,b)