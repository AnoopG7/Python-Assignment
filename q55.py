# Write a script that reads a CSV file and prints each row. (Assume the file exists and is properly formatted.)
import csv
filename = input("Enter the CSV filename: ")

try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
