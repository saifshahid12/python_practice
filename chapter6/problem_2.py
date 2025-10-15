#write a programme to find out whether a student has passed or fail if it require a total of 40%
#and atleast 33%in each subject to pass.assume three subjects and take marks as input from user.


marks1=int(input("enter marks 1:"))
marks2=int(input("enter marks 2:"))
marks3=int(input("enter marks 3:"))

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 ):
    print("you are passed", total_percentage)

else :
    print("you are faied",total_percentage)


print("===============================================================")



#write a programme to find out whether a student has passed or fail if it require a total of 40%
#and atleast 33%in each subject to pass.assume three subjects and take marks as input from user.


marks1=int(input("enter marks 1:"))
marks2=int(input("enter marks 2:"))
marks3=int(input("enter marks 3:"))

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print("you are passed", total_percentage)

else :
    print("you are faied",total_percentage)




