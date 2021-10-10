# OVERRIDING

#different class, same method name, same signature
#inheritance -- override inheritance

# world - save(a)
# sbi - save(a)
# a = sbi()

# class WorldBank():
#     def Saving(self,amount):
#         if(amount > 1000):
#             print('Saving successful')

# class SBIBank(WorldBank): 
#     def Saving(self, amount):
#         if(amount > 500):
#             print('SBI Saving successful')
#         else:
#             print('Minimum bal should be 500')

# class BOIBank(WorldBank):
#     def Saving(self, amount):
#         if(amount > 500):
#             print('BOI saving successful')                           
#         else:
#             print('Minimum bal should be 500')

# SBIBank().saving(499)

#overloading - same class, same method name , different signature 
#overriding  - different class have inheritance, same method, same signature

import math
class Square():
    def area(self,x):
        print(x*x)

class Circle(Square):
    def area(self,x):
        print(math.pi*x*x) 

c = Circle()
c.area(23)

d = Square()
d.area(23)