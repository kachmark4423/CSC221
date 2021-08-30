#  Program will take input to create a schedule file and create a 
# schedule report
# 2/11/2021
# CSC121 M8Pro–Final 
# Khalil Kachmar

# Display MENU
#         1) Create Schedule File
#         2) Create Report File
#         3) Exit
#
#         "Enter your selection: "
# Input selection
# If selection == 1:
    # Display "Enter class name: "
    # Input name
    # Display "Enter class number:" 
    # Input number
    # Display "Enter meeting days: "
    # Input days
    # Display "Enter meeting times: "
    # Input times
    # Open schedule.txt
    # Write name
    # Write number
    # Write days
    # Write times
# If selection == 2:
    # Open schedule.txt
    # Read name, number, days, times
    # Open Report.txt
    # Write Class Name    Meeting Days    Meeting Times    
    # Write name+number   days            times
# If selection == 3:
    #Exit

def menu():
    print("MENU")
    print("1) Create Schecule File\n"
          "2) Create Report File\n"
          "3) Exit\n")
    
    try:
        selection = int(input("Please enter your selection: "))
        return selection
    except ValueError:
        return 0
    
    
    
def create_schedule_file():
    print("Enter your schedule information")
    classes = []
    more_classes = True
    while more_classes:
        class_name = input("Enter class name: ")
        class_number = input("Enter class number: ")
        meeting_days = input("Enter meeting days: ")
        meeting_time = input("Enter meeting time: ")
        class_info = (class_name, class_number, meeting_days, meeting_time)
        classes.append(class_info)
        
        another = input("Would you like to enter another class?(y/n): ")
        while another.lower() != 'n' and another.lower() != 'y':
            print("Please choose 'y' or 'n'.")
            another = input("Would you like to enter another class?(y/n): ")
        if another.lower() == 'y':
            continue
        else:
            more_classes = False
            
    schedule_file = open('schedule.txt', 'w')
    with schedule_file:
        for classInfo in classes:
            name, number, days, time = classInfo
            print(f"{name}\n{number}\n{days}\n{time}", file=schedule_file)
    
def create_report_file():
    report_file = open('report.txt', 'w')
    schedule_file = open('schedule.txt', 'r')
    with report_file, schedule_file:
        i = 0
        lines = schedule_file.readlines()
        report_file.write(f"{'Khalil Kachmar 2021 Spring Schedule':^42}\n")
        report_file.write(f"{'Class Name':<14}{'Meeting Days':<14}{'Meeting Times':<14}\n")
        for j in range(int(len(lines) / 4)):
            name, number, days, time = lines[i:i+4]
            full_class_name = name.strip()+number.strip()
            print(f"{full_class_name:<14}{days.rstrip():<14}{time.rstrip():<14}", file=report_file)
            i += 4
    
def main():
    show_menu = True
    while show_menu:
        try:
            selection = menu()
            if selection == 1:
                create_schedule_file()
            elif selection == 2:
              create_report_file()
            elif selection == 3:
                 print("Goodbye")
                 show_menu = False
            else:
                print("That is not a valid option\n")
        except FileNotFoundError:
            print("You must create a schedule file first\n")
        

if __name__ == "__main__":
    main()