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

def utilisateur_bienvenue(addr, conn) : 
    message_bienvenue = f"Bienvenue au nouvel arrivant : {addr}\n".encode()
    for u in utilisateur:
        if u != conn : 
            u.sendall(message_bienvenue) 

def message(conn, addr):
    conn.sendall(b"Hello, world\n")
    utilisateur_bienvenue(addr, conn)
    while True:
        data = conn.recv(1024)
        if not data:
            utilisateur.remove(conn)
            conn.close()
            break
        print(f"{addr} : {data}")
        utilisateur_message(data, conn)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    while True:
        conn, addr = server.accept()
        utilisateur.append(conn) 
        thread = threading.Thread(target=message, args=(conn, addr))
        thread.start()
