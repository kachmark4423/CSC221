# Program will take numbers as input from user and display
# the two largest values 
# 1/22/2021
# CSC-121 M1HW2 – Nested Statements
# Khalil Kachnmar


# Set numbers = []
# Display "Please enter 10 separate numbers."
# Input num (x 10)
# Set top_two = []
# While length(top_two) < 2:
    # Set largest = numbers[0]
    # For number in numbers:
        # If number > largest:
            # Set largest = number
    # Place largest in top_two
    # Remove largest from numbers
# Display "Largest Number: top_two[0]"
# Display "Second Largest: top_two[1]"

numbers = []

print("Please enter 10 separate numbers.")

for i in range(1, 11):
    num = float(input(f"Number {i}: "))
    numbers.append(num)

top_two = []
while len(top_two) < 2:
    largest = numbers[0] 
    for number in numbers:
        if number > largest:
            largest = number
    top_two.append(largest)
    numbers.remove(largest)

print(f"\nLargest Number: {top_two[0]}")
print(f"Second Largest: {top_two[1]}")