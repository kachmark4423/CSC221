# program will ask user to imput 10 numbers, display min, max, total, 
# and average. ask user to imput one more number and display all numbers in 
# list larger than that number. 
# 1/16/2021
# CSC-121 M3Lab – Lists
# Khalil Kachmar

#Display "Enter 10 separate numbers"
#Declare num
#Input numbers (x10)
#Display "Minimum: min(numbers)"
#Display "Maximum: max(numbers)"
#Display "Total: sum(numbers)"
#Display "Average: mean(numbers)"
#Display "Enter any number:"
#Declare reference_num = Input
#Input number
#For number in numbers:
#   Display number if number > reference_num



import statistics as stats

def list_description(numbers):
    print(f"\nMinimum: {min(numbers)}\n"
          f"Maximum: {max(numbers)}\n"
          f"Total: {sum(numbers)}\n"
          f"Average: {stats.mean(numbers)}")
    
def greater_than(numbers, value):
    print(f"NUMBERS GREATER THAN {value} IN YOUR LIST:\n")
    for number in numbers:
        if number > value:
            print(number, end=" ")
def main():
    num_list = []
    print("PLEASE ENTER 10 SEPARATE NUMBERS.")
    
    for i in range(1, 11):
        num = float(input(f"Number {i}: "))
        num_list.append(num)
    list_description(num_list)
    
    reference_num = float(input("ENTER ANY NUMBER: "))
    
    greater_than(num_list, reference_num)

if __name__ == "__main__":
    main()