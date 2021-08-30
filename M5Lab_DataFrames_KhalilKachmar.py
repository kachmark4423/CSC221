# Program will request student names and grades and display data in a data frame
# 1/31/2021
# CSC121 M5Lab – DataFrame
# Khalil Kachmar


# Display "Enter number of tests: "
# Input number_of_tests
# Dipslay "Enter name of test {i}: " for i in Range(number_of_tests)
# Input test_name
# Display "Enter number of students: "
# Input number_of_students
# For i in range(number_of_students):
#	Dipslay "Enter name of student: "
#	Input student_name
#	Display "Enter student grades: "
#	Input grades
#	Set student_grades[student_name] = grades
# Set grades_DF = DataFrame(student_grades)
# Display grades_DF 

import pandas as pd

def main():
	number_of_tests = int(input("Enter the number of tests to be input: "))

	test_names = []
	for i in range(number_of_tests):
	        test_name = input(f"Enter name of test {i + 1}: ")
	        test_names.append(test_name)

	student_grades = {}
	number_of_students = int(input("Enter the number of students: "))
	for i in range(number_of_students):
	        student_name = input(f"Enter name for student {i + 1}: ")
	        grades = []

	        for test in test_names:
	                grade = float(input(f"Enter {test} grade for {student_name}: "))
	                grades.append(grade)

	        student_grades[student_name] = grades

	grades_DF = pd.DataFrame(student_grades, index=test_names)
	print("\nGrades:\n---------------------")
	print(grades_DF)

if __name__ == "__main__":
        main()
