import csv


def read_csv_file(file_name):
    
       
    with open(file_name, newline='') as csvfile:
            
        csvreader = csv.reader(csvfile)

           
    for row in csvreader:
        print(', '.join(row))

 

file_name = input("Enter the CSV file name: ")

read_csv_file(file_name)
