# program will be menu driven and allow user to create text file of numbers
# and return average and total
# 2/8/2021
# M7HW_FileExceptions
# Khalil Kachmar

# Display Menu
#         1. Create Text File
#         2. Average Values
#         3. Total Values
#         4. Exit Program
#         
#         Enter your selection: 
# Input selectin
# If selection == 1:
    # Set numbers = numbers.txt
    # Display "Enter at least 5 numbers: "
    # Input nums
    # With numbers:
        # Write nums
# If selection == 2:
    # Open numbers.txt
    # Average(nums) for nums in numbers.txt
# If selection == 3:
    # Open numbers.txt
    # Sum(nums) for nums in numbers.txt
# If selection == 3:
    # Exit

def menu():
    print("Menu")
    print("1. Create Text File\n"
          "2. Average Values\n"
          "3. Total Values\n"
          "4. Exit Program\n")
    
    try:
        choice = int(input("Enter your choice(1-4): "))
        return choice
    except ValueError:
        return 5
    
def create_file():
    numbers = []
    for i in range(5):
        valueerror = True
        while valueerror:
            try:
                num = float(input(f"Number {i + 1}: "))
                numbers.append(num)
                valueerror = False
            except ValueError:
                print("You must enter a number.")
    
    more = True
    i = 6
    while more:
        more_entries = input("Would you like to enter another number(y/n)?: ")
        if more_entries.lower() == 'n':
            more = False
        elif more_entries.lower() == 'y':
            valueerror = True
            while valueerror:
                try:
                    num = float(input(f"Number {i}: "))
                    numbers.append(num)
                    i += 1
                    valueerror = False
                    
                except ValueError:
                    print("You must enter a number.")
        else:
            continue
        
    number_file = open('numbers.txt', 'w')
    with number_file:
       for number in numbers:
           print(f'{number}', file=number_file)
     
     
def get_average():
    total = 0
    number_of_items = 0
    number_file = open('numbers.txt', 'r')
    with number_file:
        for number in number_file:
            number_of_items += 1
            total += float(number)
    average = total/number_of_items
    
    return average
    
def get_total():
    total = 0
    number_file = open('numbers.txt', 'r')
    with number_file:
        for number in number_file:
            total += float(number)
    return total
           
def main():
    show_menu = True
    while show_menu:
        choice = menu()
        if choice == 1:
            create_file()
        elif choice == 2:
            try:
                average = get_average()
                print(f'Average: {average}\n')
            except FileNotFoundError:
                print("No file exists. Please create file first.\n")
        elif choice == 3:
            try:
                total = get_total()
                print(f"Total: {total}\n")
            except FileNotFoundError:
                print("No file exists. Please create a file first.\n")
        elif choice == 4:
            print("Goodbye")
            show_menu = False
        else:
            print("That is not a valid option.\n")
           
if __name__ == "__main__":
    main()