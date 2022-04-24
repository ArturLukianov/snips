import requests
import sys


users_api_url = sys.argv[1] + '/wp-json/wp/v2/users/'

resp = requests.get(users_api_url, verify=False, timeout=10, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'
})


if resp.status_code == 200:
    print(sys.argv[1], ','.join([user['slug'] for user in resp.json()]))
