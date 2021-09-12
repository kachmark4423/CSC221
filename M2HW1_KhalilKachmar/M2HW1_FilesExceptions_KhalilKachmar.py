# Program will be menu driven with various options for reading information found
# in diamonds.csv file.
# M2H1-Files Exceptions
# Khalil Kachmar
# 09/04/2021

# SET df = DataFrame(diamonds.csv)
# DISPLAY "Menu"
          # "1. Display First Seven Rows"
          # "2. Display Last Seven Rows"
          # '3. Calculate Descriptive Statistics for "Carat"'
          # '4. Calculate Descriptive Statistics for "Cut", "Color" and "Clarity"'
          # '5. Display Unique Category Values for "Cut", "Color" and "Clarity"'
          # '6. Display Histogram of each Numerical Column'
          # '7. Exit Program'
          # Enter your choice: 
              
# INPUT choice
# IF choice NOT IN RANGE(1, 8):
    # DISPLAY "Not a valid entry"
# ELSE:
    # IF choice == 1:
        # DISPLAY df[:7]
    # ELSE IF choice == 2:
        # DISPLAY df[-7:]
    # ELSE IF choice == 3:
    #     DISPLAY df['carat'].describe()
    # ELSE IF choice == 4:
    #     DISPLAY df['cut', 'color' 'clarity'].desciribe()
    # ELSE IF choice == 5:
    #     DISPLAY df.cut.unique(), df.color.unique(), df.clarity.unique()
    # ELSE IF choie == 6 :
    #     DISPLAY df.hist()
    # ELSE:
    #     EXIT

      

import pandas as pd
import matplotlib.pyplot as plt

def display_first_seven(df):
    print(df[:7])
    
def display_last_seve(df):
    print(df[-7:])
    
def stats_for_carat(df):
    print(df.carat.describe())
    
def stats_for_cut_color_clarity(df):
    print(df.loc[:, ['cut', 'color', 'clarity']].describe())

def display_unique_values(df):
    cut_vals = [val for val in df.cut.unique()] + [ '-', '-', '-']
    color_vals = [val for val in df.color.unique()]+['-']
    clarity_vals = [val for val in df.clarity.unique()]
    
    unique_vals_dict = {'Cut':cut_vals, 'Color':color_vals, 'Clarity':clarity_vals}
    new_df = pd.DataFrame(unique_vals_dict)
    print(new_df)
    
def display_histogram(df):
    df.hist()
    plt.show()
    

def menu():
    print("\nMenu"
          "\n1. Display First Seven Rows"
          "\n2. Display Last Seven Rows"
          '\n3. Calculate Descriptive Statistics for "Carat"'
          '\n4. Calculate Descriptive Statistics for "Cut", "Color" and "Clarity"'
          '\n5. Display Unique Category Values for "Cut", "Color" and "Clarity"'
          '\n6. Display Histogram of each Numerical Column'
          '\n7. Exit Program')
    
    try:
        selection = int(input("Enter your choice: "))
    except ValueError:
        print("Not a valid entry. Please enter a proper value.\n")
    else:
        return selection

def main():
    
    df = pd.read_csv('diamonds.csv', index_col=0)

    show_menu = True
    while show_menu:
        choice = menu()
        if not str(choice).isdigit():
            pass
        elif choice not in range(1, 8):
            print("Not a valid entry. Please enter a proper value.\n")
        else:
            if choice == 1:
                display_first_seven(df)
            elif choice == 2:
                display_last_seve(df)
            elif choice == 3:
                stats_for_carat(df)
            elif choice == 4:
                stats_for_cut_color_clarity(df)
            elif choice == 5:
                display_unique_values(df)
            elif choice == 6:
                display_histogram(df)
            else:
                print("Goodbye")
                show_menu = False
    

if __name__ == "__main__":
    main()


    