r=10
c=20
for i in range(r):
    for j in range(c):
        if(j<c-1-i and j>r-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end="")
    print()