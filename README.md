# Bitwarden Password Breach Checker

This script checks passwords from a **Bitwarden CSV export** against known data breaches using the **Have I Been Pwned (HIBP) Pwned Passwords API**. It also cross-references a local list of banned passwords.

## Features

* Checks Bitwarden exported passwords for known breaches using HIBP.
* Uses **SHA-1 k-anonymity API**, so real passwords are never sent in full.
* Cross-checks against a local banned passwords list.
* Reports breached passwords with the number of occurrences.

## Requirements

* Python 3
* `requests` library

```bash
pip install requests
```

## Usage

1. Export your Bitwarden vault as a CSV (`bitwarden_export.csv`).
2. Create a `banned_passwords.txt` file with one banned password per line (One is available in this repo).
3. Run the script:

```bash
python check_passwords.py
```

Example output:

```
[1/120] Password checked, not breached
[2/120] Breached password: 'password123' found 45678 times
```

## Notes

* Respects HIBP rate limit (1 request per ~1.6s).
* The script prints breached passwords to the console; consider masking them in shared environments.
