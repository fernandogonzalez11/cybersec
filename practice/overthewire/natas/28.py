import requests
from requests.auth import HTTPBasicAuth
import urllib.parse

url = "http://natas28.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')
headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

text = "' OR 1=1 --"
query = f"query={text}"

res = requests.post(url, auth=auth, headers=headers, data=query)
res_url = urllib.parse.unquote(res.url)

enc = res_url.split('?query=')[1]

print(enc)
