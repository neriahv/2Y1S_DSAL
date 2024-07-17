# Neriah Faith L. Villapana
# 6DSAL \ CS-202
# July 17, 2024

# 2. Create a text file in the D:\ drive with the following information
    # a line of code to write a new text file
myfile = open ("D:\\filehandling_villapana.txt", "w+")
    # Printing the informationes needed
myfile.write("Student Name: Neriah Faith L. Villapana")
myfile.write("\nStudent Number: 20829374")
myfile.write("\nAffilliations/Organizations: League of Outstanding Programmers & USG Senate")
myfile.write("\nGuiding principle (motto) in life: Everything happens for a reason")
myfile.close() # saves & closes the file

# 4. After creating the text file, perform the following file handling actions:
    # a line of code to read a text file
myfile = open ("D:\\filehandling_villapana.txt", "r")
    # 4.1) display output of read() - displaying the whole text file
print("\nThe output of read() is: \n" + myfile.read())
myfile.seek(0) # to move the cursor in the beginning
    # 4.2) display the output of readline() - displaying the first line
print("\nThe output of readline() is: \n" + myfile.readline())
myfile.seek(0)
    # 4.3) display the output of read(23) - displaying a part of a text file
print("The output of read(23) is: \n" + myfile.read(23))
myfile.seek(0)
    # 4.4) display the output of readline(5) - displaying a part of a text file
print("\nThe output of readline(5) is: \n" + myfile.readline(5))
myfile.close()

    # a line of code to append a data in text file
myfile = open ("D:\\filehandling_villapana.txt", "a")
    # 4.5) appending the text below
myfile.write("\nHoly Angel University\n")
myfile.write("Laus Deo Semper \n")
myfile.close()
    # a line of code to read again the UPDATED text file 
myfile = open ("D:\\filehandling_villapana.txt", "r")
    # 4.5) displaying the entire content of the file
print("\n" + myfile.read())