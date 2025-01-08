r=5
for i in range(r):
    for j in range(r-1-i):
        print(" ",end=" ")
    for k in range(i,-1,-1):
        print(k+1,end=" ")
    print()