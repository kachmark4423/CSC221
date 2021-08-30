# Program will take a file with student names and id numbers and create a report that lists 
# name, id numbers, username, and email. 
# 2/6/2021
# CSC121 M7Lab - Files
# Khalil Kachmar

# Set studentinfo = studentinfo.txt
# Set logininfo = logininfo.txt
# With studentinfo:
    # Set last_name = Last Name, first_name = First Name, id_num = 
# Set user_id = last_name + firt_name[0] + id_num[4:7]
# Set email = user_id@student.faytechcc.edu
# With logininfo:
    # Write: Student Login Information
    #     Last         First       ID         User ID
    #   last_name   first_name    id_numb   user_id  for student in studentinfo

studentinfo = open("studentinfo.txt", 'r')
logininfo = open('logininfo.txt', 'w')

with studentinfo, logininfo:
	logininfo.write(f'{"Student Login Information":^72}\n')
	logininfo.write(f'{"Last":<10}{"First":<10}{"Id Num":<10}{"Login Id":<16}{"Email"}\n')
	for student in studentinfo:
		last_name, first_name, id_number = student.split()
		user_id = last_name.lower() + first_name[0].lower() + id_number[-4:]
		email = f'{user_id}@student.faytechcc.edu'
		print(f'{last_name:<10}{first_name:<10}{id_number:<10}{user_id:<16}{email}', file=logininfo)
