# Project Proposal

## Project Title
**Development of a Python-Based Security Monitoring Tool for Detecting Suspicious Authentication Activity**

## 1. Introduction

This mini-project will focus on developing a simple cybersecurity monitoring tool using Python. The purpose of the project is to analyse authentication log data and identify suspicious login behaviour that may indicate a security threat, such as a brute-force attack.

Authentication logs can contain useful information including usernames, IP addresses, timestamps, and whether a login attempt was successful or unsuccessful. By analysing these records, it is possible to identify patterns that may require further investigation.

## 2. Project Aim

The aim of this project is to design and develop a Python-based security monitoring tool that can analyse authentication logs, detect repeated failed login attempts, identify suspicious activity, classify the level of risk, and produce a simple security alert.

## 3. Project Objectives

The objectives of the project are:

1. To understand how authentication logs can be used in cybersecurity monitoring.
2. To create a sample dataset containing successful and failed login attempts.
3. To develop a Python program that reads and analyses authentication log data.
4. To detect repeated failed login attempts linked to the same username or IP address.
5. To classify suspicious activity using basic risk levels such as Low, Medium, and High.
6. To generate a security alert when suspicious authentication activity is detected.
7. To provide simple response recommendations for identified security events.
8. To test and document the tool using different login scenarios.
9. To present the completed project professionally using GitHub.

## 4. Justification

I selected this project because my self-assessment identified a gap between my current theoretical knowledge of cybersecurity and my practical experience of security monitoring and log analysis.

I currently have a basic understanding of cybersecurity concepts, networking, IP addresses, Python programming, and common threats such as brute-force attacks. However, I have limited practical experience using Python to analyse security data, identify suspicious behaviour, and support basic incident response.

This project will allow me to apply my existing knowledge in a practical context while developing new technical skills. It is also relevant to my future career goal of progressing towards an entry-level cybersecurity role such as Junior SOC Analyst or Cybersecurity Analyst. These roles commonly involve monitoring alerts, analysing logs, identifying suspicious authentication activity, assessing risk, documenting findings, and escalating incidents where necessary.

## 5. Project Development

The project will use a sample CSV file containing authentication records. Each record will include information such as:

- timestamp;
- username;
- IP address;
- login result.

The Python application will read the data and analyse failed login attempts. A simple detection rule will be used to identify suspicious patterns.

For example:

- 1–2 failed login attempts: Low risk
- 3–4 failed login attempts: Medium risk
- 5 or more failed login attempts: High risk

Where repeated failed login attempts are detected from the same IP address or against the same account, the program will generate a warning indicating possible suspicious authentication activity.

The system will also display simple response recommendations, such as investigating the source IP address, checking the affected account, reviewing additional logs, resetting credentials where appropriate, or enabling multi-factor authentication.

## 6. Tools and Technologies

The project will use:

- **Python 3** — application development
- **Visual Studio Code** — coding and testing
- **CSV** — sample authentication log data
- **Git** — version control
- **GitHub** — project repository and professional portfolio

## 7. Testing

The project will be tested using several scenarios, including:

- normal successful login activity;
- one or two failed login attempts;
- multiple failed login attempts;
- five or more failed login attempts;
- repeated failed attempts from the same IP address;
- failed attempts followed by a successful login.

The expected result of each test will be compared with the actual output of the program.

## 8. Expected Outcome

The expected outcome is a working Python-based security monitoring tool that can read authentication log data, detect repeated failed login attempts, classify suspicious activity by risk level, and generate a basic security alert.

The project is expected to improve my practical skills in Python, log analysis, threat detection, risk assessment, testing, technical documentation, Git, GitHub, and basic incident response. These skills will support my professional development and preparation for an entry-level cybersecurity career.
