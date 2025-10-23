

  # store the multiplication table generated in problem 3 in a file name table.txt:

n = int(input("enter your number :"))

table = [n*i for i in range(1,11)]
with open("tables.txt","a") as f:
  #  f.write(str(table)+ "\n")
    f.write(str(table)+"\n")
