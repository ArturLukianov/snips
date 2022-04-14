#!/bin/python

import requests
import sys

site = sys.argv[1]
u = site

t = requests.head(u, verify=False, timeout=3)
if t.status_code == 200:
    print(u)
