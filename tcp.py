import socket

host= "www.google.com"
port = 80

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# sock stream means that it is going to send a tcp connection
# AF_INET means that it is a ipv4 address that we are going to target

client.connect((host , port))

client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

rec = client.recv(4096)

# print(rec)
# This opens the file in write mode ('w')
with open('output.txt', 'w') as f:
    print(rec , file = f)
    
    
    