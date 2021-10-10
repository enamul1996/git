# class Student:
#     age = 26
#     language = 'asamese'
#     fullName = 'enamul hussain'

#     def display(self):
#         print(self.fullName)
#         print(self.language)
# enamul = Student()    
# enamul.display()

# print(enamul.age)
# print(enamul.language)
# print (enamul.fullName)

# hussain = Student()
# enamul.age = 36
# hussain.display()

# print(enamul.age)
# print(hussain.age)




# class Student:
#     def __init__(self,nm=0,ag=0,gr=0):
#         self.name = nm
#         self.age = ag
#         self.gender = gr

#     def display(self):
#         print(self.name)

# enamul = Student(ag=23,nm='enamul',gr ='Male')
# hussain = Student('hussain','34','male')

# enamul.display()
# hussain.display()

# class Bank:
#     def __init__(self,accNo,accName,bal):
#         self.accountNumber = accNo
#         self.accName = accName
#         self.balance = bal

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#     def withDrawl(self,amount):
#         if(amount<self.balance):
#             self.balance = self.balance - amount
#         else:
#             print('Insufficient Balance')    

# enamul = Bank(324, "enamul hussain", 1500)
# enamul.withDrawl(550)
# print(enamul.balance)
# enamul.deposit(134134)
# print(enamul.balance)