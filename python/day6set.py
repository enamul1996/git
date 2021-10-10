#set does not store value by index
#set only stores unique

#  setA = {1 , 2 , 3 , 4 , 5 , 6 , 56 , 45 , 95}
# print(setA)
#print(setA[5])

# setB = {41 , 23 , 45 , 31 , 53 , 56 }
# for a in setB:
#     print(a)

# setB.remove(45)    
# print(setB)

# setB.pop()
# print(setB)

# setB.clear()
# print(setB)

# del setB
# print(setB)

# setC = {36 , 76 , 56}
# setC.update([4,6,7,3,9])
# setC.update("enamul")
# setC.update((2,4,5,3,6,34,6))
# setC.update([1,3,2,45,5,3])
# print(setC)

# setD = {34,45,56,76}
# setE = setD.copy()
# print(setE)
# print(setD)
# setE.remove(34)
# print(setE)
# print(setD)

# setJ = {5,4,6,3,7,9}
# setK = (4,3,2,4,5,3,5)
# print(setK.difference(setJ))
# print(setJ.difference(setK))

# setJ = {5,4,6,3,7,9}
# setK = (4,3,2,4,5,3,5)
# setJ.difference_update(setK)
# print(setJ)
# setK.difference_update(setJ)
# print(setK)

# setJ = {5,4,6,3,7,9}
# setK = (4,3,2,4,5,3,5)
# print(setJ.intersection(setK))
# setJ.intersection_update(setK)
# print(setJ)
# setK.intersection_update(setJ)
# print(setK)

# setJ = {5,4,6,3,7,9}
# setK = (4,3,2,4,5,3,5)

# setJ.add(34)
# print(setJ)

# setJ.discard(5)
# print(setJ)

# setL = {1,2,3,4,5,6}
# setM = {1,2,3,4,5,6,7,8,9}
# print(setL.issubset(setM))
# print(setL.issuperset(setM))


# setN = {6,4,8,4}
# setO = {5,4,7,45,54,87}
# print(setN.union(setO))

# setP = {122,444,556}
# setQ = {1231,333,4445}
# print(setP.symmetric_difference(setQ))
# setP.symmetric_difference_update(setQ)
# print(setP)


# true when no element is common among sets
# print(setP.isdisjoint(setQ))