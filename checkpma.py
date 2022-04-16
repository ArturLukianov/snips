import requests
import sys

url = sys.argv[1]

pma_paths = [
    '/phpmyadmin/',
    '/pma/'
]

ok_url = None

for path in pma_paths:
    f_url = url + path
    response = requests.get(f_url, verify=False, timeout=5)
    if response.status_code == 200 and '<title>phpMyAdmin</title>' in response.text:
        ok_url = f_url
        break

if ok_url is None:
    exit(0)

print(ok_url)
