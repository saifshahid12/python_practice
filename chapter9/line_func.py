f=open("file.txt")


# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)



# using while loop :

line = f.readline()
while(line !=""):
    print(line)
    line=f.readline()

f.close