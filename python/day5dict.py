# DICTIONARY

# # human = ["enamul","hussain",26,57]
# # # print(human)
# # # print(type(human))
# # # print(human[0])
# person = {
#
#         'firstName':"enamul",
#         'lastName':"hussain",
#         'rollNo':26,
#         'age':57
#
# }
#
#
# print(type(person))
# print(person)
# print(person['firstName'])
# print(person['lastName'])
#
#
#
#
# for x in person:
#     print(x,person[x])
#
#
# for x in person.keys():
#     print(x)
#
# for x in person.values():
#     print(x)
#
#
# for x,y in person.items():
#     print(x,y)
#
# students = [
#     {
#
#         'firstName':"amit",
#         'lastName':"kumar",
#         'rollNo':23,
#         'age':27
#
#     },
# {
#
#         'firstName':"enamul",
#         'lastName':"hussain",
#         'rollNo':26,
#         'age':57
#
#     },
# {
#
#         'firstName':"ajay",
#         'lastName':"pawar",
#         'rollNo':39,
#         'age':53
#
#     }
#
# ]
#
#
# dictOne = students[0]
# print(dictOne)
# print(dictOne['lastName'])
#
# # print(students[1]['age'])
# # print(students[2]['firstName'])
# #students = [dictOne,dictTwo,dictThree]
# for item in  students:
#     dict = item
#     for key,val in dict.items():
#         print(key,val)
# #---------------------------------------------
# vehical =
# {
#     'color':"Yellow",
#     'regNo':354,
#     'language':'Hindi'
# }
# print(vehical)
# print(vehical['color'])
#
# for key in vehical:
#     print(key,vehical[key])
#
# for key in vehical.keys():
#     print(key)
#
# for key in vehical.values():
#     print(key)
#
# for x,y in vehical.items():
#     print(x,y)
#
# listA = [{'firstName':"enamul"},{'firstName':"amit"},{'firstName':"ajay"}]
# print(listA[0]['firstName'])
#
# for item in listA:
#     dict = item
#     for x,y in dict.items():
#         print(x,y)
#
#
# #-----------------------------------------
#
#
# h = {
#     'age':32,
#     'roll':65,
#     'id':'6754'
# }
#
# # h['id'] = 654
# # print(h)
#
# j = h
# print(j)
# print(h)
#
# j['id'] = 674
#
# print(j)
# print(h)
#
#
#
# nn = {}
# mm = nn.copy()
# mm['age'] = 65
# print(nn)
# print(mm)
#
# # to fetch the value from dictionary
# print(nn['age'])
#
# # to fetch the value from dictionary
# print(nn.get('age'))
#
# nn.pop('age')
# print(nn)



#---------------------Dict--------------------

# amit = {
#     'firstName':"amit",
#     'lastName': "kumar",
#     'age': 43,
#     'rollNo': 15,
#     'skills':["python","java","c#"]
# }

# # by square braacket notation
# print(amit['firstName'])
# # by get method
# print(amit.get('firstName'))

# # Updating the value
# amit['firstName'] = "amol"
# print(amit)
# #Updating the value by update method
# amit.update({'language':"english"})
# amit.update({'language':"Hindi"})
# print(amit)
# #Deleting the values from dictionary

# amit = {
#     'firstName':"amit",
#     'lastName': "kumar",
#     'age': 23,
#     'rollNo': 45,
#     'skills':["python","java","c#"]
# }

# amit.popitem()
# print(amit)
# amit.pop('lastName')
# print(amit)

# #
# # amit.clear()
# # print()

# ajay = amit.copy()
# print(ajay)
# print(amit)

# amit['age']= 44
# print(ajay)
# print(amit)

# # setdefault
# amit.pop('age')
# print(amit.setdefault('age',56))
# print(amit)


# y = ['age','rollNumber','name']
# x = [1,2,3]
# bh = dict.fromkeys(y,x)
# print(bh)



# amit = {
#     'firstName':"amit",
#     'lastName': "kumar",
#     'age': 23,
#     'rollNo': 45,
#     'skills':["python","java","c#"]
# }


# for key in amit:
#     print(key , amit[key])

# for x in amit.keys():
#     print(x)

# for x in amit.values():
#     print(x)

# for x,y in amit.items():
#     print(x,y)





























# h.clear()
# print(h)

# del h
# print(h)


















