
#include <zmq.hpp>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    zmq::context_t context (1);

    //  Socket to talk to server
    zmq::socket_t subscriber (context, ZMQ_SUB);
    subscriber.connect("tcp://localhost:5556");
    // subscriber.setsockopt(ZMQ_SUBSCRIBE);

    // Make a vector
    std::vector<float> vect_r;
    zmq::message_t message_r;

    while(true){
        subscriber.recv(&message_r);

        // Bytes in the message
        int bytes_r = message_r.size();
        // floats in the message
        int elements_r = bytes_r / sizeof(float);

        vect_r.resize(elements_r);
        memcpy(vect_r.data(), message_r.data(), bytes_r);

        // Print out the results
        for(int i = 0; i < elements_r; i++){
            printf("%0.1f\n", vect_r[i]);
        }

        // Print white space
        printf("\n\n\n");
    }
}    
    