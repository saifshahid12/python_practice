
    # create a class with class attribute a:create an object from it and set "a":
    # directly using object .a =0 does this change the class attribute:

class demo:
     a= 4

o = demo()
print(o.a)
                    # not chang class because instance value not give:
o.a = 0
print(o.a)

