# # program One
# class Student:
#     def __init__(self):
#         self.name = "enamul"
#         self.age = 25
#         self.mark = 90
#         print(self.mark)
#     def info(self):
#         print('Hi my name is ' + self.name)    
#         print(self.age)
# enamul = Student()  
# enamul.info()    
  

# # program Two
# class Student:
#     def __init__(self,nm,ag,mrk):
#         self.name = nm
#         self.age = ag
#         self.marks = mrk
#     def info(self):
#         print('Hi my name is '+ self.name)    
#         print('and age is ' + str(self.age))
#         print('I got ' + str(self.marks) + ' marks') 
        
# enamul = Student("enamul" , 25 , 60)        
# enamul.info()
# enamul.language = "assamese"
# print(enamul.language)
# enamul.language = "bengali"
# print(enamul.language)


# # program Three
# class Student:
#     def __init__(self, n = "", m = 0):
#         self.name = n
#         self.marks = m
#     def display(self):
#         print('Hi',self.name)    
#         print('My marks',self.marks)

# e = Student("enamul",67)        
# e.display()


# program Four
class Person:
    def __init__(self,nm,ag,lang,adno):
        self.name = nm
        self.age = ag
        self.language = lang   
        self.adharNo = adno    
   
    def display(self):
        for name in self.name:
            print('My name is',name)
        print('My age is',self.age)
        print('my language is',self.language)
        print('My adhar no is',self.adharNo)        

en = Person("Enamul",25,"Bengali",9049867634)
en.display()