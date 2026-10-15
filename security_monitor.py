
import csv

with open("authentication_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)