#write a programe to find the greatest of four number enter by the user.

a1 = int(input("enter number 1 :"))
a2 = int(input("enter number 2 :"))
a3 = int(input("enter number 3 :"))
a4 = int(input("enter number 4 :"))


if(a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1 :",a1)


elif(a2>a1 and a2>a3 and a2>a4):
    print("greatet numberis a2 :",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("greatest number is a3 :",a3)


elif(a4>1 and a4>a2 and a4>a3):
    print("greatest number is a4",a4)