# # problem 4
# class Car:
# # class variable

#     madeIn = "India"
#     def __init__(self,color,type,regNo):
# # instance variable
#         self.color = color
#         self.type = type
#         self.regNo = regNo

# tata = Car("blue","SUV",653)
# mahindra = Car("silver","MUV",757)
# hindustan = Car("white","sedane",767)

# print(tata.madeIn)
# tata.madeIn = "US"

# print(tata.madeIn)
# print(tata.color)
# print(mahindra.madeIn)
# print(hindustan.madeIn)
# mahindra.color = "red"
# print(mahindra.color)

# # program 5

# class calculate:
#     def __init__(self):
#         self.x = 25
#     def modify(self):
#         self.x = self.x + 10.7
# s1 = calculate()
# s2 = calculate()

# print(s1.x)
# print(s2.x)

# s1.modify()
# print(s1.x)
# print(s2.x)

# s2.modify()
# print(s2.x)

# # program 6

# class Car:
#     #class variable
#     madeIn = "India"

#     @classmethod
#     def modify(cls):
#         cls.madeIn = "germany"

#     def __init__(self,color,type,regNo):
#         #instance variable
#         self.color = color
#         self.type = type
#         self.regNo = regNo

# tata = Car("blue","SUV",653)
# mahindra = Car("silver","MUV",757)
# hindustan = Car("white","sedane",767)            

# tata.modify()
# Car.modify()
# print(tata.madeIn)

# tata.madeIn = "france"
# print(tata.madeIn)
# print(mahindra.madeIn)
# print(hindustan.madeIn)

#program 7

class Student:
    #constructor
    def __init__(self,n='',m=0):
        self.name = n
        self.marks = m

    def display(self):
        print(self.name)
        print(self.mark)

    def calculate(self):
        if self.mark >= 60:
            print('Division A')
        elif self.mark > 50 and self.mark < 60:
            print('Division B')    
        else:
            print('Division C')    

e =[ Student('enamul',48) , Student('husssain',62) , Student('mazumdar',72)]

for item in e:
    item.calculate()
