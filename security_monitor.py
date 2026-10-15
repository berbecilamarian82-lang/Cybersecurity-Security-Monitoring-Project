import csv

failed_attempts = 0
failed_by_ip = {}

with open("authentication_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["login_result"] == "Failed":
            failed_attempts += 1

            ip_address = row["ip_address"]

            if ip_address in failed_by_ip:
                failed_by_ip[ip_address] += 1
            else:
                failed_by_ip[ip_address] = 1

print("Failed login attempts by IP address:")

for ip_address, count in failed_by_ip.items():
    print(ip_address, ":", count)

print("\nTotal failed login attempts:", failed_attempts)
