# Program will return non-digit character, word, digit, and white space counts
# of user inputted sentence
# 1-31-2021
# CSC121 M6Lab – Reading String
# Khalil Kachmar

# Display "Enter message"
# Input message
# Display "MENU
        # 1) Number of Digits
        # 2) Number of Characters
        # 3) Number of White Space
        # 4) Number of Words
        # 5) Quit"
# Display "Enter your selection:"
# Input selection
# If selecion == 1:
    # Display "Number of digits: digit_count"
# Else If selection == 2:
    # Dipslay "Number of characters: character_count"
# Else If selection == 3:
    # Display "Number of white space: white_space_count"
# Else If selection == 4:
    # Display "Number of words: word_count"
# Else if selection == 5:
    # Display "Goodbye"
# Else:
    # Display "That is not a valid option"


import re

def menu():
    print("\nMENU")
    print(f"1) Number of Digits\n"
          f"2) Number of Characters\n"
          f"3) Number of White Space\n"
          f"4) Number of Words\n"
          f"5) Quit\n")
    selection = input("Make your selection(1-5): ")
    return selection

def digits(message):
    digits = re.findall('\d', message)
    print("\nNumber of digits:", len(digits))
    
def characters(message):
    non_digits = re.findall('\D', message)
    print("\nNumber of non-digit characters:", len(non_digits))

def white_space(message):
    white_space = re.findall('\s', message)
    print("\nNumber of white space characters:", len(white_space))
    
def words(message):
    words = message.split()
    print("\nNumber of words:", len(words))
    
def main():
    message = input("Input your string:\n")
    show_menu = True
    
    while show_menu:
        selection = menu()
        
        if selection == '1':
            digits(message)
        elif selection == '2':
            characters(message)
        elif selection == '3':
            white_space(message)
        elif selection == '4':
            words(message)
        elif selection == '5':
            print("Goodbye")
            show_menu = False
        else:
            print("\nThat is not a valid option.")
        
if __name__ == "__main__":
    main()
    






