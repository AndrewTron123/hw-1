import csv
infile = open('customers.csv','r')
outfile = open('customer_country.csv', 'w')

in_csv = csv.reader(infile)
next(in_csv)
outfile.write(f'{"Full Name: "}, {"Country"}\n')
clients_no = 0
for row in in_csv:
    outfile.write(f'{row[1]} {row[2]}, {row[4]}\n')
    clients_no += 1
outfile.close()
print(f'Total Number of Customers: {clients_no}')
