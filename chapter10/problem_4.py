
    # add a staticmethid :


class calculator:
    def __init__(self,n):
        self.n=n

    def square(self) :
        print(f"the square is :{self.n*self.n}")

    def cube(self):
        print(f"the qube is :{self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the square root is :{self.n**1/2}")

    @staticmethod       # also called decorator method :
    def hello():
        print("good morning!")


a = calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()
