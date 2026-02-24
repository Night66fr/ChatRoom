# ChatRoom
import socket
import logging
import threading
import time


HOST = "127.0.0.1" # IP LocalHost
PORT = 1966 # Port > 1024 (pas de droit) (sudo en dessous de 1024)

def message(conn):
    conn.sendall(b"Hello, world\n")
    conn.sendall(b'You can chat right now or login using (LOG)\n')

def thread_function(name, conn):
    message(conn)
    while True:
            data = conn.recv(1024)
            print(f'{data}')
            if not data:
                conn.close()
                break

#attend une connexion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind((HOST, PORT))
    connection.listen()
    
    while True:
        conn, addr = connection.accept()
        t = threading.Thread(target=thread_function, args=(addr, conn))
        t.start()
    
