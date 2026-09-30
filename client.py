import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "avjo"
PORT = 9999
SERVER = "10.117.89.43"
ADDR = (SERVER , PORT)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)