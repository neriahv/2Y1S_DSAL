def get_non_positive_integer():
    while True:
        try:
            value = int(input("Enter a non-positive integer: "))
            if value <= 0:
                return value
            else:
                print("Please enter a non-positive integer (zero or negative number).")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    array = []
    print("Enter non-positive integers to create a 3x3 array:")
    for i in range(3):
        row = []
        for j in range(3):
            value = get_non_positive_integer()
            row.append(value)
        array.append(row)

    print(array)

    total_sum = 0
    for row in array:
        for value in row:
            total_sum += value
            
    print(f"The sum of all elements in the array is: {total_sum}")