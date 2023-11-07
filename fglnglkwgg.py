a = 'slnlnvf dfjjvf dfijgf zoeg bgdfklrg bk'
d = ''
def kal(a,d):
   
    for i in range(len(a)):
        b=''
        
        if i%2==0 and a[i] != ' ':
            if a[i].islower() == True:
                # print (a[i].swapcase())
                b=a[i].swapcase()
                d=d+b
                # print(d)
        else:
            # print (a[i])
            d=d+a[i]
            # print(d)
        if i == len(a)-1:
            print(d)


kal(a,d)
