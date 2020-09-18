# Half Duplex Chat using TCP/IP
A simple half-duplex application where client establishes a connection with the server to send and receive messages at the same time
# Methodology
1. The server takes care of 3 main functions during establishment of a connection <br />
  a) s.bind()- binds the address to the socket. address contains hostname and port number. <br />
  b) s.listen()- used to establish a TCP listener. <br />
  c) s.accept()- accepts another TCP connection and waits for connection to be established. <br />
2. The client's job is to initiate a TCP server connection. Connection is succesfull when there is a TCP listener active on the server application.
