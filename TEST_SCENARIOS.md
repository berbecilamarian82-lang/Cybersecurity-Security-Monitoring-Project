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

---

## Test 5 – Repeated Failed Attempts from the Same IP Address

**Input condition:**  
Multiple failed login attempts originate from the same IP address.

**Expected result:**  
The tool should group the failed attempts by source IP address and display the correct count.

---

## Test 6 – Repeated Failed Attempts Against the Same Username

**Input condition:**  
Multiple failed login attempts target the same username.

**Expected result:**  
The tool should group the failed attempts by username and display the correct count.

---

## Test 7 – Multiple Usernames Targeted from the Same IP Address

**Input condition:**  
The same source IP address attempts authentication against multiple usernames.

**Expected result:**  
The activity should be identified as suspicious and treated as High risk according to the project detection rules.

---

## Test 8 – Failed Attempts Followed by Successful Login

**Input condition:**  
Multiple failed login attempts are followed by a successful login for the same username and/or IP address.

**Expected result:**  
The activity should be treated as a High Priority Investigation because successful authentication may indicate compromised credentials.

---

## Test 9 – Total Failed Login Count

**Input condition:**  
Run the tool against the complete authentication dataset.

**Expected result:**  
The total number of failed authentication attempts should be:

**21**