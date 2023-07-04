import csv

# Excel -
# CSV -
# name,age
# pramod,32
#
# XLSX - Lib

with open('TestData.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        for value in row:
            print(value,end=" ")
        print()

# The with statement is used to open the file, and it automatically handles the closing of the file, ensuring that resources are properly released
# when you're done reading the file.