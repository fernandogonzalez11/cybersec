kali
========================

1. download virtualbox from the website
2. download distro from kali.org (7zip with a vbox and vdi)
3. add button in virtualbox, rather than create
4. create a NAT Network (file > tools > network manager)
5. all my machines have to be connected to this NAT (preferences > network > NAT Network)

menu folders in order of common cybersec workflow

sudo: superuser, do!

# navigating the fs
pwd: present working directory

`locate` command
* doesn't work right away, might need to run `updatedb` first

# users and privileges
`ls -la`
first line: 
* - (file), d (directory)
* rwx (read write execute)
* three groups: owner, members that own the file, other users

`chmod 777 hello.txt` full rwx across the board

`adduser john`

su: switch user

# common network commands
ifconfig
* ifconfig is getting deprecated for ip
* ip addresses: ip a
* arp table: ip n
* routing table: ip a

iwconfig for wireless connections

ping \<address>

ICMP traffic: another word for ping

arp -a: IP addresses that talk to the machine and the MAC associated with them, a way of associating IPs with MACs

netstat -ano: active connections running on the machine, you can see if a machine is talking to another

route: print routing table
* where your traffic exits

# viewing, creating and editing files
`echo "hello" > hello.txt`

`cat hello.txt`

`echo "hey again" >> hello.txt`: appends at the end

`touch newfile.txt`

# scripting with bash
`cat ip.txt | grep "64 bytes" | cut -d "  " -f 4 | tr -d ":"`
* cut returns portions of text
    * -d: split the text into portions according to the delimiter " "
    * -f 4: get the 4th portion of what was splitted
* translate (tr) also deletes characters
    * -d is option for delete

`for ip in $(cat ips.txt); do nmap $ip; done`

# sockets
connect two nodes together ~ connect to an open port in an IP

`nc -nvlp 7777` open port 7777 with netcat and make it listen on any interface