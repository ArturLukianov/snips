import requests
import sys


url = sys.argv[1]

resp = requests.get(url, verify=False, timeout=5)
if resp.status_code != 404 and 'sql' in resp.text.lower():
    print(url)
