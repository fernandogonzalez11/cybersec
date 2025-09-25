passive recon
========================
# physical / social
## location information
* satellite images
* drone recon
* building layout (break areas, security, etc)

## job information
* employees: names, titles, phones, managers  
* pictures: badges, desks, computer photos, etc

# web / host
## target validation
we need to find out if the IP or whatever target they give us is in fact what we should be targetting

whois, nslookup, dnsrecon

## finding subdomains
google, nmap, etc

## fingerprinting
what kind of services are running on a web or host

## data breaches
most common way that we get into networks

breached incidents from the past that have had credentials dumped


# identifying our target
we're gonna be using bugcrowd.com > engagements > Tesla

## discovering e-mail addresses
hunter.io: me uní con mi correo educativo

phonebook.cz: created account on lrobles, pass on bitwarden

clearbit: has to be used in chrome

emailhippo: to verify e-mails
https://tools.emailhippo.com/

also https://email-checker.net/validate

## breached credentials

https://github.com/hmaverickadams/breach-parse is a bash script that searches through its own database of breached credentials, for a certain domain (db totals 24 gb)

https://dehashed.com is like ^ but much more powerful, however it's paid

https://hashes.org to (possibly) turn a hash into plaintext

# web enumeration
sublist3r package for gathering subdomains

https://crt.sh: certificate fingerprinting "%.tesla.com"

owasp amass combines both ^ but is more difficult to install and set up

tomnomnom/httprobe: you can give it a sublist3r-like list and it'll test the subdomains that actually work

# identifying website technologies
what is a website built with?

https://builtwith.com

wappalyzer

whatweb package

![qownnotes-media-ZpamPm](media/qownnotes-media-ZpamPm.png)
![qownnotes-media-ebXpuo](media/qownnotes-media-ebXpuo.png)

# gathering info with burpsuite
web proxy: has capability of intercepting traffic for us

first link burp to firefox with a manual proxy config

![qownnotes-media-kiegWH](media/qownnotes-media-kiegWH.png)
![qownnotes-media-SWDBWO](media/qownnotes-media-SWDBWO.png)

open https://burp ,  accept certificate risk, download cert by clicking on data certificate

then, go to firefox settings > privacy & security > view certificates > add that cert > check both boxes

![qownnotes-media-BpFvlL](media/qownnotes-media-BpFvlL.png)

# google fu

basically google dorks lol

# utilizing social media

linkedin > photos > they can have badges, desks, software!

twitter too