# Cybersecurity Security Monitoring Project

## Project Title

**Development of a Python-Based Security Monitoring Tool for Detecting Suspicious Authentication Activity**

## Project Overview

This project is being developed as part of the PFD200 Professional Development module.

The purpose of the project is to develop a Python-based security monitoring tool that analyses authentication log data and identifies suspicious login behaviour.

The application is designed to detect patterns such as repeated failed login attempts, activity associated with the same IP address or username, and other authentication behaviour that may require further investigation.

The project supports my professional development towards an entry-level cybersecurity role such as a Junior SOC Analyst or Cybersecurity Analyst.

## Project Aim

The main aim is to design and develop a Python application that can:

- read authentication log data from a CSV file;
- identify failed login attempts;
- group failed attempts by IP address;
- group failed attempts by username;
- classify suspicious activity by risk level;
- generate security alerts;
- provide response recommendations;
- support testing using different authentication scenarios.

## Detection Rules

The project uses predefined detection rules for learning and demonstration purposes.

| Failed Login Attempts | Risk Level |
|---|---|
| 1–2 | Low |
| 3–4 | Medium |
| 5 or more | High |

Additional suspicious patterns will include:

- the same IP address targeting multiple usernames;
- repeated failed attempts followed by a successful login.

These thresholds are project-defined and are not presented as universal industry standards.

For the complete detection rules, see:

[DETECTION_RULES.md](DETECTION_RULES.md)

## Current Project Progress

Completed:

- Authentication CSV dataset created
- Detection rules defined
- Python CSV reader implemented
- Failed login attempts detected and counted
- Failed attempts grouped by IP address
- Failed attempts grouped by username

Currently in development:

- Low / Medium / High risk classification

Planned:

- Security alert generation
- Response recommendations
- Testing scenarios
- Expected vs actual result testing
- Final documentation and portfolio evidence

## Technologies Used

- **Python 3** – application development
- **CSV** – authentication log dataset
- **Visual Studio Code** – coding and testing
- **Git** – version control
- **GitHub** – repository and project documentation
- **GitHub Projects** – Kanban-style project management

## Repository Structure

```text
Cybersecurity-Security-Monitoring-Project/
│
├── authentication_logs.csv
├── DETECTION_RULES.md
├── PROJECT_PROPOSAL.md
├── SELF_ASSESSMENT.md
├── security_monitor.py
└── README.md 