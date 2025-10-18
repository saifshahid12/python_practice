    # write a programme to calculate the factorial number using for loop:

n=int(input("enter factorial number:"))


num=1
for i in range(1,n+1):
    num=num*i

print(f"the factorial of {n} is {num}")