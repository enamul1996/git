# class Duck(object):
#     def talk(self):
#         print('quack quack')

# class Human(object):
#     def talk(self):
#         print('hello hi')

# def call_talk(obj):
#     obj.talk()

# x = Duck()
# y = Human()
# call_talk(x)
# call_talk(y) 

# class Dog:
#     def bark(self):
#         print('Bow Bow')

# class Duck(object):
#     def talk(self):
#         print('quack quack')

# class Human(object):
#     def talk(self):
#         print('hello hi')

# def call_talk(obj):
#     obj.talk()

# def call_bark(obj):
#     obj.bark()    

# x = Dog()
# y = Duck()
# z = Human()

# call_bark(x)
# call_talk(y)
# call_talk(z)

# class Dog:
#     def bark(self):
#         print('Bow Bow')

# class Duck(object):
#     def talk(self):
#         print('hello hi')

# def call_talk(obj):
#     if(aaabbb(obj,'talk')):
#         obj.talk()    
#     elif(aaabbb(obj,'bark')):
#         obj.bark()
#     else:
#         print("incorrect")

# x = Dog()
# y = Duck()
# z = Human()

# call_bark(x)
# call_talk(y)
# call_talk(z)

# #operator overloading

# print(6+6)
# print('enamul'+'hussain')


# class Bookx():
#     def __init__(self,pages):
#         self.pages = pages

# class Booky():
#     def __init__(self,pages):
#         self.pages = pages

# b1 = Bookx(100)
# b2 = Booky(200)

# print(b1 + b2)


# class Bookx():
#     def __init__(self,pages):
#         self.pages = pages

#     def __add__ (self,other):
#         return self.pages + other.pages    

# class Booky():
#     def __init__(self,pages):
#         self.pages = pages

#     def __add__ (self,other):
#         return self.pages + other.pages      

# b1 = Bookx(100)
# b2 = Booky(200)

# print(b1 + b2)

# class Bookx():
#     def __init__(self,pages):
#         self.pages = pages

# class Booky():
#     def __init__(self,pages):
#         return self.pages

#     def __add__(self,other):
#         return self.pages + other.pages

# b1 = Bookx(100)
# b2 = Booky(200)
# print(b2 + b1)               
        
#amazon method overloading

# search(a)
# search(a,b)
# search(a,b,c)

class ClassMy:
    def sum(self,a = None,b = None,c = None):
        if(a != None and b != None and c != None):
            print(a+b+c)
        elif(a != None and b != None):
            print(a+b)
        else:
            print('Please enter a valid input')   

b = ClassMy()
b.sum(4,3)
b.sum(6,4,5)
b.sum(9) 
                
                