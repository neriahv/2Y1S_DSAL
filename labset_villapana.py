# Neriah Faith L. Villapana
# 6DSAL / CS-202
# July 14, 2024

# Set for each color: 
red = {1, 5, 6, 8}
orange = {1, 3, 4, 7, 9}
yellow = {1, 3, 5, 6, 9}
blue = {2, 3, 4, 6, 10}
purple = {2, 5, 7, 8, 10}
green = {2, 4, 7, 8, 9, 10}

# Created a set for all students using ".union" to compare it to other sets that needs all of the students
students = red.union(orange, yellow, blue, purple, green)

# a. The set of students who like both red and orange.
    # I used intersection to find the students who are both in red and orange sets.
likeRO = red.intersection(orange)

# b. The set of students who like all three colors - blue, green and purple. 
    # I used intersection to find the students who are all in the blue, green, purple sets.
likeBGP = blue.intersection(green, purple)

# c. The set of students who do not like yellow.
    # I used difference to find the students who are not in yellow set.
notlikeyellow = students.difference(yellow)

# d. The set of students who like blue but not green.
    # I used difference to find the students who are in the blue set but not in the green set
likeblue_notgreen = blue.difference(green)

# c. The union of the sets of students who like red, orange and yellow.
    # I used union to combine all of the students who are in the red, orange, and yellow sets.
likeROY = red.union(orange, yellow)

# Print the new sets
print("Students who like both red and orange color =" , likeRO)
print("Students who like all three colors - blue, green, and purple =", likeBGP)
print("Students who do not like yellow =", notlikeyellow)
print("Students who like blue but not green =", likeblue_notgreen)
print("Students who like red, orange, and yellow =", likeROY)