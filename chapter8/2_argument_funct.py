

def greet(name):
    print("good day ,"+name)

greet("saif")
greet("harry")

print("=============================================================")


def greet(name,ending):
    print("good day,"+name)
    print(ending)

greet("saif", "thankew")
greet("harry","thankew")


print("1==========================================================")

# using return ""

def greet(name,ending):
    print("good day,"+name)
    print(ending)

    return "ok"

a=greet("saif", "thankew")
print(a)
