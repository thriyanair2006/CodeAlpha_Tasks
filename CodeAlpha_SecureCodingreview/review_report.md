# Secure Coding Review Report

## Application Reviewed

Python Login System

## Vulnerabilities Found

### 1. Plain Text Password Storage

Passwords were stored directly in source code.

Risk:
Attackers can steal passwords.

Fix:
Use password hashing.

---

### 2. Sensitive Data Exposure

The program displayed user credentials.

Risk:
Attackers can view usernames and passwords.

Fix:
Remove sensitive information from output.

---

## Security Improvements

- SHA256 password hashing
- Sensitive data removed
- Improved authentication

## Conclusion

The vulnerable application contained security flaws.
The secure version follows better coding practices.