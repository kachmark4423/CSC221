# Program contains code from chapter 9 which writes/reads text and JSON files 
# 09/02/2021
# CSC221 M2T1 – Text File Processing
# Khalil Kachmar

def code_9_3_1():

  with open ('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')


def selfCheck_9_3_1():

  with open('grades.txt', mode='w') as grades:
    grades.write('1 Red A\n')
    grades.write('2 Green B\n')
    grades.write('3 White A\n')

def code_9_3_2():
  
  with open('accounts.txt', mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":<10}')
    for record in accounts:
      account, name, balance = record.split()
      print(f'{account:<10}{name:<10}{balance:<10}')

def selfCheck_9_3_2():
 
  with open('grades.txt', mode='r') as grades:
    print(f'{"ID":<4}{"Name":<7}{"Grade"}')
    for record in grades:
      student_id, name, grade = record.split()
      print(f'{student_id:<4}{name:<7}{grade}')

def code_9_4():
  import os

  accounts = open('accounts.txt', 'r')
  temp_file = open('temp_file.txt', 'w')

  with accounts, temp_file:
    for record in accounts:
      account, name, balance = record.split()
      if account != '300':
        temp_file.write(record)
      else:
        new_record = ' '.join([account, 'Williams', balance])
        temp_file.write(new_record + '\n')

  os.remove('accounts.txt')
  os.rename('temp_file.txt', 'accounts.txt')

def selfCheck_9_4():
  import os

  accounts = open('accounts.txt', 'r')
  temp_file = open('temp_file.txt', 'w')

  with accounts, temp_file:
    for record in accounts:
      account, name, balance = record.split()
      if name != 'Doe':
        temp_file.write(record)
      else:
        new_record = ' '.join([account, 'Smith', balance])
        temp_file.write(new_record + '\n')

  os.remove('accounts.txt')
  os.rename('temp_file.txt', 'accounts.txt')

def code_9_5():
  import json

  accouns_dict = {'accounts': [{'account':100, 'name':'Jones', 'balance':24.98},
                              {'account':200, 'name':'Doe', 'balance':345.67}]}

  with open('accounts.json', 'w') as accounts:
    json.dump(accouns_dict, accounts)

  with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)
    print(f'{accounts_json}\n')
    print(f"{accounts_json['accounts']}\n")
    print(f"{accounts_json['accounts'][0]}\n")
    print(f"{accounts_json['accounts'][1]}\n")
    print(json.dumps(accounts_json, indent=4))

def selfCheck_9_5():
  import json 

  grades_dict = {'gradebook': [{'student_id':1, 'name':'Red', 'grade':'A'},
                               {'student_id':2, 'name':'Green', 'grade':'B'},
                               {'student_id':3, 'name':'White', 'grade':'A'}]}

  with open('grades.json', 'w') as grades:
    json.dump(grades_dict, grades)

  with open('grades.json', 'r') as grades:
    print(json.dumps(json.load(grades), indent=4))

def main():
  code_9_3_1()
  selfCheck_9_3_1()
  print("Code 9.3.2:")
  code_9_3_2()
  print("\nSelf-Check 9.3.2:")
  selfCheck_9_3_2()
  code_9_4()
  selfCheck_9_4()
  print("\nCode 9.5:")
  code_9_5()
  print("\nSelf Check 9.5:")
  selfCheck_9_5()




if __name__ == '__main__':
  main()
