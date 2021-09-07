# Program will be menu driven that allows user to enter a number and return the
# number doubled.
# 08-18-2021
# M1LAB1 - Python Review 
# Khalil Kachmar

#DECLARE List results
#DISPLAY "Please Enter A Number:"
#INPUT number
#DISPLAY number * 2
#APPEND number * 2 INTO results
#DISPLAY "MENU
        # -----------------------------------
        # 1) Enter another number
        # 2) Exit
        # 3) Display results"
        
        # "Enter your selection: "
#INPUT selection
#IF selection == 1:
    #DISPLAY "Enter A Number:"
#ELSE IF selection == 2:
    #EXIT
    #DISPLAY results
#ELSE IF selection == 3:
    #DISPLAY results
#ELSE DISPLAY "That is not a valid option"


results = []

def main():
   user_number = float(input("Please Enter A Number: "))
   double_number(user_number)
def double_number(number):
    print(f"\nYour number doubled is: {number * 2}")
    results.append(number*2)
    menu()
def menu():
    
    print("\nMENU\n" + "-"*35)
    print("1) Enter another number\n2) Exit\n3) Display results")
    
    choice = int(input("Please enter your selection: "))
    if choice == 1:
        main()
    elif choice == 2:
        print("Goodbye!")
        print(f"Results: {results}")
    elif choice == 3:
        print(f"\nPrevious results: {results}")
        menu()
    else:
        print("That is not a valid entry!\n")
        menu()
        
    
if __name__ == "__main__":
    main()