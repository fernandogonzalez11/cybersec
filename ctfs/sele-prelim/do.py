data = """arch           echo           link           nice           setpriv
ash            ed             linux32        nuke           setserial
base64         egrep          linux64        pidof          sh
busybox        false          ln             ping           sleep
cat            fatattr        login          ping6          stat
chattr         fdflush        ls             pipe_progress  stty
chgrp          fgrep          lsattr         printenv       su
chmod          fsync          lzop           ps             sync
chown          getopt         makemime       pwd            tar
conspy         grep           mkdir          reformime      touch
cp             gunzip         mknod          resume         true
cpio           gzip           mktemp         rev            umount
cttyhack       hostname       more           rm             uname
date           hush           mount          rmdir          usleep
dd             ionice         mountpoint     rpm            vi
df             iostat         mpstat         run-parts      watch
dmesg          ipcalc         mt             scriptreplay   zcat
dnsdomainname  kbd_mode       mv             sed
dumpkmap       kill           netstat        setarch"""

# Split and clean the list of commands
commands = data.split()

filt = []
for c in commands:
	if len(c) < 3: continue
	filt.append(c)

# Sorting by 3rd character first, then 2nd character
sorted_commands = sorted(filt, key=lambda x: (x[2],x[1]))

# Print the sorted list
for cmd in sorted_commands:
    print(cmd[0], end='')
