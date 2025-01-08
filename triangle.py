r=6
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print(" ",end=" ")
    temp=i*2+1
    for k in range(temp):
        print("*",end=" ")
    print()