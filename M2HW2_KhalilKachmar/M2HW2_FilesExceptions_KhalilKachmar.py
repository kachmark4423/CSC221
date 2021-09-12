# Program will be menu driven, read text file and display file stats.
# such as word count etc...
# 09/05/2021
# CSC221 M2HW – FileExceptions
# Khalil Kachmar

# SET speech = OPEN('state_of_union.txt')
# DISPLAY "  Menu
           # 1. Display Entire Speech
           # 2. Display Total Word Count
           # 3. Display Total Character Count
           # 4. Display Average Word Length
           # 5. Display Top Ten Longest Words
           # 6. Exit Program  "

           # Enter Your Choice: 

# INPUT choice
# IF choice == 1:
#     DISPLAY speech.READLINES
# ELSE IF choice == 2:
#     SET word_count = 0
#     FOR word in speech:
#         word_count += 1
#     DISPLAY word_count
# ELSE IF choice == 3:
#     SET char_count = 0
#     FOR word in speech:
#         FOR letter in word:
#             char_count += 1
#     DISPLAY char_count
# ELSE IF choice == 4:
#    SET word_lengths = []
#    FOR word in speech:
#        word_lengths.append(len(word))
#    DISPLAY avg(word_lengths)
# ELSE IF choice == 5:
#      words = []
#      lengths = []
#      FOR word in speech:
#        words.APPEND(word)
#        lenths.APPED(len(word))
#      word_lengths = SERIES(words, lengths)
#      word_lengths.ORDERBY(lengths)
#      DISPLAY word_length[0, 11]
# ELSE:
#     EXIT
    

import pandas as pd
import numpy as np
import math

def display_speech():
    with open('state_of_union.txt', 'r') as speech:
        x = speech.readlines()
        for line in x:
            print(line, end='')
        
def word_count():
    wordCount = 0
    with open('state_of_union.txt', 'r') as speech:
        for line in speech:
            new_line = line.replace('--', ' ')
            wordCount += len(new_line.split())
                
        print(f"Word Count: {wordCount}\n")
    
def char_count():
    charCount = 0
    char_count_no_spaces = 0
    
    with open('state_of_union.txt', 'r') as speech:
        for line in speech:
            for letter in line.strip():
                charCount += 1
                if letter != ' ':
                    char_count_no_spaces += 1
                
        print(f"Character Count With Spaces: {charCount}")
        print(f"Character Count Excluding Spaces: {char_count_no_spaces}\n")
    
def average_word_length():
    length_table = clean_words()
    print(f"Average Word Length: {math.ceil(length_table.mean())}\n")

def display_top_ten():
    length_table = clean_words()
    print(f"Ten Longest Words:\n{length_table.nlargest(10)}\n")

def clean_words():
    words = []
    lengths = []
    with open('state_of_union.txt', 'r') as speech:
        for line in speech:
            word_list = line.replace('.', '')
            word_list = word_list.replace(',', '')
            word_list = word_list.replace('?', '')
            word_list = word_list.replace('"', '')
            word_list = word_list.replace(';', '')
            word_list = word_list.replace('--', ' ').split()
            words += word_list
    
    unique_words = np.unique(words)
    for w in unique_words:
        lengths.append(len(w))
    
    length_table = pd.Series(lengths, index = unique_words)
    return length_table
   
def menu():
    print("Menu\n"
          "1. Display Entire Speech\n"
          "2. Display Total Word Count\n"
          "3. Display Total Character Count\n"
          "4. Display Average Word Length\n"
          "5. Display Top Ten Longest Words\n"
          "6. Exit Program\n")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("That is not a valid option\n")
    else:
        return choice
    
    
def main():
    show_menu = True
    while show_menu:
        choice = menu()
        if not str(choice).isdigit():
            pass
        elif choice not in range(1, 8):
            print("That is not a valid entry.\n")
        else:
            if choice == 1:
                display_speech()
            elif choice == 2:
                word_count()
            elif choice == 3:
                char_count()
            elif choice == 4:
                average_word_length()
            elif choice == 5:
                display_top_ten()
            else:
                print("Goodbye!")
                show_menu = False

if __name__ == "__main__":
    main()