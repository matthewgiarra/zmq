#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
from urllib.request import urlretrieve

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

cat_url="http://media.boingboing.net/wp-content/uploads/2017/03/surprised-cat-04.jpg"
dog_url="https://www.lukor.net/wp-content/uploads/2017/07/surprised-looking-dog_1600.jpg"

while True:
    #  Wait for next request from client
    message = socket.recv().decode('ascii').lower()
    print("Received request: %s" % message)
    
    if message.lower() == 'cat':
        url = cat_url
    elif message.lower() == 'dog':
       url = dog_url
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
    