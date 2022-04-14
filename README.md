# pentest snips
Small tools to automate some attacks and scans

Use with xargs like this:
```
cat urls.txt | xargs -n1 -P10 python ~/snips/checkgitconfig.py | tee valid-git-urls.txt
```
