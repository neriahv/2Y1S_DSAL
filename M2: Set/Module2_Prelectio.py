# SETS
#   - unordered and unindexed (no index property)
#   - all the elements must be unique (no duplicate elements)
#       - if there is a duplicate element, the python will disregard it
#   - use curly braces { }
#   - support union (joining or adding), intersection (same), difference (an element on x that is not in y)

# Sets with duplicate
samset = {"sun", "moon", "star", "cloud", 1.0, 1, -6, -6.0}
# result: {1.0, -6, 'sun', 'moon', 'star', 'cloud}
    # positive number - prioritize the FLOAT (ex: 1.0 vs 1 = 1.0 )
    # negative - prioritize the INT (ex: -6 vs -6.0 = -6)

# Acessing items in the sets
samsets = {"sun", "mon", "tue"}
for x in samsets:
    print(x)
    # result: (unordered) tue \n sun \n mon

# Checking if in the set
samsets1 = {"sun", "mon", "tue"}
print ("thurs" in samsets1)
# result: False

# Adding items in the set (use add())
samsets2 = {"sun", "mon", "tue"}
samsets2.add("wed")
print (samsets2)
# result (ex): {'tue', 'wed', 'mon', 'sun'}
# it will be put in any order

# Adding MULTIPLE items (use update())
samsets3 = {"sun", "mon", "tue"}
samsets3.update(["wed", "thurs", "fri", "sat"])
print(samsets3)
# result (ex): {'thurs', 'fri', 'sat', 'mon', 'tue', 'wed', 'sun'}
# no [ ] result: {'sun', 'a', 't', 's', 'w', 'e', 'r', 'i', 'tue', 'd', 'u', 'f', 'h', 'mon'}

# Joining two sets (use .union())
samsets4 = {"sun", "mon", "tue"}
samsets5 = {1, 2, 3}
samsets6 = samsets4.union(samsets5)
# union CREATES a new set
print(samsets6)
# result : {1, 2, 3, 'tue', 'mon', 'sun'}

# Discarding an item in the sets (use .discard())
samsets7 = {"sun", "mon", "wed", "fri"}
samsets7.discard("sun")
print(samsets7)
# result: {'mon', 'wed', 'fri'}
# will not ERROR even if the stated item on the discard method is not existing
    # note: but .remove() will return error
# but will return an error if (ex) you discard sun without ""

# Differentiating items in the sets (use .difference())
    # return a set that contains the items that only exist in set x and not in set y
    # creating a NEW SET
samsets8 = {"sun", "thu", "tue", "wed"}
samsets9 = {"mon", "thu", "tue", "fri"}
x = samsets8.difference(samsets9)
print(x)
# result: {'sun', 'wed'}
    # in x but not in y

y = samsets9.difference(samsets9)
print(y)
# result: {'mon', 'fri'}

# Intersecting of items in the set
    # what is in x and in y
samsets8 = {"sun", "thu", "tue", "wed"}
samsets9 = {"mon", "thu", "tue", "fri"}
a = samsets8.intersection(samsets9)
print(x)
# result: {'thu', 'tue'}
samsets10 = {1, 2, 3}
b = samsets9.intersection(samsets10)
# result: set()
    # even if nothing is the same, will not have an error but EMPTY set

# SAME FUNCTIONS IN LIST AND TUPLE:
    # Removing (.remove())
    # Length (len())
    # Pop (.pop())
        # - Note: Sets are unordered, so when using the pop() method you will not know which item gets removed.
    # Delete (del)
        # - Note: will return an error if the deleted set is printed
        # deleting the whole set
    # Clear (.clear())
        # - Note: will return set()
        # clearing only the elements

