r=4
for i in range(r):
    for j in range(r-i-1):
        print(" ",end=" ")
    for k in range(i,-1,-1):
        print(k+1,end=" ")
    for m in range(1,i+1):
        print(m+1,end=" ")
    print()