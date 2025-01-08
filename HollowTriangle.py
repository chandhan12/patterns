r=6
for i in range(r):
    for j in range(r-i-1):
        print(" ",end=" ")
    for k in range(i*2+1):
        if(i==r-1 or k==0 or k==i*2 ):
            
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()