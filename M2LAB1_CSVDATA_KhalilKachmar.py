# Program will read a CSV file and display different data
# CSC221 - CSV DATA
# Khalil Kachmar
# 09-09-2021

import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')

pd.set_option('precision', 2)

print("Head:\n")
print(titanic.head())

print("\nTail:\n")
print(titanic.tail())

titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

print("\nHead with new column names:\n")
print(titanic.head())

print("\nTitanic.Describe:\n")
print(titanic.describe())

print("\nSurvived == 'yes'.Describe:\n")
print((titanic.survived == 'yes').describe())

histogram = titanic.hist()

print("\nHistogram:\n")
plt.show()