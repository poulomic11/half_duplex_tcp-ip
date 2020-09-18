from socket import *
server_port = 5000
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print ("Welcome: The server is now ready to receive")
connection_socket, address = server_socket.accept()
while True:
  sentence = connection_socket.recv(2048).decode()
  print("Message from client: ",sentence)
  message = input("Enter your message(type 'q' to end session): ")
  connection_socket.send(message.encode())
  if(message == 'q'):
    connection_socket.close()
    print("End of connection")