import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 1968
utilisateur = []

def utilisateur_message(data, conn) : 
    for u in utilisateur :
        if u != conn :
            u.sendall(data)

def message(conn, addr):
    utilisateur.append(conn)
    conn.sendall(b"Hello, world\n")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"{addr} : {data}")
        utilisateur_message(data, conn)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=message, args=(conn, addr))
        thread.start()
