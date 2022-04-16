import sys
import requests


url = sys.argv[1]
resp = requests.get(url, verify=False, timeout=3)

if resp.status_code == 200 and 'Adminer' in resp.text:
    print(url)
