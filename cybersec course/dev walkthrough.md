dev walkthrough
========================

1. nmap scan: ssh in 22, 2 webservers (80 and 8080), nfs (its like samba) in 2049, extra linux shit
2. port 80 mentions a software named Bolt, port 8080 has php info website (leaks)
3. scanning port 80: /app that has server shit, particularly /config/config.yml which has a db user/pass (I_love_java)
4. scanning port 8080: /dev that has BoltWire interface, we can create a user and also I found credentials admin/I_love_java
5. `showmount -e 10.0.2.7` shows the nfs instance we can mount into
6. create /mnt/dev folder and `mount -t nfs 10.0.2.7:/srv/nfs /mnt/dev`, then cd into it
7. theres a save.zip, to unzip we need a password. crack it with  `fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt` (external package) (unzip rockyou with `gzip -d <file>`). password is java101
8. unzip and we'll have id_rsa and todo.txt with a mention of user "jp". try ssh with this user but it no worky :(
9. boltwire has [local file inclusion](https://www.exploit-db.com/exploits/48411) where we can see `/etc/passwd`. do that and realize there's a jeanpaul user (jp!!)
10. try ssh with jeanpaul and pass I_love_java -> works!
11. `history` -> cleared
12. `sudo -L` -> zip in NOPASSWD
13. with [gtfobins](https://gtfobins.github.io/) we can find privilege escalation with nopasswds! click Sudo > zip and copy commands in Sudo portion.
14. pwned!!!!