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
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import ipdb as pdb

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")

# Create the socket 
# zmq.REQ means set the socket type to "request"
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

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
