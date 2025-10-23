
   # write list comprehension to print a list which contain a multiplication table 
#    of a user wnter number :

n = int(input("enter your number :"))

table = [n*i for i in range(1,11)]
print(table)