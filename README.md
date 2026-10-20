# Cybersecurity Security Monitoring Project

## Project Title
**Development of a Python-Based Security Monitoring Tool for Detecting Suspicious Authentication Activity**

## Project Overview
This project is a Python-based security monitoring tool designed to analyse authentication log data and identify suspicious login activity.

The tool was developed as part of my Professional Development module and supports my career goal of progressing towards a Cybersecurity Analyst or Junior SOC Analyst role.

The project demonstrates practical use of Python for security monitoring, authentication log analysis, risk classification, alert generation, security analysis and incident response recommendations.

---

## Project Aim
The aim of this project is to develop a Python-based monitoring tool that can analyse authentication logs, detect suspicious login activity, classify security risk and provide meaningful security analysis to support investigation.

---

## Key Features

The tool can:

- read authentication log data from a CSV file;
- detect failed login attempts;
- count total failed authentication attempts;
- group failed login activity by IP address;
- group failed login activity by username;
- classify authentication activity as Low, Medium or High risk;
- generate Medium and High Risk security alerts;
- provide security response recommendations;
- detect one source IP address targeting multiple usernames;
- detect repeated failed login attempts followed by a successful login;
- identify the highest-risk source IP address;
- identify the highest-risk username;
- identify suspicious authentication patterns;
- generate an overall Security Analysis Summary;
- recommend immediate investigation where high-risk activity is detected.

---

## Detection Rules

The project uses the following project-defined detection thresholds:

| Failed Login Attempts | Risk Level |
|---|---|
| 1–2 | Low |
| 3–4 | Medium |
| 5 or more | High |

Additional suspicious authentication patterns include:

### Multiple Usernames Targeted from the Same IP
If one source IP address generates failed authentication attempts against multiple usernames, the activity is treated as suspicious and classified as High Risk.

### Failed Attempts Followed by Successful Login
If multiple failed authentication attempts are followed by a successful login, the event is treated as a High Priority Investigation because the successful authentication may indicate compromised credentials.

> These thresholds were defined specifically for this project and are not intended to represent universal industry security standards.

---

## Security Response Recommendations

### Low Risk
- Continue monitoring the activity.

### Medium Risk
- Investigate the source IP address or affected account.
- Review additional authentication logs for related activity.

### High Risk
- Investigate immediately.
- Review the affected account and related logs.
- Consider blocking the source IP address.
- Reset credentials if compromise is suspected.
- Enable Multi-Factor Authentication if it is not already enabled.

---

## Security Analysis

In addition to detecting suspicious authentication events, the application generates an automated Security Analysis Summary.

The analysis identifies:

- total failed login attempts;
- highest-risk source IP address;
- highest-risk username;
- suspicious authentication patterns;
- overall security assessment;
- recommended investigation priority.

Example analysis output:

```text
SECURITY ANALYSIS SUMMARY

Total failed login attempts: 21

Highest-risk source IP:
185.22.44.10 - 6 failed attempts - High Risk

Highest-risk username:
admin - 6 failed attempts - High Risk

Suspicious patterns detected:
- 203.0.113.50 targeted multiple usernames
- User sarah successfully logged in after 5 failed attempts

Overall assessment:
High-risk authentication activity detected.
Immediate investigation is recommended.