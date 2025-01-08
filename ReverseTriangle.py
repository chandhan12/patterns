r=10
for i in range(r):
    for j in range(i):
        print(" ",end=" ")
   
    for k in range((2*r)-1-(2*i)):
        print("*",end=" ")
    print()