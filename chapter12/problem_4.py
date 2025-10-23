   
   # write  a programme to display a/b where a and b are integer .if b=0 display infinite handling"zerodivisionerror:


try:
   a = int(input("enter number :"))
   b = int(input("enter your number :"))
   print(a/b)

except ZeroDivisionError as e:
   print("infinite")
