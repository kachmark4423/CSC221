# A brief description of the project
# 1/19/2021
# CSC121 M4Lab – Dictionary Manipulations
# Khalil Kachmar

# Display Menu
#         ---------------
#         1) Create dictionary
#         2) Search for TLD
#         3) Add to dictionary
#         4) Update dictionary
#         5) Display dicionary content
#         6) Exit
# 
#         Enter your selection: 
# Input selection
# If selection == 1:
    # Declare user_dictionary
    # Set more = True
    # While more:
        # Display "Enter country name: "
        # Input country
        # Display "Enter TLD: "
        # Input tld
        # If country or tld == 'q':
            # more = False
        # Else:
            # Set user_dictionary[country] = tld
# ElseIf selection == 2:
    # Display "Enter country to search: "
    # Input country
    # Display user_dictionary[country]
# ElseIf selection == 3:
    # Display "Enter country name: "
    # Input country
    # Display "Enter TLD: "
    # Input tld
    # Set user_dictionary[country] = tld
# ElseIf selection ==  4:
    # Display "Enter country to update: "
    # Input country
    # Display "Enter TLD: "
    # Input tld
    # Set user_dictionary[country] = tld
# ElseIf selection == 5:
    # Display Country     TLD
             #----------------
             # country     tld
             # For country, tld in user_dictionary
# ElseIf selection == 6:
    # Exit
            

# Part 1:
    
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

#a
print('a)', 'Canada' in tlds.keys())
#b
print('b)','France' in tlds.keys())
#c
print(f"c)\n{'Country':<20}{'TLD'}")
print("-" * 25)
for key, value in tlds.items():
    print(f'{key:<20}{value}')
#d
tlds['Sweden'] = 'sw'
print(f"d) {tlds['Sweden']}")
#e
tlds['Sweden'] = 'se'
print(f"e) {tlds['Sweden']}")
#f
tlds_reversed = {value: key for key, value in tlds.items()}
print(f"f) {tlds_reversed}")
#g
tlds_reversed_upper = {key: value.upper() 
                       for key, value in tlds_reversed.items()}
print(f"g) {tlds_reversed_upper}")

# Part 2

def new_dictionary():
    user_tlds = {}
    more = True
    print("Enter 'q' any time to quit.")
    while more:
        key = input("Enter country name: ")
        if key.lower() == 'q':
            break
        value = input("Enter TLD: ")
        if value.lower() == 'q':
            break
        
        user_tlds[key.title()] = value.lower()
       
        
    return user_tlds
 

def search_for_tld(dictionary):
    country = input("Enter country name: ")
    tld = dictionary[country.title()]
    print(f"TLD for {country}: {tld}\n")
    

def add_to_dictionary(dictionary):
    country = input("Enter new country: ")
    tld = input("Enter country TLD: ")
    dictionary[country.title()] = tld.lower()
    
    return dictionary
    
    
def update_dictionary(dictionary):
    country = input("Enter country to update: ")
    tld = input("Enter new TLD: ")
    dictionary[country.title()] = tld.lower()
    
    return dictionary
   

def display_dictionary(dictionary):
    print(f"\n{'Country':<20}{'TLD'}")
    print("-" * 25)
    for key, value in dictionary.items():
        print(f'{key:<20}{value}')
    
    print()
  
        
def menu():
    print("MENU")
    print("-" * 28)
    print(f'1) Create dictionary\n'
          f'2) Search for TLD\n'
          f'3) Add to dictionary\n'
          f'4) Update dictionary\n'
          f'5) Display dicionary content\n'
          f'6) Exit')
    
    
    selection = int(input("Please make your selection: "))
    return int(selection)

        
def main():
    show_menu = True
    user_tld = {}
    while show_menu:
        selection = menu()
        if selection == 6:
            print("Goodbye")
            show_menu = False
        elif selection != 1 and len(user_tld) == 0:
            print("You must create a dictionary first.\n")
        elif selection == 1:
            user_tld = new_dictionary()
        elif selection == 2:
            search_for_tld(user_tld)
        elif selection == 3:
            user_tld = add_to_dictionary(user_tld)
        elif selection == 4:
            user_tld = update_dictionary(user_tld)
        elif selection ==  5:
            display_dictionary(user_tld)

        else:
            print("That is not a valid option.\n")
if __name__ == "__main__":
    main()