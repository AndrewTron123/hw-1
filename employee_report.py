import csv

infile = open('employee_data.csv', 'r')

csv_file = csv.reader(infile)

next(csv_file)
print("High Efficency Individuals")

for row in csv_file:

    efficent = int(row[5])/int(row[4])
    if efficent >= 2:
        print(row[1])
print()
infile.seek(0)
next(csv_file)
print("Low Efficency Individuals")
for row in csv_file:
    efficent = int(row[5])/int(row[4])
    if efficent < 2:
        print(row[1])

print()
infile.seek(0)
next(csv_file)

print("Employees in their 40's")
i = 0
for row in csv_file:
    age = int(row[2])
    
    if age >= 40:
        print(row[1])
        i += 1
print(f"The total number of employees in their 40's is {i}")

print()   
infile.seek(0)
next(csv_file)

print("Employees in their 30's")
i = 0
for row in csv_file:
    age = int(row[2])
    
    if age < 40 and age >= 30:
        print(row[1])
        i += 1
print(f"The total number of employees in their 30's is {i}")   

print()   
infile.seek(0)
next(csv_file)

print("Employees in their 20's")
i = 0
for row in csv_file:
    age = int(row[2])
    
    if age < 30 and age >= 20:
        print(row[1])
        i += 1
print(f"The total number of employees in their 20's is {i}")  