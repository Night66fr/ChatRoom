# ChatRoom
import socket
import logging
import threading
import time


HOST = "0.0.0.0" # IP 0.0.0.0 for ssh or 127.0.0.1 for localhost
PORT = 1966 # Port > 1024 (pas de droit) (sudo en dessous de 1024)
utilisateurs = []

def message(conn):
    conn.sendall(b"Hello, world\n")
    conn.sendall(b'You can chat right now or login using (LOG)\n')

def diffuser_message(data, expediteur_conn):
    """ Envoie le message à tout le monde sauf à celui qui l'a écrit """
    for u in utilisateurs:
        if u != expediteur_conn:
            u.sendall(data)

def thread_function(addr, conn):
    utilisateurs.append(conn)
    message(conn)
    welcome = f"User {addr} joined\n".encode()
    diffuser_message(welcome, conn)

    while True:
            data = conn.recv(1024)
            if not data:
                utilisateurs.remove(conn)
                conn.close()
                break
            print(f"{addr} : {data}")
            diffuser_message(data,conn)

#attend une connexion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind((HOST, PORT))
    connection.listen()
    
    while True:
        conn, addr = connection.accept()
        t = threading.Thread(target=thread_function, args=(addr, conn))
        t.start()
    
