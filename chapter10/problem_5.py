
    # write a class train which has method to book a ticket get status(no of seats)
    # and get fair information of train running:

from random import randint

class train :
    def __init__(self,trainno):
        self.trainno = trainno

    def book(self,fro,to):
        print(f"ticket is book in no {self.trainno}: from {fro} to {to}")

    def getstatus(self):
        print(f"train number {self.trainno} is running on time :")

    def getfair(self , fro , to ):
        print(f"ticket fair in train no:{self.trainno} from {fro} to {to} is {randint(222,555)}")


t = train(12434)
t.book("india", "delhi")
t.getstatus()
t.getfair("india","delhi")