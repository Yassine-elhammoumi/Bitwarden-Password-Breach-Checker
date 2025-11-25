import csv
import hashlib
import requests
import time

with open("banned_passwords.txt", "r") as f:
    banned = set(line.strip() for line in f)

with open("bitwarden_export.csv", "r", encoding="utf-8") as csv_file:
    reader = list(csv.DictReader(csv_file))
    total = len(reader)

    for i, row in enumerate(reader, start=1):
        pwd = row.get("login_password", "")
        if not pwd:
            continue

        if pwd in banned:
            print(f"[{i}/{total}] Skipped banned password")
            continue

        sha1 = hashlib.sha1(pwd.encode("utf-8")).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
        except Exception as e:
            print(f"[{i}/{total}] Error contacting HIBP:", e)
            continue

        found = False
        for line in r.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                print(f"[{i}/{total}] Breached password: '{pwd}' found {count} times")
                found = True
                break

        if not found:
            print(f"[{i}/{total}] Password checked, not breached")

        time.sleep(1.6)

