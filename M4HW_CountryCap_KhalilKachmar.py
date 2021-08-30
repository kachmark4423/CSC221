# Program will quiz user on country capitals
# 1/20/2021
# CTI-110 M4HW – Country Capitals
# Khalil Kachmar

# Set capitals
# Set number_correct = 0
# Set number_incorrect = 0
# Declare user_response
# While user_response != 'q':
    # test country = random(country) for country in capitals
    # Display "Enter 'q' to quit."
    # Display "Name the capital of test_country"
    # Input user_response
    # If user_response == capitals[test_country]:
        # Display "Congratulations, that is correct!"
        # number_correct + 1
    # ElseIf user_response == 'q':
        # Display "Goodbye"
                # "Results: Number Correct: number_correct
                #           Number Incorrect: number_incorrect"
    # Else:
        # Display "That is not correct."
        # number_incorrect + 1
    

import random

capitals = {'United States': 'Washington D.C.', 'Lebanon': 'Beirut', 
            'United Arab Emirates': 'Abu Dhabi', 'Afghanistan': 'Kabul',
            'Uganda': 'Kampala', 'United Kingdon': 'London', 'Spain': 'Madrid',
            'Nicaragua': 'Managua', 'Czech Republic': 'Prague', 
            'Latvia': 'Riga', 'El Salvador': 'San Salvador', 
            'South Korea': 'Seoul', 'Bulgaria': 'Sofia', 'Sweden': 'Stockholm',
            'Croatia': 'Zagreb', 'Laos': 'Vientiane', 'Austria': 'Vienna',
            'Philippines': 'Manila', 'Mexico': 'Mexico City', 
            'Cuba': 'Havana'}



def quiz():
    number_correct = 0
    number_incorrect = 0
    user_response = ''
    

    
    while user_response.lower() != 'q':
        countries = [country for country in capitals.keys()]
        test_country = random.choice(countries)
        print("Enter 'q' to quit.")
        user_response = input(f"Name the capital of {test_country}: ")
            
        if user_response.lower() == capitals[test_country].lower():
            print("Congratulations, that is correct!\n")
            number_correct += 1
        elif user_response.lower() == 'q':
            print("Goodbye\n")
        else:
            print("That is not correct.\n ")
            number_incorrect += 1
    
    return (number_correct, number_incorrect)

def main():
    
    num_correct, num_wrong = quiz()
    print("RESULTS:\n-----------------")
    print(f"Correct Answers: {num_correct}")
    print(f"Incorrect Answers: {num_wrong}")
    
if __name__ == "__main__":
    main()