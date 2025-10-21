  # create a class (2d vector) and use it to create another class 
  # representing (3d vector):


class towDvector:
  def __init__(self,i ,j):
    self.i =i
    self.j =j

  def show (self):
    print(f"the vector is :{self.i}i +{self.j}j")


class threeDvector(towDvector):
  def __init__(self, i, j, k):
    super().__init__(i ,j)
    self.k = k

  def show(self):
      print(F"the vector is :{self.i}i +{self.j} +{self.k}k")

a=towDvector(1, 2)
a.show()
b=threeDvector(5,2,3,)
b.show()

