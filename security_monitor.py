import csv

failed_attempts = 0
failed_by_ip = {}
failed_by_username = {}

with open("authentication_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["login_result"] == "Failed":
            failed_attempts += 1

            ip_address = row["ip_address"]
            username = row["username"]

            if ip_address in failed_by_ip:
                failed_by_ip[ip_address] += 1
            else:
                failed_by_ip[ip_address] = 1

            if username in failed_by_username:
                failed_by_username[username] += 1
            else:
                failed_by_username[username] = 1

print("Failed login attempts by IP address:")

for ip_address, count in failed_by_ip.items():
    print(ip_address, ":", count)

print("\nFailed login attempts by username:")

for username, count in failed_by_username.items():
    print(username, ":", count)

print("\nTotal failed login attempts:", failed_attempts)
