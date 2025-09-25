
academy walkthrough
========================
1. nmap scan: ftp (with anon login), apache http, ssh
2. scan directories (dirbuster or a ffuf)
    * ffuf has the advantage that it only does depth-1 searching so it'll be quicker
3. find /academy/ login portal and /phpmyadmin/
4. login to ftp server (user/pass is anonymous)
5. get note.txt, realize it has a hashed password
6. hash-identifier command to show it's md5
7. hashcat to dehash that bitch (preferrable to do in main as it uses gpu power but i dont even have gpu anyway xDDD)
8. login with student account
9. in profile, you can upload a pfp but really it can be any file
10. search php reverse shell and put it into a file
11. open port with netcat
12. update with that file and it'll auto execute it lol
13. now we have shell of user www-data or some shit
14. set up a python webserver: `python -m http.server 80` in a `transfer` folder
15. download linpeas.sh to make a vuln search, add it to the transfer folder
16. wget the file from the attacker's ip
17. run and find out mysql password, along with a backup.sh in gremmie user
18. ssh into gremmie@ip from the attacker; somehow that mysql pass is also the gremmie login pass
19. download pspy 64 bits and also add to transfer folder (this can check crontabs without root)
20. wget pspy into gremmie /tmp/, chmod it and run
21. realize backup.sh is getting cronned every minute!!!
22. search "bash reverse shell oneliner", get that line, modify to a proper ip and port
23. open port with netcat
23. modify backup.sh to have that, and save file
24. once it runs, we have access to root! /root/ has flag.txt
