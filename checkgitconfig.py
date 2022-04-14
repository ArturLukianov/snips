import sys
import requests

text = requests.get(sys.argv[1], verify=False, timeout=5).text

if '[core]' in text:
    print(sys.argv[1])
