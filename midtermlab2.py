student_list = []

print("Let us now organize your index cards for your graded recitation!")

while True:
    lastname = input("\nInput student's last name: ").strip()

    if len(student_list) == 5:
        popped = student_list.pop(0)
        print(popped + " has been removed")

    if lastname == "" or lastname.isdigit():
        print("Error input. Try again.")
        continue

    found = False
    for i in range (len(student_list)):
        if student_list[i] == lastname:
            found = True
            print("There is an existing student with same last name.")
            exist_first = input("Input existing student's first name: ")
            student_list[i] = lastname + " "  + exist_first
            new_first = input("Input new student's first name: ")
            student_list.append((lastname + " " + new_first))

    if not found:
        student_list.append(lastname)

    student_list.sort()
    print("Index Card List: ")
    for x in student_list:
        print(x)

    if len(student_list) == 5:
        choice = input("\nYou have reached the maximum limit of 5 index cards! Do you wish to add more (Y/N)? : ").upper().strip()
        if choice == 'Y':
            continue
        if choice == 'N':
            break
    
print("Thank you and have a good day!")