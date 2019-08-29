#include <zmq.hpp>
#include <stdio.h>
#include <stdlib.h>
#include <chrono>
#include <thread>

int main(int argc, char * argv[])
{
    int elements_s = atoi(argv[1]);
    zmq::context_t context(1);
    zmq::socket_t publisher (context, ZMQ_PUB);
    publisher.bind("tcp://*:5558");

    // Initialize rng
    srandom((unsigned) time(NULL));

    // Instantiate and populate a vector of floats
    std::vector<float> vect_s(elements_s);
    std::vector<float> vect_r;
    
    for(int i = 0; i < elements_s; i++){
        vect_s.push_back ( (float)i );
    }

    // Calculate number of bytes in data
    int bytes_s = vect_s.size() * sizeof(float);
    printf("Send bytes: %d\n", bytes_s);

    // Create the zmq message object
    zmq::message_t message_s(bytes_s);

    int loopnum = 1;
    
    // Update the loop contents
    for(int i = 0; i < elements_s; i++){
        vect_s[i] = float(i) * float(loopnum);
    }

    // Copy the vector data into the message data
    memcpy(message_s.data(), vect_s.data(), bytes_s);

    // Send the message
    // publisher.send(message);

    // Get the size of the message in bytes
    int bytes_r = message_s.size();
    int elements_r = bytes_r / sizeof(float);

    // printf("Receive bytes: %d\n", bytes_r);
    // printf("Receive elements: %d\n", elements_r);

    return(0);
}

