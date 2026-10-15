
import csv

failed_attempts = 0

with open("authentication_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["login_result"] == "Failed":
            failed_attempts += 1
            print(row)

print("\nTotal failed login attempts:", failed_attempts)
