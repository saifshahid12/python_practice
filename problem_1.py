
    # create a class "programmer" for storing information of few programmers workin in 
    # microsoft :

class programmer:
    company ="microsoft"
    def __init__( self,name,sallery,pin):

        self.name = name
        self.sallery = sallery
        self.pin = pin

p = programmer("saif",12000,234)
print(p.name, p.sallery, p.pin, p.company)

r = programmer("rohan",10000,800)
print(r.name, r.sallery, r.pin, r.company)