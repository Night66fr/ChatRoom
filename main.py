# ChatRoom
import socket
HOST = "127.0.0.1" # IP LocalHost
PORT = 1967 # Port > 1024 (pas de droit sudo en dessous de 1024)

def message():
    conn.sendall(b"Hello, world\n")
    conn.sendall(b'You can chat right now or login using (LOG)\n')

#attend une connexion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind((HOST, PORT))
    connection.listen()
    conn, addr = connection.accept()
    with conn:
        print(f"Connected by {addr}")
        message()
        while True:
            data = conn.recv(1024)
            print(f'{data}')
            conn.sendall(data)
            if not data:
                break


def multi_threading():
    pass

def identite():
    pass

def ui():
    pass

def main():
    pass