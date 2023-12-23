a=[1, 3, 6, 10, 46]
for i in range (len(a)):
    if a[i]!=a[-1] and a[i] < a[i+1]:
        print ("возрост")
    elif a[i]==a[-1] and a[i] > a[i-1]:
        print ("возрост")    
    else:
        print ("мимо")
        break