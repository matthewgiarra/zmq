
PROG_S=testserver
PROG_C=testclient
all:
	g++ -lzmq $(PROG_S).cpp -o $(PROG_S)
	g++ -lzmq $(PROG_C).cpp -o $(PROG_C)
