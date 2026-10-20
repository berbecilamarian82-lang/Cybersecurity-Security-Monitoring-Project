import csv

failed_attempts = 0
failed_by_ip = {}
failed_by_username = {}
usernames_by_ip = {}
failed_history_by_user = {}
successful_logins = []


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

def generate_analysis_summary(
    failed_attempts,
    failed_by_ip,
    failed_by_username,
    usernames_by_ip,
    successful_logins
):
        print("\n==============================")
        print("SECURITY ANALYSIS SUMMARY")
        print("==============================")

        print(f"\nTotal failed login attempts: {failed_attempts}")

        if failed_by_ip:
            highest_risk_ip = max(failed_by_ip, key=failed_by_ip.get)
            highest_ip_count = failed_by_ip[highest_risk_ip]
            highest_ip_risk = get_risk_level(highest_ip_count)

            print("\nHighest-risk source IP:")
            print(
                f"{highest_risk_ip} - {highest_ip_count} failed attempts "
                f"- {highest_ip_risk} Risk"
            )

        if failed_by_username:
            highest_risk_username = max(
                failed_by_username,
                key=failed_by_username.get
            )
            highest_username_count = failed_by_username[highest_risk_username]
            highest_username_risk = get_risk_level(highest_username_count)

            print("\nHighest-risk username:")
            print(
                f"{highest_risk_username} - {highest_username_count} failed attempts "
                f"- {highest_username_risk} Risk"
            )

        suspicious_patterns = []

        for ip_address, usernames in usernames_by_ip.items():
            if len(usernames) > 1:
                suspicious_patterns.append(
                    f"{ip_address} targeted multiple usernames"
                )

        for event in successful_logins:
            suspicious_patterns.append(
                f"User {event['username']} successfully logged in after "
                f"{event['failed_attempts']} failed attempts"
            )

        print("\nSuspicious patterns detected:")

        if suspicious_patterns:
            for pattern in suspicious_patterns:
                print(f"- {pattern}")
        else:
            print("- No major suspicious patterns detected")

        high_risk_detected = any(
            count >= 5 for count in failed_by_ip.values()
        ) or any(
            count >= 5 for count in failed_by_username.values()
        )

        if successful_logins or high_risk_detected:
            print("\nOverall assessment:")
            print("High-risk authentication activity detected.")
            print("Immediate investigation is recommended.")
        elif any(count >= 3 for count in failed_by_ip.values()):
            print("\nOverall assessment:")
            print("Medium-risk authentication activity detected.")
            print("Further investigation is recommended.")
        else:
            print("\nOverall assessment:")
            print("Low-risk authentication activity detected.")
            print("Continue monitoring.")

with open("authentication_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip_address = row["ip_address"]
        username = row["username"]

        if row["login_result"] == "Failed":
            failed_attempts += 1

            if username not in failed_history_by_user:
                failed_history_by_user[username] = 0
            failed_history_by_user[username] += 1

            if ip_address not in usernames_by_ip:
                usernames_by_ip[ip_address] = set()
            usernames_by_ip[ip_address].add(username)

            if ip_address in failed_by_ip:
                failed_by_ip[ip_address] += 1
            else:
                failed_by_ip[ip_address] = 1

            if username in failed_by_username:
                failed_by_username[username] += 1
            else:
                failed_by_username[username] = 1

        elif row["login_result"] == "Success":
            if failed_history_by_user.get(username, 0) >= 3:
                successful_logins.append(
                    {
                        "username": username,
                        "ip_address": ip_address,
                        "failed_attempts": failed_history_by_user[username],
                        "timestamp": row["timestamp"],
                    }
                )
                failed_history_by_user[username] = 0




print("\nFailed attempts followed by a successful login:")

for event in successful_logins:
    print(
        f"SECURITY ALERT - HIGH PRIORITY: User {event['username']} "
        f"successfully logged in from {event['ip_address']} after "
        f"{event['failed_attempts']} failed attempts at {event['timestamp']}."
    )
print("\nMultiple usernames targeted from the same IP address:")   

for ip_address, usernames in usernames_by_ip.items():
    if len(usernames) > 1:
        print(
            f"SECURITY ALERT - HIGH RISK: {ip_address} targeted multiple usernames: "
            f"{', '.join(sorted(usernames))}"
        )

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

generate_analysis_summary(
    failed_attempts,
    failed_by_ip,
    failed_by_username,
    usernames_by_ip,
    successful_logins
)


