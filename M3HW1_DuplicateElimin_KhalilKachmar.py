# program will take a list of numbers and a list of strings as input and 
# display each list sorted with no duplicates. 
# 1/17/2021
# CSC-121 M3HW1 – Duplicate Elimination
# Khalil Kachmar

# Set num_list = []
# Set string_list = []
# Set more_nums = True
# Set more_strings = True
# Display "Enter a series of numbers. Enter 'q' when finished."
# Input items
# Display "Enter a series of strings. Enter 'q' when finished."
# Input items
# Set modified_list = []
# For item in num_list:
#   If item not in modified list:
#       Place item in modified list.
# Display modified_list
# For item in string_list:
#   If item not in modified list:
#       Place item in modified list.
# Display modified_list

def sort_list(unsorted_list, nums = False):
    modified_list = []
    for item in unsorted_list:
        if item not in modified_list:
            modified_list.append(item.lower())
    if nums:
        return sorted(modified_list, key=float)
    else: 
        return sorted(modified_list)

def main():
    num_list = []
    string_list = []
    more_nums = True
    more_strings = True
    
    print("Enter a series of numbers. Enter 'q' when finished")
    while more_nums:
        item = input("Enter next number: ")
        if item == 'q':
            more_nums = False
        else:
            num_list.append(item)
    modified_num_list = sort_list(num_list, True)

    print("Enter a series of strings. Enter 'q' when finished")
    while more_strings:
        
        item = input("Enter next string: ")
        if item == 'q':
            more_strings = False
        else:
            string_list.append(item)
    modified_string_list = sort_list(string_list)
    
    print(f"Modified number list: {modified_num_list}")
    print(f"Modified string list: {modified_string_list}")
if __name__ == "__main__":
    main()
