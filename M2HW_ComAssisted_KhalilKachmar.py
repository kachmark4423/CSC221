# program will test user on multiplication problems
# 1/22/2021
# CSC121 M2HW – Computer Assisted
# Khalil Kachmar

# Display "Choose a difficulty"
# Display "1) Level One"
#         "2) Level Two"
# Input difficulty
# If difficulty == 1:
    # Set int1 = Random(1, 9)
    # Set int2 = Random(1, 9)
# If difficulty == 2:
    # Set int1 = Random(1, 99)
    # Set int2 = Random(1, 99)
    
# Display "what is int1 times int2"
# Input guess
# Set product = int1 * int2
# If guess = product
#   Display Random(positive_message)
# Else:
#   Display Random(negative_message)

import random

def factor_generator(level):
    if level == '1':
        int1 = random.randint(1, 9)
        int2 = random.randint(1, 9)
    if level == '2':
        int1 = random.randint(1, 99)
        int2 = random.randint(1, 99)
    return (int1, int2)

def response_generator(key, correct=True):
    positive_responses = ('Very good!', 'Nice Work!', 'Keep up the good work!')
    negative_responses = ('No. Please try again', 'Wrong. Try once more',
                          'No, keep trying')
    if correct:
       return positive_responses[key - 1]
    else:
       return negative_responses[key - 1]
def check_answer(num1, num2, product):
    correct = False
    
    while not correct:
        guess = int(input(f"How much is {num1} times {num2}? "))
        key = random.randint(1, 3)
        
        if guess == product:
            response = response_generator(key)
            print(response)
            correct = True
        else:
            response = response_generator(key, False)
            print(response)
    main()
    
def menu():
    print("Choose a difficulty setting(1 or 2)\n")
    print("1. Level One\n2. Level Two")
    
    difficulty = input("Level: ")
    return difficulty
    

def main():
    num1, num2 = factor_generator(level)
    product = num1 * num2
    check_answer(num1, num2, product)
    
if __name__ == "__main__":
    level = menu()
    main()
