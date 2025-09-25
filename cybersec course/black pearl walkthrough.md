black pearl walkthrough
========================

1. nmap shows ports 22 (ssh), 53 (dns), 80 (http)
2. scanning port 80 we find `secret` file -> dead end
3. however in the main page we find alek@blackpearl.tcm as webmaster (clue)
4. if we recon the dns with `dnsrecon -r 127.0.0.0/24 -n 10.0.2.8 -d randomdomain`, we find `PTR blackpearl.tcm 127.0.0.1`
5. so, we can add in /etc/hosts a pointer as `10.0.2.8 blackpearl.tcm` which will allow us to see this domain
6. in http://blackpearl.tcm we find a php info dump. scanning this website we find `navigate` directory
7. go there and it's navigate cms v2.8. turns out there's an [exploit](https://www.rapid7.com/db/modules/exploit/multi/http/navigate_cms_rce/) of unauthed RCE
8. load it with metasploit (i set rhosts as blackpearl.tcm, but keath set rhosts to 10.0.2.8 and vhost to blackpearl.tcm, both work)
9. we pop a meterpreter shell as www-data! type `shell` to get the linux shell. you can turn it into a tty with [this](https://wiki.zacheller.dev/pentest/privilege-escalation/spawning-a-tty-shell) if the machine has python
10. open transfer folder's webserver and wget linpeas.sh in the target 
11. chmod and run it -> there are files that say "Unknown SUID binary"
  * basically what this means is that it's a binary that runs in the root environment even when we call it as a normal user
12. `find / -type f -perm -4000 2>/dev/null` lets us print easily which binaries have this property
13. gtfobins has a suid category for privilege escalation, turns out php7.3 (which was on that list) has potential for escalation
14. run the command from the suid portion, and we'll get a root shell!
