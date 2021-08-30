# Program will prompt user for a 10 character telephone number and return it with 
# alpha characters translated to numerical characters
# 1/31/2021
# CSC121 M6HW – Alpha Tele Num Translator
# Khalil Kachmar

# Declare dictionary
# Set new_number = 'y'
# While new_number == 'y':
#	Display "Enter a 10-character number in the format XXX-XXX-XXXX: "
#	Input user_number
#	For symbol in user_number:
#		If symbol is Alpha:
#			Replace symbol with digit
# 	Display user_number
# 	Display "Would you like to enter another number?(y/n)"
#	Input new_number

def main():
	dictionary = {2: ('a', 'b', 'c'), 3: ('d', 'e', 'f'), 4: ('g', 'h', 'i'),
				  5: ('j', 'k', 'l'), 6: ('m', 'n', 'o',), 7: ('p', 'q', 'r', 's'),
				  8: ('t', 'u', 'v'), 9: ('w', 'x', 'y', 'z') }

	new_number = 'y'

	while new_number.lower() == 'y':
		user_number = input("Enter a 10-character number in the format XXX-XXX-XXXX: ")

		for symbol in user_number:
			if symbol.isalpha():
				for number in dictionary.keys():
					if symbol.lower() in dictionary[number]:
						user_number = user_number.replace(symbol, str(number))
						break

		print(f"Number: {user_number}")
		new_number = input("Would you like to enter another number?(y/n) ")

if __name__ == "__main__":
	main()

