# Client side script
#author: poulomi chatterjee
from socket import *
server_name = 'localhost'
server_port = 5000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
  sentence = input("Enter your message(type 'q' to end session): ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2048)
  print ("Message from server: ", message.decode())
  if(sentence == 'q'):
    client_socket.close()
    print("End of connection")
