""" What is COLLECTION?
     - It is a built-in Python module that implements specialized container data types providing 
       alternatives to Python's general purpose built-in containers such as lists, tuples, and sets. """

#  LIST [ ]
#    - contains multiple data items
#    - ordered & mutable

myList = ["sun", "moon", "star", "cloud"]

# Printing the whole list
print(myList) #result: ['sun', 'moon', 'star', 'cloud']
# Accessing element
print(myList[1]) #result: moon
# Access range
print(myList[2:4]) #result: ['star', 'cloud']
print(myList[:3]) #result: ['sun', 'moon', 'star']
print(myList[2:]) #result: ['star', 'cloud']
print (myList[-1]) #result: cloud
# Change item
myList[3] = "rain"
print(myList) #result: ['sun', 'moon', 'star', 'rain']
# Add item
print(myList.insert(1, "cloud")) 
# Remove (using the elements)
print(myList.remove("star"))
# Remove (using index)
print(myList.pop(2))
# Remove (using 'del')
del myList[0]
print(myList)
# Clear the empty
print(myList.clear())
# Count an item 
myList1 = [1, 2, 3, 4, 1, 2]
print(myList.count(1))
# Reverse an item
print(myList1.reverse())
# Sort
print(myList1.sort())
# Extend
print(myList1.extend(myList))
# Copy the entire list
myList_copy = myList1.copy()
print(myList_copy) #result: [1, 2, 3, 4, 1, 2]
# Access using for loop
for x in myList1:
    print(x)
# Check if it is in a list
if 1 in myList1:
    print("Yes")


# TUPLE ( )
#    - ordered and immutable
#    - accessing, range, iteration, len, and checking is the same in LIST

myTuple = (5, 6, 7, 8, 9, 10)
# deleting tuple
    # del myTuple
    # print(myTuple) #result: ERRORRRRR
# finding the index of an item
myTuple1 = (5, 6, 7, 8, 9, 10)
print(myTuple.index(8))
# count a item
print(myTuple.count(8))
# join a tuple
myTuple2 = (1, 2, 3, 4)
print(myTuple + myTuple2)
# sort
myTuple3 = (2, 5, 7,23 ,87)
list(myTuple3).sort()
print(myTuple3)
# Changing (since tuple is immutable, change it into list first)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) # result: ('apple', 'kiwi', 'cherry')
