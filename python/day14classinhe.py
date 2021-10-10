# SINGLE INHERITANCE

# class Bank(object):
#     cash = 20500

#     @classmethod
#     def available_bal(cls):
#         print(cls.cash)

# class SBI(Bank):
#     cash = 50000
#     @classmethod
#     def available_bal(cls):
#         print(cls.cash + Bank.cash)

# class PNB(Bank):
#     pass
# pnb = PNB()
# pnb.avilable_bal()

# sbi = SBI()
# sbi.available_bal()

#MULTI-LEVEL INHERITANCE

# class GrandFather(object):

#     lastName = "mazumdar"
#     def __init__(self,firstName):
#         self.firsiName = firstName

#     def display(self):
#         print(self.firstName + " " + self.lastName)

# class Father(GrandFather):

#     def __init__(self, firstName,ffirstName):    
#         super().__init__(firstName)
#         self.ffirstName = ffirstName

#     def display(self):
#         print(self.ffirstName + " " + self.lastName)
#         super().display()

# class Son(Father):

#     def __init__(self, firstName, ffirstName, sfirstName):
#         super().__init__(firstName, ffirstName)
#         self.sfirstName = sfirstName

#     def display(self):
#         print(self.sfirstName + " " + self.ffirstName + " " + self.astName)
#         super().display()            

# enamul = Son("mazumdar" , "hussain" , "enamul")
# enamul.display()

# MULTIPLE INHERITANCE

# class Father:

#     def height(self):
#         print('6 feet tall')

# class Mother:
#     def color(self): 
#         print('Color is brown')  

# class Son(Father,Mother):
#     pass

# enamul = Son()
# enamul.color()
# enamul.height()

#-------------------------------------------------------

# class Father:

#     def name (self):
#         print('name called from father')

# class Mother:

#     def name(self):
#         print('name called from mother') 

# class Son(Mother, Father)
#     pass

# enamul = Son()
# enamul.name()

# METHOD RESOLUTION ORDER

class A(object):
    def method(self):
        print('A class method')
        super().method()

class B(object):
    def method(self):
        print('B class method')
        super().method()

class C(object):
    def method(self):
        print('C class method')

class X(A,B):
    def method(self):
        print('X class method')
        super().method()

class Y(B,C):
    def method(self):
        print('Y class method')
        super().method()

class P(X,Y):
    def method(self):
        print('P class method')
        super().method()

p = P()
p.method()        
