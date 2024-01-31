import csv

infile = open('employee_data.csv', 'r')

csv_file = csv.reader(infile)

next(csv_file)

for row in csv_file:
    print(f'Name: {row[1]}')
    print(f'Salary: {row[3]}')
    
    print(f'Bonus: ')

