# write a program to print a following stars pattern:
#    * * *
#    *   *
#    * * *

n = int(input("enter the number of rows:"))
for i in range(1, n+1):
    if(i==1 or n==1):
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "* (n-2),end="")
        print("*",end="")    

    print("")