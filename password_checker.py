import subprocess

'''This script is using for taking forgotten password'''

passwords = {}

data = str(subprocess.check_output(["netsh", "wlan", "show", "profiles"])).split('\\r\\n')
profiles = [i.split(":")[1][1:].strip() for i in data if "All User Profile" in i]

for i in profiles:
    try:
        results = str(subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])).split("\\r\\n")
        passwords[i] = [b.split(":")[1][1:] for b in results if "Key Content" in b]
    except:
        print("Error was raised")

print(*[f'{i} : {passwords.get(i)[0] if passwords.get(i) else " "}\n' for i in passwords])
