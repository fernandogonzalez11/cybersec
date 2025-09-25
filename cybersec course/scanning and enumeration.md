scanning and enumeration
========================
# installing kioptrix

beginner level vulnerable machine from vulnhub (site where people share broken machines to try hack them)

finding its IP: `sudo netdiscover 10.0.2.15/24`

vendor of VirtualBox seems to be PCS Systemtechnik GmbH

# scanning with nmap

network mapper: scan for open ports and services, will identify with something similar to the three-way handshake

`nmap -sS` (stealth scanning): used to be undetectable, now it is lol
* "stealthy" because it does SYN > SYN ACK > RST (rst: nevermind lol im not gonna connect)
* default option now

`nmap -T4 -p- <comma-sep list of ports> -A`
* T4: choice in speed (1 is slow, 5 is fast) slower is more thorough
* -p-: i want to scan all ports
    * no -p: scans top 1000 ports
* -A: tell me everything of a port: version info, os, fingerprinting, etc
    * combination of -sV (service/info scanning), -sC (script scanning), etc

![qownnotes-media-rAACkn](media/qownnotes-media-rAACkn.png)
![qownnotes-media-PEjWTd](media/qownnotes-media-PEjWTd.png)

# enumerating HTTP / HTTPS

![qownnotes-media-pcoMjc](media/qownnotes-media-pcoMjc.png)

## nikto
web vulnerability scanner

`nikto -h http://10.0.2.4`

![qownnotes-media-gXnbDg](media/qownnotes-media-gXnbDg.png)

## directory busting
dirbuster, dirb, gobuster: 3 dir busting programs

![qownnotes-media-vrMuMS](media/qownnotes-media-vrMuMS.png)

burpsuite repeater: you can send what you intercepted manually, and modify your request to see different responses

# enumerating SMB

smb: file share

metasploit (msfconsole), has a bunch of exploits, scanners, etc
* `search smb`
* 389 auxiliary/scanner/smb/smb_version
* `use auxiliary/scanner/smb/smb_version` or `use 389`
* `info` inside a module
* `options`
* `set RHOSTS 10.0.2.4`

![qownnotes-media-OsWwmF](media/qownnotes-media-OsWwmF.png)

`smbclient`: attempt to connect to the fileshare
* if we can connect with anonymous access, we can see files

`smbclient -L \\\\10.0.2.4\\`

![qownnotes-media-pMBUID](media/qownnotes-media-pMBUID.png)


then try to connect to a particular server without the -L

![qownnotes-media-vfusks](media/qownnotes-media-vfusks.png)

# enumerating SSH

![qownnotes-media-okGAKp](media/qownnotes-media-okGAKp.png)

![qownnotes-media-epJkdD](media/qownnotes-media-epJkdD.png)

sadly for me it didnt work but for keath it did

`ssh 10.0.2.4 -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa -oCiphers=+aes256-cbc` works by setting the cipher

# scanning with nessus

download nessus .deb > cd Downloads > sudo dpkg -i Nessus-yadayada.deb

email: f.gonzalez.1@estudiantec.cr  
activation code: APLT-DDQE-XFDJ-HW3J-GSH3  
user: tera  
pw: same as this machine

then go to https://kali:8834