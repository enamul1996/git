# class Student:
#     country = "India"
#     def __init__(self,name,lang):
#         self.name = name
#         self.lang = lang

#     def totalMarks(self):
#         self.sum = 0
#         for x in self.lang:
#             self.sum = self.sum + x
#             return self.sum

#     def percentage(self):
#         self.percentage = 0
#         self.percentage = (self.sum/len(self.lang)*100)*100
#         return self.percentage

#     @classmethod
#     def updateCountry(cls,Cname):
#         cls.country = Cname
        
# enamul = Student("enmaul",[56,76,86,68,64])        
# hussain = Student("hussain",[64,45,67,75,69])  

# a = enamul.totalMarks()
# print(a)
# b = hussain.totalMarks()
# print(b)
# c = enamul.percentage()
# print(c)
# d = hussain.percentage()
# print(d)
# average = c + d
# print(average/2)

#-----------------------------------------------------------------------------

class Student():
    count = 0
    def __init__(self,name,rollNum):
        self.name = name
        self.roll = rollNum
        Student.updateCount()

    def display(self):
        print('hello')    

    @classmethod
    def updateCount(cls):
        cls.count = cls.count + 1

    @staticmethod
    def countOnObject():
        return Student.count

e = Student('enam',24)
f = Student('huss',36)

e.display()
f.display()

print(Student.countOnObject())
