         
    # create a class employee and add sallery and increments properties to it :

class employee:
    sallery=234
    increment=20
e= employee()
print(f"the sallery is :{e.sallery}")
print(f"the increment is :{e.increment}")

print("--------------------------------------------------")

    # write a method salleryafterincrement method with  @property decorator with a setter which changes the increment value :
class employee:
    sallery=234
    increment=20

    @property
    def salleryafterincrement(self):
        return self.sallery + (self.sallery * self.increment)/100
e= employee()
print(f"the sallery after increment is :{e.salleryafterincrement}")