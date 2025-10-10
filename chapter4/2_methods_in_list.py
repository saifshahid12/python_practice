#  methods use in list :
# 1 sort()
# 2 reverse()
# 3 append()
# 4 insert()
# 5 pop()
# 6 remov()

# use append method :

friends =["apple","orange","5","35","false","rohan"]
print(friends)

friends.append("saif")
print(friends)
print("================================================")

# use sort method :

list=[1,60,47,8,0,4]
print(list)

list.sort()
print(list)
print("==================================================")
# use reverse methos :

list1=[10,20,30,40,50]
print(list1)

list1.reverse()
print(list1)
print("===================================================")

# use insert method

list2=[1,2,3,4,5,6,7,8]
print(list2)

list2.insert(2,9)    #two is a index number, and insert 9
print(list2)
print("====================================================")

# use pop method:

list3 = [50,100,200,300,400]
print(list3)

list3.pop(2)
print(list3)        # use pop method to delet num (200) from list throgh index 2:
print("=====================================================")

# use remove mwthod :

list4 =[20,30,40,50,60]
print(list4)

list4.remove(20)    # remove 20 from list using remov method :
print(list4)