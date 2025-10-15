# write a programe to calculate grade of a student from his marks from a folllowing scheme:

marks=int(input("enter your marks :"))

if(marks<=100 and marks>=90):
    grade="Ex"

elif(marks<=90 and marks>=80):
    grade="A"

elif(marks<=80 and marks>=70):
    grade="B"

elif(marks<=70 and marks>=60):
    grade="c"

elif(marks<=60 and marks>=50):
    grade="D"

elif(marks<50):
    grade="F"

print("Your grade is :",grade)


print("=======================================================")


# PRACTICE



marks=int(input("enter your marks :"))


if(marks<=100 and marks>=90):
    grade="ex"

elif(marks<=90 and marks>=80):
    grade="A"

elif(marks<=80 and marks>=70):
    grade="b"

elif(marks<=70 and marks>=60):
    grade="c"

elif(marks<=60 and marks>=60):
    grade="d"
elif(marks<50):
    grade="F"

print("your grade is :",grade)