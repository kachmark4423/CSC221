# Program will be menu driven with options for user to create and manipulate a 
# 3x3 array
# 1/31/2021
# CSC121 M5HW – Array Manipulations
# Khalil Kachmar

# Display 
# "Menu
# -----------------------------------
# 1) Create a 3-by-3 Array
# 2) Display cube Values for elements in array
# 3) Add 7 to every element and display result
# 4) Multiply elements by 6 and display result
# 5) Exit
# Enter your selection:"
# Input selection
# If selection = 1:
#	Declare user_array
#	Display "Enter array values: "
#	Input value(x9)
# If selection = 2:
#	Display user_array ** 3
# If selection = 3:
# 	Display user_array + 7
# If selection = 4:
#	Display user_array * 6
# If selection = 5:
#	Exit


import numpy as np 



def menu():
	print("Menu")
	print("-"*35)
	print("1) Create a 3-by-3 Array\n"
		  "2) Display cube Values for elements in array\n"
		  "3) Add 7 to every element and display result\n"
		  "4) Multiply elements by 6 and display result\n"
		  "5) Exit")
	option = int(input("Enter your selection: "))
	main(option)

def create_array():
	row_1 = []
	row_2 = []
	row_3 = []
	
	print("Enter your array values by row. Values must be even between 2 and 18")
	print("Row ONE Values")
	for i in range(3):
		value = int(input(f"Value {i + 1}: "))
		while value not in range(2, 19, 2):
			print("That value is not valid!")
			value = int(input(f"Value {i + 1}: "))
		row_1.append(value)

	print("Row TWO values")
	for i in range(3):
		value = float(input(f"Value {i + 1}: "))
		while value not in range(2, 19, 2):
			print("That value is not valid!")
			value = int(input(f"Value {i + 1}: "))
		row_2.append(value)

	print("Row THREE values")
	for i in range(3):
		value = float(input(f"Value {i + 1}: "))
		while value not in range(2, 19, 2):
			print("That value is not valid!")
			value = int(input(f"Value {i + 1}: "))
		row_3.append(value)
	
	user_array = np.array([row_1, row_2, row_3])
	print("\nArray:")
	for i in range(3):
		for j in range(3):
			print(f"{user_array[i, j]:>2.0f}", end=' ')
		print('')
	return user_array

def cube_array(array):
	print("\nSquared array:")
	cubed_array = array ** 3
	for i in range(3):
		for j in range(3):
			print(f"{cubed_array[i, j]:>4.0f}", end=' ')
		print('')

def add_seven(array):
	print("\nArray + 7:")
	add_7 = array + 7
	for i in range(3):
		for j in range(3):
			print(f"{add_7[i, j]:>2.0f}", end=' ')
		print('')
def times_six(array):
	print("\nArray * 6:")
	times_6 = array * 6
	for i in range(3):
		for j in range(3):
			print(f"{times_6[i, j]:>3.0f}", end=' ')
		print('')
def main(option):
    global user_array
    if len(user_array) == 0 and option in range(2, 5):
        print("\nArray is empty")
        menu()
    elif option == 5:
        print("Goodbye")
    else:
        if option == 1:
            user_array = create_array()
            menu()
        elif option == 2:
            cube_array(user_array)
            menu()
        elif option == 3:
            add_seven(user_array)
            menu()
        elif option == 4:
            times_six(user_array)
            menu()
        else:
            print("That is not a valid option")
            menu()

if __name__ == "__main__":
    user_array = []
    menu()
