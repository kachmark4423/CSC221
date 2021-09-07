# Program will create and manipulate data in a DataFrame
# 08/16/2021
# CSC221 M1HW2 – DataFrame
# Khalil Kachmar



#SET temperatures_dictionary = {'Maxine':[88.5, 99.2, 89.1], 'James':[87.9, 100, 89.7],
#                          'Amanda': [89, 99, 90]}
#SET temperatures = DataFrame(temperatures_dicionary)
#DISPLAY temperatures
#SET temperatures = DataFrame(temperatures_dictionary, indeces=['Morning', 
#                             'Afternoon', 'Evening'])
#DISPLAY temperatures
#DISPLAY temperatures.Maxine
#DISPLAY temperatures['Morning']
#DISPLAY temperatures['Morning', 'Evening']
#DISPLAY temperatures['Amanda', 'Maxine']
#DISPLAY temperatures[['Morning', 'Evening'], ['Amanda', 'Maxine']]
#DISPLAY temperatures.describe()
#DISPLAY temperatures.transpose()
#DISPLAY temperatures.sort(by=column name)


import pandas as pd

temperatures_dictionary = {'Maxine':[88.5, 99.2, 89.1], 'James':[87.9, 100, 89.7],
                           'Amanda': [89, 99, 90]}

# a)
temperatures = pd.DataFrame(temperatures_dictionary)
print("a) Temperatures DataFrame:\n\n",temperatures)

#b)
temperatures = pd.DataFrame(temperatures_dictionary, 
                            index=['Morning', 'Afternoon', 'Evening'])
print("\nb) DataFrame with custom indeces:\n\n", temperatures)

#c)
print(f'\nc) Temps for Maxine:\n\n{temperatures.Maxine}')

#d)
print(f'\nd) Morning Temperatures:\n\n{temperatures.loc["Morning"]}')

#e)
print(f'\ne) Morning/Evening Temperatures:\n\n'
      f'{temperatures.loc[["Morning", "Evening"]]}')

#f)
print('\nf) Temps for Amanda and Maxine:\n')
print(temperatures.loc[:, ['Amanda', 'Maxine']])

#g)
print('\ng) Morning and Afternoon temps for Amanda and Maxine:\n')
print(temperatures.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']])

#h)
print('\nh) Descriptive Statitsitcs:\n')
print(temperatures.describe())

#i)
print(f"\ni) DataFrame Transposed:\n\n{temperatures.T}")

#j)
print(f"\nj) Sorted by Column Name:\n\n{temperatures.sort_index(axis=1)}")
