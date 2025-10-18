    # write a recursive function to calculate the  sum of first natural number :


def sum(n):
    if n==1:
        return 1

    else:
        return sum(n-1)+n

n=int(input("enter number :"))

print(sum(n))