    # write a class calculator capable of finding square , qube and square root of a number:

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self) :
        print(f"the square is :{self.n*self.n}")

    def cube(self):
        print(f"the qube is :{self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the square root is :{self.n**1/2}")

a = calculator(4)
a.square()
a.cube()
a.squareroot()
