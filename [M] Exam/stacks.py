index_cards = []

print("Let us now organize your index cards for your graded recitation!")

while True:
    lastname = input("Input student's last name: ")
    duplicate_found = False  # Track if a duplicate was found

    for i in range(len(index_cards)):
        if index_cards[i].startswith(lastname + " "):
            match = index_cards[i]
            index_cards.pop(i)
            duplicate_found = True

            print("There is an existing student with the same last name.")
            
            # Get the existing first name for the current student
            existing_firstname = input("Input the existing student's first name: ")
            
            # Update the existing entry with the new first name
            index_cards.append(lastname + " " + existing_firstname)
            
            # Get the new student's first name
            new_firstname = input("Input the new student's first name: ")
            index_cards.append(lastname + " " + new_firstname)
            break  # Exit the loop after handling the duplicate

    if not duplicate_found:
        # Get the student's first name and append the full name if no duplicate
        index_cards.append(lastname + " ")

    index_cards.sort()
    print("\nIndex Card List:")
    for card in reversed(index_cards):
        print(card)
    
    if len(index_cards) == 5:
        choice = input("\nYou have reached the maximum limit of 5 index cards! Do you wish to add more (Y/N)?: ").strip().upper()
        if choice == 'Y':
            removed_card = index_cards.pop() 
            print(f"{removed_card} has been removed.")
        elif choice == 'N':
            break
        else:
            print("Invalid input. Please enter Y or N.")

print("Thank you and have a good day!")
