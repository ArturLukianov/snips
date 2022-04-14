import sys
import os

with open(sys.argv[1]) as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()
    if url.strip() == '':
        continue
    clear_url = url.split('/.git/config')[0]
    fname = sys.argv[2] + '/' + url.split('://')[1].split('/')[0]
    os.system(f'git-dumper {clear_url} {fname}')
