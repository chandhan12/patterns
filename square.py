r=5
c=5
for i in range(r):
    for j in range(c):
        if(j==0 or j==4 or i==4 or  i==0 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()


    

#     r=5
# c=5
# for i in range(r):
#     for j in range(c):
#         if(i==0 or j==0 or j==c-1 or i==r-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

    