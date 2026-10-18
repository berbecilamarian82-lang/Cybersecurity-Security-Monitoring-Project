import csv

failed_attempts = 0
failed_by_ip = {}
failed_by_username = {}

def get_risk_level(count):
    if count >= 5:
        return "High"
    elif count >= 3:
        return "Medium"
    else:
        return "Low"
    
def generate_alert(identifier, count, risk_level):
    if risk_level == "High":
        print(
            f"SECURITY ALERT - HIGH RISK: {identifier} has {count} failed login attempts."
        )
    elif risk_level == "Medium":
        print(
            f"SECURITY ALERT - MEDIUM RISK: {identifier} has {count} failed login attempts."
        )
def get_response_recommendation(risk_level):
    if risk_level == "High":
        return (
            "Investigate immediately, review the affected account and related logs, "
            "consider blocking the source IP address, reset credentials if compromise "
            "is suspected, and enable MFA if it is not already enabled."
        )
    elif risk_level == "Medium":
        return (
            "Investigate the source IP address or affected account and review "
            "additional authentication logs for related activity."
        )
    else:
        return "Continue monitoring the activity."

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
    risk_level = get_risk_level(count)
    generate_alert(ip_address, count, risk_level)
    recommendation = get_response_recommendation(risk_level)
    print("Recommended Response:", recommendation)
    print(ip_address, ":", count, "- Risk Level:", risk_level)

print("\nFailed login attempts by username:")

for username, count in failed_by_username.items():
    risk_level = get_risk_level(count)
    generate_alert(username, count, risk_level)
    recommendation = get_response_recommendation(risk_level)
    print("Recommended Response:", recommendation)
    print(username, ":", count, "- Risk Level:", risk_level)

print("\nTotal failed login attempts:", failed_attempts)

