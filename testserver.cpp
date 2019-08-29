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
    publisher.bind("tcp://*:5556");

    // Instantiate and populate a vector of floats
    std::vector<float> vect_s;
    
    for(int i = 0; i < elements_s; i++){
        vect_s.push_back ( (float)i );
    }
   // Calculate number of bytes in data
    int bytes_s = vect_s.size() * sizeof(float);
     
    printf("Send elements: %d\n", (int) vect_s.size());
    printf("Send bytes: %d\n", bytes_s);

    int loopnum = 1;
    while(1)
    {
        
        for(int i = 0; i < elements_s; i++){
            vect_s[i] = (float) loopnum * (float)i;    
        }

        zmq::message_t message_s(bytes_s);
        memcpy(message_s.data(), vect_s.data(), bytes_s);

        // Send the message
        publisher.send(message_s);
        printf("Sent frame %d\n", loopnum);
        /*
        for(int i = 0; i < elements_s; i++)
        {
            printf("vect_send[%d] = %0.1f\n", i, vect_s[i]);
        }
        printf("\n\n\n");
        */ 
        loopnum++;
        // std::this_thread::sleep_for(std::chrono::seconds(1));

    }
    return(0);
}

