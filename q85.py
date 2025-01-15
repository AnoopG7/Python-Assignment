# Write a Python script to read a CSV file and print each row.
import csv
filename = input("Enter the CSV filename: ")
try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
