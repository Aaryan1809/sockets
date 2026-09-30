import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "avjo"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (SERVER , PORT)


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle(conn , addr):
    print(f"{addr} Connected")

    connection = True
    while connection:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connection = False

            print(f"[{addr}] : {msg}")
        
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handle , args=(conn, addr))
        thread.start()
        print(f"Active connections = {threading.active_count() - 1}")

print("Server is starting")
start()