# ChatRoom
import socket
HOST = "127.0.0.1" # IP LocalHost
PORT = 1966 # Port > 1024 (pas de droit) (sudo en dessous de 1024)

#attend une connexion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    connection.bind((HOST, PORT))
    connection.listen()
    conn, addr = connection.accept()
    with conn:
        print(f"Connected by {addr}")
        
        while True:
            data = conn.recv(1024)
            conn.sendall(b"Hello, world")
            if not data:
                break
            conn.sendall(data)


def message():
    pass

def multi_threading():
    pass

def identite():
    pass

def ui():
    pass


def main():
    pass