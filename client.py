#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
##
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
from zmq import ssh
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import ipdb as pdb
import argparse
from getpass import getuser
import socket

# Get some defaults
default_username = getuser()
default_hostname = socket.gethostbyname(socket.gethostname())

# Instantiate the argument parser
parser = argparse.ArgumentParser()

# Add some arguments
parser.add_argument("--user", type=str,default=default_username, help="User name for ssh (default: %s)" % default_username)
parser.add_argument("--host", type=str, default=default_hostname, help = "host name for ssh (default: %s)" % default_hostname)
parser.add_argument("--socket", type=int, default = 5555, help = "socket number (default: 5555)")

# Parse the arguments
args = parser.parse_args()
username = args.user
hostname = str(args.host)
socket_num  = args.socket

# String for SSH to user name and host name
userhost = "%s@%s" % (username, hostname)
tcp_str = "tcp://localhost:%d" % socket_num

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")

# Create the socket 
# zmq.REQ means set the socket type to "request"
socket = context.socket(zmq.REQ)

# Tunnel connection
ssh.tunnel_connection(socket, tcp_str, userhost)
# socket.connect("tcp://localhost:5555")

while True:

    # Get some input
    classname = input("Class name: ").lower()
    
    # Request name
    request = classname.encode('ascii')

    # Send the request
    socket.send(request)
        
    # Receive a message
    message = socket.recv().decode('ascii')
    
    # Print the reply
    print("Received reply: %s" % message)
   
    # Load the image if it's there
    if not(message == ""):

        # Load and display the image
        if os.path.isfile(message):
            img = mpimg.imread(message)
            plt.imshow(img)
            plt.show()
