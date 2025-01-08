r=6

for i in range(r-1):
    for j in range(r-i-1):
        print(" ",end=" ")
    for k in range(i*2+1):
        if(i==r-1 or k==0 or k==i*2 ):
            
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(r-1,-1,-1):
    for j in range(r-i-1):
        print(" ",end=" ")
    for k in range(i*2+1):
        if(  k==0 or k==i*2 ):
            
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()