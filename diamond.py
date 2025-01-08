r=6
c1=r-1
for i in range(r-1):
    for j in range(c1-i):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()
for i in range(r-1,-1,-1):
    for j in range(c1-i):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()