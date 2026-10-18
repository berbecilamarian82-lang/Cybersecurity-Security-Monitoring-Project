# Test Scenarios

## Project
**Development of a Python-Based Security Monitoring Tool for Detecting Suspicious Authentication Activity**

## Purpose
The purpose of these test scenarios is to verify that the security monitoring tool correctly identifies failed authentication activity, applies the defined risk levels, generates security alerts, and provides appropriate response recommendations.

---

## Test 1 – Normal Successful Login

**Input condition:**  
A successful login with no failed attempts.

**Expected result:**  
No failed login alert should be generated.

**Expected risk level:**  
No risk classification required.

**Actual result:**  
Successful login records with no previous failed attempts did not generate a failed-login security alert.

**Status:**  
**Passed**

---

## Test 2 – Low Risk Activity

**Input condition:**  
1–2 failed login attempts from the same IP address or against the same username.

**Expected result:**  
The failed attempts should be counted and classified as Low risk.

**Expected alert:**  
No Medium or High security alert.

**Expected recommendation:**  
Continue monitoring the activity.

**Actual result:**  
The tool correctly classified two failed attempts from `192.168.1.12` and two failed attempts against the username `carol` as Low risk. No Medium or High security alert was generated. The tool recommended continuing to monitor the activity.

**Status:**  
**Passed**

---

## Test 3 – Medium Risk Activity

**Input condition:**  
3–4 failed login attempts from the same IP address or against the same username.

**Expected result:**  
The activity should be classified as Medium risk.

**Expected alert:**  
SECURITY ALERT - MEDIUM RISK

**Expected recommendation:**  
Investigate the source IP address or affected account and review additional authentication logs.

**Actual result:**  
The tool correctly identified three failed login attempts from `10.0.0.25` and against the username `david`. The activity was classified as Medium risk, a Medium security alert was generated, and the expected investigation recommendation was displayed.

**Status:**  
**Passed**

---

## Test 4 – High Risk Activity

**Input condition:**  
5 or more failed login attempts from the same IP address or against the same username.

**Expected result:**  
The activity should be classified as High risk.

**Expected alert:**  
SECURITY ALERT - HIGH RISK

**Expected recommendation:**  
Investigate immediately, review the affected account and related logs, consider blocking the source IP address, reset credentials if compromise is suspected, and enable MFA if it is not already enabled.

**Actual result:**  
The tool correctly classified multiple cases with five or more failed attempts as High risk. Examples included `185.22.44.10` with six failed attempts, `203.0.113.50` with five failed attempts, `198.51.100.23` with five failed attempts, `admin` with six failed attempts and `sarah` with five failed attempts. High-risk alerts and the expected response recommendations were displayed.

**Status:**  
**Passed**

---

## Test 5 – Repeated Failed Attempts from the Same IP Address

**Input condition:**  
Multiple failed login attempts originate from the same IP address.

**Expected result:**  
The tool should group the failed attempts by source IP address and display the correct count.

**Actual result:**  
The application successfully grouped failed authentication attempts by source IP address and displayed the correct counts:

- `192.168.1.12` – 2
- `10.0.0.25` – 3
- `185.22.44.10` – 6
- `203.0.113.50` – 5
- `198.51.100.23` – 5

**Status:**  
**Passed**

---

## Test 6 – Repeated Failed Attempts Against the Same Username

**Input condition:**  
Multiple failed login attempts target the same username.

**Expected result:**  
The tool should group the failed attempts by username and display the correct count.

**Actual result:**  
The application successfully grouped failed authentication attempts by username. Examples included:

- `carol` – 2
- `david` – 3
- `admin` – 6
- `sarah` – 5

The remaining usernames in the dataset each recorded one failed authentication attempt.

**Status:**  
**Passed**

---

## Test 7 – Multiple Usernames Targeted from the Same IP Address

**Input condition:**  
The same source IP address attempts authentication against multiple usernames.

**Expected result:**  
The activity should be identified as suspicious and treated as High risk according to the project detection rules.

**Actual result:**  
The tool detected that source IP address `203.0.113.50` targeted multiple usernames: `eve`, `frank`, `grace`, `henry` and `irene`. A High Risk security alert was generated.

**Status:**  
**Passed**

---

## Test 8 – Failed Attempts Followed by Successful Login

**Input condition:**  
Multiple failed login attempts are followed by a successful login for the same username and/or IP address.

**Expected result:**  
The activity should be treated as a High Priority Investigation because successful authentication may indicate compromised credentials.

**Actual result:**  
The tool detected that user `sarah` successfully logged in from `198.51.100.23` after five failed authentication attempts. The successful login occurred at `2026-10-15 10:22:30`, and the application generated a High Priority security alert.

**Status:**  
**Passed**

---

## Test 9 – Total Failed Login Count

**Input condition:**  
Run the tool against the complete authentication dataset.

**Expected result:**  
The total number of failed authentication attempts should be:

**21**

**Actual result:**  
The application reported:

**Total failed login attempts: 21**

**Status:**  
**Passed**

---

## Overall Testing Result

All nine planned test scenarios passed successfully.

The testing confirmed that the Python security monitoring tool can:

- read authentication log data;
- identify and count failed login attempts;
- group failed attempts by IP address and username;
- classify activity as Low, Medium or High risk;
- generate Medium and High security alerts;
- provide response recommendations;
- detect one IP address targeting multiple usernames;
- detect repeated failed login attempts followed by a successful login;
- calculate the correct total number of failed authentication attempts.

The test results demonstrate that the current version of the application meets the core functional requirements defined for the mini-project.