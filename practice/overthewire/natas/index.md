# natas: summary index

# 0
password hidden in HTML comment
CWE-256: Plaintext Storage of a Password
https://cwe.mitre.org/data/definitions/256.html

# 1
password hidden in HTML comment
right click blocked -> bypass with shift+right click

# 2
loads /files/pixel.png, but I can access /files and get /files/users.txt
CAPEC-126: Path Traversal
https://capec.mitre.org/data/definitions/126.html

# 3
Disallow: /s3cr3t/ in robots.txt
CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
https://cwe.mitre.org/data/definitions/200.html

# 4
website gives password if the request comes from another website (Referrer header)
so go to the desired page and put a link 
Referer-Based Access Control Flaw
