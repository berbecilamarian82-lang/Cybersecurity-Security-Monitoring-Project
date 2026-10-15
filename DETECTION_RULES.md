# Detection Rules

## Project
**Development of a Python-Based Security Monitoring Tool for Detecting Suspicious Authentication Activity**

## Purpose
These detection rules define how the project will identify suspicious authentication activity in the sample log dataset.

The thresholds below are project-defined rules for this mini-project. They are not presented as universal industry standards.

## Detection Rules

### Rule R1 — Low Risk
**Condition:** 1–2 failed login attempts from the same IP address or against the same username.

**Risk Level:** Low

**Recommended Response:**
- Continue monitoring the activity.
- Review the account or source IP if the activity continues.

---

### Rule R2 — Medium Risk
**Condition:** 3–4 failed login attempts from the same IP address or against the same username.

**Risk Level:** Medium

**Recommended Response:**
- Investigate the source IP address.
- Review the affected account.
- Check additional authentication logs for related activity.

---

### Rule R3 — High Risk
**Condition:** 5 or more failed login attempts from the same IP address or against the same username.

**Risk Level:** High

**Recommended Response:**
- Investigate the activity immediately.
- Review the affected account and related logs.
- Consider blocking the source IP address where appropriate.
- Reset credentials if account compromise is suspected.
- Enable multi-factor authentication if it is not already enabled.

---

### Rule R4 — Multiple Usernames Targeted
**Condition:** The same IP address generates failed login attempts against multiple different usernames.

**Risk Level:** High

**Reason:** This pattern may indicate password spraying or broad credential-guessing activity.

**Recommended Response:**
- Investigate the source IP address.
- Identify all accounts targeted.
- Review related authentication events.
- Consider blocking the IP address where appropriate.

---

### Rule R5 — Failed Attempts Followed by a Successful Login
**Condition:** Multiple failed login attempts are followed by a successful login for the same username and/or source IP address.

**Risk Level:** High Priority Investigation

**Reason:** The pattern may indicate that an attacker eventually obtained valid credentials.

**Recommended Response:**
- Investigate the successful login immediately.
- Review the affected account.
- Check the source IP address and related log activity.
- Consider resetting credentials.
- Review or enable multi-factor authentication.
- Escalate for further investigation if compromise is suspected.

## Summary

| Rule | Condition | Risk Level |
|---|---|---|
| R1 | 1–2 failed attempts | Low |
| R2 | 3–4 failed attempts | Medium |
| R3 | 5+ failed attempts | High |
| R4 | Same IP targets multiple usernames | High |
| R5 | Multiple failures followed by success | High Priority Investigation |
