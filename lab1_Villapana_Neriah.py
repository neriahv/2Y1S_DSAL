# Neriah Faith L. Villapana
# DSAL / CS-202
# July 10, 2024

dsal_group = ["Justin Pangilinan", "Laurenzo Centeno", "Neriah Villapana", "Shawn Cabutihan"]

print("Our 6DSAL group members: ", dsal_group)
print("Total group members: ", len(dsal_group))
print("Our group leader: ", dsal_group[2])

dsal_group.insert(4, "Khatz Aguilar")
dsal_group.remove("Justin Pangilinan")
dsal_group.sort()

print("New 6DSAL group members: ", dsal_group)

student_numbers = [20867387, 20829374, 20832952, 199603259]
student_numbers.extend(dsal_group)

print("Student Number\tStudent Name")
print(student_numbers[3],"\t", student_numbers[4])
print(student_numbers[2],"\t", student_numbers[5])
print(student_numbers[1],"\t", student_numbers[6])
print(student_numbers[0],"\t", student_numbers[7])
