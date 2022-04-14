import requests
import sys

url = sys.argv[1] + '/wp-admin/'

res = requests.get(url, verify=False, timeout=5, allow_redirects=False)
if res.status_code == 302 and 'wp-login.php' in res.headers['Location']:
    print(url)
