    # write a programe using function to find greatest of three numbers :


a=7
b=8
c=1
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
# a=7
# b=8
# c=1
print(greatest(a,b,c))