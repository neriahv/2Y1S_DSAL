# LIST
numList = []
while (len(numList) != 5):
    integer = int(input("Enter 5 integers: "))
    if -20 <= integer <= 20:
        numList.append(integer)
    else:
        print("Invalid. Try again.")
        continue
print("List = ", numList)

counter = 0
for i in numList:
    i += i
    counter += 1

ans = i / counter
print("Average = ", "%.2f"%ans)

# TUPLE
myTuple = tuple(numList)

def tuple_to_string(the_tuple_here, separator_here):
    string_elements = [str(element) for element in the_tuple_here]
    return separator_here.join(string_elements)

final_tuple = tuple_to_string(myTuple, " ^_^ ")
print(final_tuple)

# SET
squares = set()
myfinalset = set()

mySet = final_tuple.split(" ^_^ ")

mySet_list = [int(x) for x in mySet]
mySet = set(mySet_list)

for i in mySet:
    if i >= 0:
        squares.add(i**2)
mySet.update(squares)
for x in list(mySet):
    if x < 0:
        mySet.remove(x)
print(mySet)

# DICTIONARY
multiplied = set()
myDict = {}

# setting the keys and value
for element in mySet:
    myDict[element] = element * 23

# invert keys to value
def invert_dict (dict):
    inverted = {}
    for key, value in dict.items():
        inverted[value] = key
    return inverted

# calling and printing
inverted_dict = invert_dict(myDict)
print(inverted_dict)