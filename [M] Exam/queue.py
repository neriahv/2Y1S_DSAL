index_list = []

print("Let us now organize your index cards for your graded recitation!")
while True:
    lastname = input("\nInput student's last name: ")
    duplicate = False

    for i in range(len(index_list)):
        if index_list[i] == lastname:
            duplicate = True
            matched = index_list[i]
            index_list.remove(matched)
        
            print("There is an existing student with same last name.")
            exist_firstname = input("Input existing student's first name: ")
            index_list.append(lastname + " " + exist_firstname)
            new_firstname = input("Input new student's first name: ")
            index_list.append(lastname + " " + new_firstname)

    if not duplicate:
        index_list.append(lastname + "")

    print("Index Card List: ")
    index_list.sort()
    for x in index_list:
        print(x)

    if len(index_list) == 5:
        choice = input("You have reached the maximum limit of 5 index cards! Do you wish to add more (Y/N)? : ").strip().upper()
        if choice == "Y":
            popped = index_list.pop(0)
            print(popped + " will be removed.")
        elif choice == "N":
            break
        else: 
            print("Invalid choice. Please choose Y or N.")

print("Thank you and have a good day!")

    