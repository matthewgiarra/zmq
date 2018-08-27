# Server inter-process communication in Python

import time
import zmq
from urllib.request import urlretrieve
import argparse
import ipdb as pdb

# Instantiate an argument parser
parser = argparse.ArgumentParser()

# Add some arguments
parser.add_argument("--socket", type=int, default = 5555, help = "socket number (default: 5555)")

# Parse the arguments
args = parser.parse_args()
socket_num = args.socket

# Instantiate the context
context = zmq.Context()

# Define the socket type
socket = context.socket(zmq.REP)

# Bind to the socket
socket.bind("tcp://*:%d" % socket_num)

# Define some URLs for testing.
cat_url="http://media.boingboing.net/wp-content/uploads/2017/03/surprised-cat-04.jpg"
dog_url="https://www.lukor.net/wp-content/uploads/2017/07/surprised-looking-dog_1600.jpg"

keepalive = True

while keepalive is True:
    
    #  Wait for next request from client
    message = socket.recv().decode('ascii').lower()
    print("Received request: %s" % message)
    
    if message.lower() == 'cat':
        url = cat_url
    elif message.lower() == 'dog':
       url = dog_url
    elif message.lower() == 'exit':
        keepalive = False
        url=''      
    else:
        url = ''
        outpath = ''
    
    # Make the output file name   
    outpath = message.lower() + ".jpg"
        
    if not (url == ""):    
        print("%s requested. Downloading %s..." % (message.lower(), message.lower()))
        urlretrieve(url,outpath)
        socket.send(outpath.encode('ascii'))      
    else:
       print("Got request for non-catalog item. Not doing anything.")
       socket.send(b"")
    