# Allein Dane G. Maninang
# August 5, 2024
# CS-201/6DSAL

#List
#statistics to use mean function
import statistics 

#function for taking the average of the list
def average(numbers):
    average = statistics.mean(numbers)
    return average

#declaration of list
numbers = []

#while loop for the validation of inputs
while (len(numbers) != 5):
    number = int(input(f"{len(numbers)+1}. Enter an Integer: "))
    if -20 <= number <= 20:
        numbers.append(number)
    else:
        print("Invalid Input")
        continue

#prints the list of numbers and its average
print(f"The Average of {numbers} is: {average(numbers)}")

#Tuples
#function for the "^_^" separator
def separator(tupless):
    final = ""
    counter = 0
    for i in tupless:
        counter += 1
        if counter == 5:
            final += f"{i}"
        else:
            final += f"{i} ^_^ "
    return final

#turning the list into tuple
tupless = tuple(numbers)

#printing of the elements in the tuple with "^_^" separator
print(separator(tupless))

#Sets
#function for adding the squares of the elements in the set
def squaress(setss):
    squares = []
    for i in setss:
        squares.append(i**2)

    for i in squares:
        setss.add(i)

    return setss

#function for removing the negative elements in the set
def negativess(setss):
    negatives = []
    for i in setss:
        if i < 0:
            negatives.append(i)
        else:
            continue

    for i in negatives:
        setss.remove(i)

    return setss

#turning the tuple into set
setss = set(tupless)

#using the squaress function
setss = squaress(setss)

#using the negativess function
setss = negativess(setss)

#printing the final set
print(setss)

#Dictionary
#function for inverting the keys and values of the dictionary
def invert(dictionary):
    dictionary2 = {}
    for i, j in zip(dictionary.keys(), dictionary.values()):
        dictionary2[j] = i

    return dictionary2

#initiating the dictionary
dictionary = {}

#appending keys and values in dictionary
for i in setss:
    dictionary[i] = i*23

#inverting the dictionary using invert function
dictionary = invert(dictionary)

#printing the final dictionary
print(dictionary)
