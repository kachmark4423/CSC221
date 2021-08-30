# The program will dipslay numbers, their square, and their cube in a table format. 
# 1\14\2021
# CSC121 M1HW1– Debugging
# Khalil Kachmar


#Display "Number    Square    Cube"
#for i in range(5):
#Display i    i**2    i**3


print('Number\tSquare\tCube')
for i in range(6):
	print(f"{i:>6}\t{i**2:>6}\t{i**3:>4}")


