
#include <zmq.hpp>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>

int main(int argc, char* argv[])
{
    zmq::context_t context (1);

    //  Socket to talk to server
    zmq::socket_t subscriber (context, ZMQ_SUB);
    printf("Subscribing to port...\n");
    subscriber.connect("tcp://localhost:5556");
    subscriber.setsockopt(ZMQ_SUBSCRIBE, "");
    printf("Subscribed!\n");

    // Make a vector
    std::vector<float> vect_r;
    zmq::message_t message_r;

    int loopnum = 0;

    while(true){
        // printf("Received frame %d\n", loopnum);
        loopnum++;
        subscriber.recv(&message_r);

        // Bytes in the message
        int bytes_r = message_r.size();
        // floats in the message
        int elements_r = bytes_r / sizeof(float);

        vect_r.resize(elements_r);
        memcpy(vect_r.data(), message_r.data(), bytes_r);

        // Print out the results
        printf("Received frame %d\n", loopnum);
        /*
        for(int i = 0; i < elements_r; i++){
            printf("vect_recv[%d] = %0.1f\n", i, vect_r[i]);
        }
        printf("\n\n\n");
        */
        
    }
}    
    